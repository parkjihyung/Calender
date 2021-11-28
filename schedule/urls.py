from django.urls import path

from . import views

app_name = 'schedule'

urlpatterns = [
    # ex /schedule/
    path('', views.index, name='index'),

    # ex /schedule/get_events/
    path('get_events/', views.get_events, name='get_events'),

    path('set_all_day_event/', views.set_all_day_event, name='set_all_day_event'),
]

    
'''
    # ex /polls/5
    path('specifics/<int:question_id>/', views.detail, name='detail'),

    # ex /polls/5/results
    path('<int:question_id>/results/', views.results, name='results'),

    # ex /polls/5/vote
    path('<int:question_id>/vote/', views.vote, name='vote'),
'''