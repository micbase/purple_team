
from django.views.generic import ListView, TemplateView

from dashboard.models import UserSkill, Skill


class ResultView(ListView):
    template_name = 'dashboard/result.html'
    paginate_by = 10

    def get_queryset(self):
        strength_name = self.request.GET.get("strength", None)
        weakness_name = self.request.GET.get("weakness", None)

        try:
            s_id = Skill.objects.get(skill_name__iexact=strength_name)
            w_id = Skill.objects.get(skill_name__iexact=weakness_name)
        except Skill.DoesNotExist:
            return []

        strength_match = UserSkill.objects.filter(
            skill_id=s_id,
            scale__lte=5,
        )

        weakness_match = UserSkill.objects.filter(
            skill_id=w_id,
            scale__gte=6,
        )

        uid_list = [item.user_id for item in weakness_match]
        final_user = [item.user for item in strength_match
                if item.user_id in uid_list]

        return final_user

    def get_context_data(self, **kwargs):
        context = super(ResultView, self).get_context_data(**kwargs)
        context['text'] = 'Hello World, Purple Team'
        return context


class DashboardView(TemplateView):
    template_name = 'dashboard/index.html'

    def get_context_data(self, **kwargs):
        context = super(DashboardView, self).get_context_data(**kwargs)
        context['text'] = 'Hello World, Purple Team'
        return context
