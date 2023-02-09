from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('products/', views.SnippetList.as_view()),
    path('GenericViewProducts/<Product_name>/', views.GenericViews.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
