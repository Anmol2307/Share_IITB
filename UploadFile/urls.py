from django.conf.urls import patterns, url
from UploadFile import views

urlpatterns = patterns('',
    url(r'^$',views.add_document,name='add_document'),
  )