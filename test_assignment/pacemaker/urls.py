from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('api/scrape',views.PacemakerScrape.as_view(),name='scrape_data'),
    path('api/search',views.PacemakerList.as_view(),name='search_api')
]
 