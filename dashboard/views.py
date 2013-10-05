
from django.db.models import Count
from django.views.generic import ListView

from dashboard.models import UserSkill


class DashboardView(ListView):
    template_name = 'dashboard/index.html'
    paginate_by = 10

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
        final_user = [item.user for item in strength_match
                if item.user_id in uid_list]

        return final_user

    def get_context_data(self, **kwargs):
        context = super(DashboardView, self).get_context_data(**kwargs)
        context['text'] = 'Hello World, Purple Team'
        return context
