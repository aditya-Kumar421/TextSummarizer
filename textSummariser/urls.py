from django.urls import path
from .views import SummarizeTextView

urlpatterns = [
    path('summarize/', SummarizeTextView.as_view(), name='summarize_text'),
]
