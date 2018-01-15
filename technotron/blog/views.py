from django.shortcuts import render,get_object_or_404,redirect
from django.utils import timezone
from blog.forms import PostForm,CommentsForm
from django.urls import reverse_lazy
from django.views.generic import (TemplateView,ListView,DeleteView,
                                    DetailView,CreateView,UpdateView)
from blog.models import Post,Comments
from django.contrib.auth.mixins import LoginRequiredMixin

#this import is used for function based views
from django.contrib.auth.decorators import login_required

# About page view
class AboutView(TemplateView):
    template_name = 'about.html'

# Post list view
class PostListView(ListView):
    model = Post

    def get_queryset(self):
        return Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')

# Post Detail view
class PostDetailView(DetailView):
    model = Post

# Create Post view
class CreatePostView(LoginRequiredMixin,CreateView):
# condition is login required to create any post_list
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'
    form_class = PostForm
    model = Post

# Post Update view
class PostUpdateView(LoginRequiredMixin,UpdateView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'
    form_class = PostForm
    model = Post

# Post Delete view
class PostDeleteView(LoginRequiredMixin,DeleteView):
    model = Post
    success_url = reverse_lazy('post_list')

# Draft List view
class DraftListView(LoginRequiredMixin,ListView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_draft_list.html'
    model = Post

    def get_queryset(self):
        return Post.objects.filter(published_date__isnull=True).order_by('created_date')

############################################################################################
# Function Basd Views
############################################################################################

# Publish Post
@login_required
def post_publish(request,pk):
    post = get_object_or_404(Post,pk=pk)
    post.publish()
    return redirect('post_detail',pk=pk)

# Add comments to the post
@login_required
def add_comments_to_post(request,pk):
    post = get_object_or_404(Post,pk=pk)
    if request.method == 'POST':
        form = CommentsForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail',pk=post.pk)
    else:
        form = CommentsForm()
    return render(request,'blog/comment_form.html',{'form':form})

# Comment Approve
@login_required
def comment_approve(request,pk):
    comment = get_object_or_404(Comments,pk=pk)
    comment.approve()
    return redirect('post_detail',pk=comment.post.pk)

# COmment Remove
@login_required
def comment_remove(request,pk):
    comment = get_object_or_404(Comments,pk=pk)
    post_pk = comment.post.pk
    comment.delete()
    return redirect('post_detail',pk=post_pk)
