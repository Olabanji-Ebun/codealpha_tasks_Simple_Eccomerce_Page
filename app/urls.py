from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .import views

urlpatterns = [
    path("", views.home),
    path("category/<slug:val>", views.CategoryView.as_view(), name="category"),
]*static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
