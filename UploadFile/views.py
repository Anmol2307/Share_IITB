from django.shortcuts import render_to_response

from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from UploadFile.models import Document
from UploadFile.forms import DocumentForm
# Create your views here.

def add_document(request):
  context = RequestContext(request)

  if request.method == 'POST':
    form = DocumentForm(request.POST)
    if form.is_valid():
      form.save(commit=True)
      return index(request)
    else:
      print form.errors
  else:
    form = DocumentForm()
  return render_to_response('UploadFile/upload_file.html',{'form':form},context)
