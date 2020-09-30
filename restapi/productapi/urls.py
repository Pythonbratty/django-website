from django.urls import path
from .views import TextAPIView


urlpatterns= [

 path("api/view", TextAPIView.as_view()),
 #path("api/Periods", PeriodListView.as_view()),
]