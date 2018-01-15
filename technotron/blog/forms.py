from django import forms
from blog.models import Post, Comments

class PostForm(forms.ModelForm):
#attach form to model
    class Meta():
        model = Post
        fields = ('author','title','text')

        #create widgets to style inside meta class
        #specify css classes as a dictionary values for fields as keys
        widgets = {

            'title':forms.TextInput(attrs={'class':'textinputclass'}),
            'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea postcontent'})
        }

class CommentsForm(forms.ModelForm):
#attach form to model
        class Meta():
            model = Comments
            fields = ('author','text')

            widgets = {

                'author':forms.TextInput(attrs={'class':'textinputclass'}),
                'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea'})
            }
