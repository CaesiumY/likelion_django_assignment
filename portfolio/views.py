from django.shortcuts import render
from django.utils import timezone
# Create your views here.


def portfolio_view(request):
    now = timezone.now()
    context = {
        'now': now,
    }
    return render(request, 'portfolio.html', context)
