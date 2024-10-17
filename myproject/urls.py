from django.urls import path
from app import views

urlpatterns = [
    path('', views.index, name='index'),  # Route to serve the HTML page
    path('submit-form/', views.submit_form, name='your_form_submission_url'),  # URL for form submission
]