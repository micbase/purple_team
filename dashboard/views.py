
from django.shortcuts import get_object_or_404, render_to_response
from django.views.generic import (
    CreateView,
    ListView,
    TemplateView
)

from dashboard.forms import (
    CreateTopicForm,
)
from dashboard.models import Class, Topic, Post


class ResultView(ListView):
    template_name = 'dashboard/result.html'
    paginate_by = 30

    def get_queryset(self):
        class_field = self.request.GET.get("class_name", "")
        return Class.objects.filter(
            class_name__icontains=class_field,
        )

    def get_context_data(self, **kwargs):
        context = super(ResultView, self).get_context_data(**kwargs)
        context['text'] = 'Purple Team'
        return context


class DashboardView(TemplateView):
    template_name = 'dashboard/index.html'

    def get_context_data(self, **kwargs):
        context = super(DashboardView, self).get_context_data(**kwargs)
        context['text'] = 'Purple Team'
        return context


class CreateTopicView(CreateView):
    template_name = 'dashboard/create_topic.html'
    model = Topic
    form_class = CreateTopicForm

    def get_success_url(self):
        return '/topics/' + self.kwargs['class_id']

    def get_form_kwargs(self):
        kwargs = super(CreateTopicView, self).get_form_kwargs()
        kwargs['class_id'] = self.kwargs['class_id']
        kwargs['author'] = 2
        return kwargs

    def get_context_data(self, **kwargs):
        context = super(CreateTopicView, self).get_context_data(**kwargs)
        context['class_id'] = self.kwargs['class_id']
        return context


class CreatePostView(TemplateView):
    template_name = 'dashboard/create_post.html'

    def get_queryset(self):
        return render_to_response('create_post.html')

    def get_context_data(self, **kwargs):
        context = super(CreatePostView, self).get_context_data(**kwargs)
        context['text'] = 'Hello World, Purple Team'
        return context


class TopicsView(ListView):
    template_name = 'dashboard/topics.html'
    paginate_by = 30
    context_object_name = 'topics'

    def get_queryset(self):
        class_id = self.kwargs['class_id']
        self.course = Class.objects.get(pk=class_id)
        return Topic.objects.filter(
            class_id=class_id,
        )

    def get_context_data(self, **kwargs):
        context = super(TopicsView, self).get_context_data(**kwargs)
        context['course'] = self.course
        return context


class PostsView(ListView):
    template_name = 'dashboard/posts.html'
    paginate_by = 30

    def get_queryset(self):
        topic_id = self.kwargs['topic_id']
        return Post.objects.filter(
            topic=topic_id,
        )

    def get_topic(self):
        topic_id = self.kwargs['topic_id']
        return Topic.objects.get(pk=topic_id)

    def get_context_data(self, **kwargs):
        context = super(PostsView, self).get_context_data(**kwargs)
        context['text'] = 'Purple Team'
        context['topic'] = self.get_topic()
        context['reply'] = self.get_queryset()
        return context
