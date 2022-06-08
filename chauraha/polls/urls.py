from django.urls import path
from . import views
from .views  import ChoiceListView, ChoiceView


urlpatterns = [
    path('choice/', ChoiceListView.as_view(), name='choicelist'),
    path('choice/<int:pk>/', ChoiceView.as_view(), name='choicedetail'),
    path('vote/', views.ChoiceVote, name='vote'),
]


