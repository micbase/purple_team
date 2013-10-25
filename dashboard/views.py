
from django.views.generic import (
    CreateView,
    ListView,
    TemplateView
)

from auth.views import LoginRequiredMixin
from dashboard.forms import (
    CreateTopicForm,
)
from dashboard.models import Course, Topic, Post


class CourseView(ListView):
    template_name = 'dashboard/courses.html'
    paginate_by = 20

    def get_queryset(self):
        course_name = self.request.GET.get("course_name", "")
        return Course.objects.filter(
            name__icontains=course_name,
        )


class CreateTopicView(LoginRequiredMixin, CreateView):
    template_name = 'dashboard/create_topic.html'
    model = Topic
    form_class = CreateTopicForm

    def get_success_url(self):
        return '/topics/' + self.kwargs['course_id']

    def get_form_kwargs(self):
        kwargs = super(CreateTopicView, self).get_form_kwargs()
        kwargs['course_id'] = self.kwargs['course_id']
        kwargs['author'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super(CreateTopicView, self).get_context_data(**kwargs)
        context['course_id'] = self.kwargs['course_id']
        return context


class CreatePostView(TemplateView):
    template_name = 'dashboard/create_post.html'

    def get_context_data(self, **kwargs):
        context = super(CreatePostView, self).get_context_data(**kwargs)
        context['text'] = 'Hello World, Purple Team'
        return context


class TopicsView(ListView):
    template_name = 'dashboard/topics.html'
    paginate_by = 20
    context_object_name = 'topics'

    def get_queryset(self):
        course_id = self.kwargs['course_id']
        return Topic.objects.filter(
            course_id=course_id,
        )

    def get_course(self):
        course_id = self.kwargs['course_id']
        return Course.objects.get(pk=course_id)

    def get_context_data(self, **kwargs):
        context = super(TopicsView, self).get_context_data(**kwargs)
        context['course'] = self.get_course()
        return context


class PostsView(ListView):
    template_name = 'dashboard/posts.html'
    paginate_by = 20
    context_object_name = 'reply'

    def get_queryset(self):
        topic_id = self.kwargs['topic_id']
        return Post.objects.filter(
            topic_id=topic_id,
        )

    def get_topic(self):
        topic_id = self.kwargs['topic_id']
        return Topic.objects.get(pk=topic_id)

    def get_context_data(self, **kwargs):
        context = super(PostsView, self).get_context_data(**kwargs)
        context['topic'] = self.get_topic()
        return context
