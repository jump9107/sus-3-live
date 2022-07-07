from django.urls import URLPattern, path

from landing import views

urlpatterns = {
    path("", views.landing)
}