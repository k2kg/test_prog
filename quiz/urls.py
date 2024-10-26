from django.urls import path
from . import views

urlpatterns = [
    path('<int:test_id>/', views.take_test, name='take_test'),
]
