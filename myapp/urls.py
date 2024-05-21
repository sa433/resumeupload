from django.urls import path
from myapp.views import HomeView, CandidateView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', HomeView.as_view(), name='HomeView'),
    path('candidate/<int:pk>/', CandidateView.as_view(), name='candidate'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)