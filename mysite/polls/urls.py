from django.urls import path

from . import views


app_name = 'polls'
urlpatterns = [
    # ex: /polls/
    path('', views.IndexView.as_view(), name='index'),
    # ex: /polls/4/
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # ex: /polls/4/results/
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    # ex: /polls/4/vote
    path('<int:question_id>/vote/', views.vote, name='vote'),
]

# urlpatterns = [
#     # ex: /polls/
#     path('', views.index, name='index'),
#     # ex: /polls/4/
#     path('<int:question_id>/', views.detail, name='detail'),
#     # ex: /polls/4/results/
#     path('<int:question_id>/results/', views.results, name='results'),
#     # ex: /polls/4/vote
#     path('<int:question_id>/vote/', views.vote, name='vote'),
# ]

