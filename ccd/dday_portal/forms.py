from . import models
from django import forms

class UpdateCandidateDetail(forms.ModelForm):
    class Meta:
        model = models.candidate
        fields = [
            'start_time',
            'expected_time',
            'company_name',
            'is_selected',
            'is_interview',
        ]

class UpdateAnnouncement(forms.ModelForm):
    class Meta:
        model = models.announcement
        fields = [
            'poc',
            'description',
            'send_all',
        ]
