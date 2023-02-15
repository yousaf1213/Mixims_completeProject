from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('products/', views.SnippetList.as_view()),
    path('GenericViewProducts/<int:pk>', views.GenericViews.as_view()),
    path('GetorInsertProduct/', views.GetorInsertProduct.as_view()),
    path('GetorInsertUser/', views.GetorInsertUser.as_view()),
    path('UserCrud/<int:pk>', views.UserCrud.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
