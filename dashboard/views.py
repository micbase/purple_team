
from django.db.models import Count
from django.views.generic import TemplateView

from dashboard.models import UserSkill


class DashboardView(TemplateView):
    template_name = 'dashboard/index.html'

    def get_queryset(self):
        s_id = 3
        w_id = 4

        strength_match = UserSkill.objects.filter(
            skill_id=s_id,
            scale__lte=5,
        ).annotate(
            strength_counter=Count('id'),
        ).filter(
            strength_counter__gte=1,
        )

        weakness_match = UserSkill.objects.filter(
            skill_id=w_id,
            scale__gte=6,
        ).annotate(
            weakness_counter=Count('id'),
        ).filter(
            weakness_counter__gte=1,
        )

        uid_list = [item.user_id for item in weakness_match]
        final_match = [item for item in strength_match if item.user_id in uid_list]
        import pdb;pdb.set_trace()

        return final_match

    def get_context_data(self, **kwargs):
        context = super(DashboardView, self).get_context_data(**kwargs)
        context['text'] = 'Hello World, Purple Team'
        self.get_queryset()
        return context
