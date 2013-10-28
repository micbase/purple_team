from django import forms
from dashboard.models import Topic,Post


class CreateTopicForm(forms.ModelForm):

    def __init__(self, course_id, author, *args, **kwargs):
        super(CreateTopicForm, self).__init__(*args, **kwargs)
        self.instance.course_id = course_id
        self.instance.author = author

    class Meta:
        model = Topic
        exclude = ['author', 'course', 'status']
        widgets = {
                'title': forms.TextInput(attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter Topic Title'
                    }),
                'content': forms.Textarea(attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter Topic Content'
                    })
                }

class CreatePostForm(forms.ModelForm):

    def __init__(self, topic_id, author, *args, **kwargs):
        super(CreatePostForm, self).__init__(*args, **kwargs)
        self.instance.topic_id = topic_id
        self.instance.author = author

    class Meta:
        model = Post
        exclude = ['author', 'topic']
        widgets = {
                'content': forms.Textarea(attrs={
                    'class': 'input-block-level',
                    'rows' : '5',
                    'placeholder': 'Enter Post Content',
                    'name' : 'post_content',
                    'id' : 'post_content'
                    })
                }
              