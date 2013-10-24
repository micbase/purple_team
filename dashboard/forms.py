from django import forms
from dashboard.models import Class,Topic, Post

class CreateTopicForm(forms.ModelForm):

	def __init__(self, class_id, author, *args, **kwargs):
		super(CreateTopicForm, self).__init__(*args, **kwargs)
		self.class_id = class_id
		self.topic_author_id = author

	class Meta:
		model = Topic
		exclude = ['topic_author','class_id']
		widgets = {
		'topic_title':forms.TextInput(attrs={
			'class' : 'form-control',
			'placeholder' : 'Enter Topic Title'
			}),
		'topic_content':forms.TextInput(attrs={
			'class' : 'form-control',
			'placeholder' : 'Enter Topic Content'
			})
		}	
