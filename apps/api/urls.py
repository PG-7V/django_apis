from django.urls import path

from apps.api.views import BookApiView

urlpatterns = [
    path('', BookApiView.as_view()),
]
