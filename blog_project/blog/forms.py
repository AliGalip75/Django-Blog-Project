from django import forms
from blog.models import Post

'''class PostCreateForm(forms.Form):
    title = forms.CharField(label='Post Title',
                            max_length=5,
                            error_messages={'required':'Please Enter A Value', 'max_length':'max 5'},
                            widget=forms.TextInput(attrs={'class':'form-control'})
                            )#required zaten varsayilan olarak true
    content = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}))
    image = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))'''
    

class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','content','category','author','image','is_active')
        labels = {'title':'Title',
                  'content':'Content',
                  'category':'Category',
                   'author':'Author',
                  'image':'Image',
                  'is_active':'Active',
                  }
        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'content':forms.Textarea(attrs={'class':'form-control'}),
            'category':forms.Select(attrs={'class': 'form-select'}),
            'author':forms.Select(attrs={'class':'form-select'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'is_active':forms.CheckboxInput(attrs={'class':'form-check'})
        }
        error_messages={
            'title':{
                'required':'Please enter title',
                'max_length':'Please enter max 50 char'
            },
            'content':{
                'required':'please enter content'
            }
            
        }
        
        
class EditPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','content','category','author','image','is_active')
        labels = {'title':'Title',
                  'content':'Content',
                  'category':'Category',
                  'author':'Author',
                  'image':'Image',
                  'is_active':'Active',
                  }
        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'content':forms.Textarea(attrs={'class':'form-control'}),
            'category':forms.Select(attrs={'class': 'form-select'}),
            'author':forms.Select(attrs={'class':'form-select'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'is_active':forms.CheckboxInput(attrs={'class':'form-check'})
        }
        error_messages={
            'title':{
                'required':'Please enter title',
                'max_length':'Please enter max 50 char'
            },
            'content':{
                'required':'please enter content'
            }
            
        }