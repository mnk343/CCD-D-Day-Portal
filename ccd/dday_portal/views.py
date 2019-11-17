from django.shortcuts import render
from . import models
from . import forms
from django.shortcuts import redirect , get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse

def showAnnouncements(request ):
    context={}
    pk1 = get_object_or_404( models.poc , user = request.user)
    pk  = pk1.poc_id
    announcements = models.announcement.objects.all().filter(send_all = True).order_by('-pk')
    context['announcement'] = announcements
    context['id'] = pk
    context['poc'] = pk1
    return render(request , 'showAnnouncements.html' , context)

def showStudents(request , pk):
    context = {}
    poc = get_object_or_404( models.poc , pk = pk )
    company = poc.company
    context['shortlist'] = company.shortlist_candidate.all().filter( is_selected = False)
    context['waitlist'] = company.waiting_candidate.all().filter( is_selected = False)
    context['poc'] = poc
    context['id'] = pk
    return render(request, 'showStudents.html' , context)

def UpdateProfile(request , pk , pk2):

    candidate = get_object_or_404(models.candidate, pk=pk)
    form = forms.UpdateCandidateDetail(instance=candidate)

    if request.method == 'POST':
        form = forms.UpdateCandidateDetail(instance=candidate, data=request.POST)
        if form.is_valid():
            form.save()
        return redirect( showStudents , pk = pk2 )

    return render(request, 'UpdateCandidateDetail.html', {'form':form, 'patient':candidate})

def UpdateAnnouncement(request , pk ):
    if request.method == "POST":
        form = forms.UpdateAnnouncement(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('showAnnouncements')

    form = forms.UpdateAnnouncement
    return render(request, 'updateAnnouncement.html', {'form': form , 'id' : id})
    #
    #
    # poc = get_object_or_404(models.candidate, pk=pk)
    # form = forms.UpdateAnnouncementDetail(instance=poc)
    # form = forms.UpdateAnnouncementDetail.create()
    # if request.method == 'POST':
    #     form = forms.UpdateCandidateDetail(instance=candidate, data=request.POST)
    #     if form.is_valid():
    #         form.save()
    #     return redirect( showStudents , pk = pk2 )
    #
    # return render(request, 'UpdateCandidateDetail.html', {'form':form, 'patient':candidate})

def deleteAnnouncement(request , pk , pk2):
    app = models.announcement.objects.get(pk=pk)
    app.delete()
    return redirect('showAnnouncements' )
