from django.urls import path
from wacky_widgets import views

urlpatterns = [
  path('', views.home, name='home'),
  path('<int:widget_id>/delete', views.Delete, name='delete'),
]