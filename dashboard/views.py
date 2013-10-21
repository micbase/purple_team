from django.shortcuts import get_object_or_404, render_to_response
from django.views.generic import ListView, TemplateView, DetailView
from dashboard.models import Class,Topic, Post


class GroupInfoView(DetailView):
    template_name = 'dashboard/groupInfo.html'

    def get_object(self):
        return get_object_or_404(Group, pk=self.kwargs["group_id"])

    def get_events(self):
        post_list = Post.objects.filter(
            group_id=self.kwargs["group_id"],
        )
        return post_list

    def get_context_data(self, **kwargs):
        context = super(GroupInfoView, self).get_context_data(**kwargs)
        context['text'] = 'Hello World, Purple Team'
        context['events'] = self.get_events()
        return context


class ResultView(ListView):
    template_name = 'dashboard/index.html'
    paginate_by = 30

    def get_queryset(self):
        group_field = self.request.GET.get("group_name", None)
        return Group.objects.filter(
            group_name__icontains=group_field,
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

class CreateTopicView(TemplateView):
    template_name = 'dashboard/create_topic.html'

    def get_queryset(self):
        title_field = self.request.GET.get("topic_name", None)
        content_field = self.request.GET.get("topic_desc", None)
        id_field = self.kwargs["class_id"]
        t=Topic(topic_title=topic_field, topic_content=content_field, topic_id=id_field )
        t.save()
        return render_to_response('index.html')

    def get_context_data(self, **kwargs):
        context = super(CreateTopicView, self).get_context_data(**kwargs)
        context['text'] = 'Hello World, Purple Team'
        return context

class CreatePostContentView (TemplateView):
    template_name = 'dashboard/create_post.html'

    def get_queryset(self):
        topic_field = self.kwargs["topic_id"]
        content_field = self.request.GET.get("post_content", None)
        p=Post(post_content=content_field, topic=topic_field )
        p.save()
        return render_to_response('create_post.html')

    def get_context_data(self, **kwargs):
        context = super(CreatePostContentView, self).get_context_data(**kwargs)
        context['text'] = 'Hello World, Purple Team'
        return context

class CreatePostView (TemplateView):
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

    def get_queryset(self):
        class_field = self.request.GET.get("group_name", None)
        c = Class.objects.get(class_name = class_field)
        return Topic.objects.filter(
            class_id=c.id,
        )

    def get_context_data(self, **kwargs):
        context = super(TopicsView, self).get_context_data(**kwargs)
        context['text'] = 'Purple Team'
        context['course_name'] =  self.request.GET.get("group_name", None)
        context['topics'] = self.get_queryset()
        return context

class PostsView(ListView):
    template_name = 'dashboard/posts.html'
    paginate_by = 30

    def get_queryset(self):
        topic_id = self.kwargs['group_id']
        return Post.objects.filter(
            topic=topic_id,
        )
    def get_topic(self):
        topic_id = self.kwargs['group_id']
        return Topic.objects.get(id=topic_id)


    def get_context_data(self, **kwargs):
        context = super(PostsView, self).get_context_data(**kwargs)
        context['text'] = 'Purple Team'
        context['topic'] = self.get_topic()
        context['reply'] = self.get_queryset()
        return context
