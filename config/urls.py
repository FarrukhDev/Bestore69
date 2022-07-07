from django.contrib import admin
from django.urls import path

from mijoz.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',HomeView.as_view(),name = 'home'),
    path('muscle/',MuscleView.as_view(),name = 'muscle'),
    path('vibro/',VibroView.as_view(),name = 'vibro'),
    path('antip/',AntiView.as_view(),name = 'antip'),
]
