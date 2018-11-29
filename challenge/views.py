from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Challenge
from .forms import ChallengeForm
from django.shortcuts import redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . import forms     
from django.conf import settings
#from django.core.exceptions import ValidationError


def challenge_list(request):
    #Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')    
    challenges = Challenge.objects.all()
    #if request.user:
    #    challenges = Challenge.objects.filter(user=request.user)
    #else:
    #    challenges = Challenge.objects.filter(user=1)
    return render(request, 'challenge/challenge_list.html', {'challenges': challenges})



def challenge_detail(request, pk):
    #challenge = challenge.objects.get(pk=pk)
    challenge = get_object_or_404(Challenge, pk=pk)
    vprogress = 66
    #return HttpResponse(pk)
    return render(request, 'challenge/challenge_detail.html', {'challenge': challenge})

@login_required(login_url="/account/login/")
def challenge_create(request):
    if request.method == "POST":
        form = ChallengeForm(request.POST,request.FILES)
        if form.is_valid():
            #return redirect('../../challenge/')
            instance = form.save(commit=False)
            instance.user = request.user
            if instance.beat_events :
                instance.beat_points = instance.beat_events * instance.points_events
                instance.porcent = int((instance.beat_events/instance.total_events)*100)
            instance.save()
            return redirect('challenge:challenge_list')
    else:
        form = ChallengeForm()
    return render(request, 'challenge/challenge_create.html', {'form': form})

@login_required(login_url="/account/login/")
def challenge_edit(request, pk):

     challenge = get_object_or_404(Challenge, pk=pk)
     if request.method == "POST":
         form = ChallengeForm(request.POST, instance=challenge)
         if form.is_valid():
             challenge = form.save(commit=False)
             challenge.user = request.user
             challenge.created_date = timezone.now()
             if challenge.beat_events :
                challenge.beat_points = challenge.beat_events * challenge.points_events
                challenge.porcent = int((challenge.beat_events/challenge.total_events)*100)
             challenge.save()
             return redirect('challenge:challenge_list')
     else:
         form = ChallengeForm(instance=challenge)
     return render(request, 'challenge/challenge_edit.html', {'form': form})


