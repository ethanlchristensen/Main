from django.shortcuts import render
from rewards.models import Reward

def rewards_view(request):
    context = {
        'rewards': Reward.objects.all()
    }
    return render(request, "rewards/rewards_view.html", context)
