# -*- coding: utf-8 -*-
from django import forms
from UploadFile.models import Document

class DocumentForm(forms.ModelForm):
  course_name = forms.CharField(max_length=100, help_text='Databases')
  course_code = forms.CharField(max_length=24, help_text='CS 347')
  category = forms.CharField(max_length=24)
  year = forms.IntegerField(initial=0, help_text='2014')
  prof = forms.CharField(max_length=100, help_text='Dr. Thomas Cormen')
  description = forms.CharField(max_length=1000, help_text='About the file')
  docfile = forms.FileField(
      label='Choose file'
  )
  class Meta:
    model = Document