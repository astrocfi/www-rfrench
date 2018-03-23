from django.shortcuts import render
from .models import Gig
import datetime

# Create your views here.
def calling(request):
    gigs = Gig.objects.order_by('start_date')

    now = datetime.datetime.now()
    current_year = now.year
    current_date = now.strftime('%y-%m-%d')
    years = []
    for gig in gigs:
        if (gig.start_date.year >= current_year and
            gig.start_date.year not in years):
            years.append(gig.start_date.year)
    years.sort()
    return render(request, 'calling/calling.html',
                  {'gigs': gigs,
                   'years': years,
                   'current_date': current_date,
                   'current_year': current_year})
