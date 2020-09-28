
from django.urls import path,include
from .views import CompanyL,CompanyDetails,MobileL,MobileDetails


urlpatterns = [
   
    path('company/',CompanyL.as_view()),
    path('company/<int:id>/',CompanyDetails.as_view()),
    path('company/<int:id>/mobile/',MobileL.as_view()),
    path('company/<int:cId>/mobile/<int:id>/',MobileDetails.as_view()),
]
