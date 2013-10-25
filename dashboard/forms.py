from django import forms
from dashboard.models import Topic


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
                'content': forms.TextInput(attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter Topic Content'
                    })
                }
