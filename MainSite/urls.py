from django.urls import path

from . import views

app_name = 'MainSite'

urlpatterns = [
    path('', views.index, name='index'),
    path('who-needs-a-consortium/', views.who_needs_a_consortium, name='who_needs_a_consortium'),
    path('what-can-elite-do-for-you/', views.what_can_elite_do_for_you, name='what_can_elite_do_for_you'),
    path('pricing/', views.pricing, name='pricing'),
    path('did-you-know-dot-requires/', views.did_you_know_dot_requires, name='did_you_know_dot_requires'),
    path('contact-us/', views.contact_us, name='contact_us'),
]
