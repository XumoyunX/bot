from django.urls import path    
from myapp.views import *




urlpatterns = [


    path('region/', Region.as_view(), name='region/'),
    path("district/<int:pk>/", District.as_view(), name="district")

]