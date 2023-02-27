from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('products/', views.SnippetList.as_view()),
    path('GenericViewProducts/<int:pk>', views.GenericViews.as_view()),
    path('GetorInsertProduct/', views.GetorInsertProduct.as_view()),
    path('GetorInsertUser/', views.GetorInsertUser.as_view()),
    path('UserCrud/<int:pk>', views.UserCrud.as_view()),
    path("fakeinsert/", views.AsyncInsertUsingThread),
    path("webscrapp/", views.WebScrapp),
    path("dictcomp/", views.dictComp),
    path("listcomp/", views.listComp),
    path("gressearch/", views.postgresSearch),
    path("stripepayment/", views.stripePayment),
    path("striperefund/", views.stripeRefund),
    path("login/", views.login),
    path("", views.index, name="index"),
    path("data/<str:room_name>/", views.room, name="room"),
    path("messageinsert/", views.messageInsert),
    path("getmessages/", views.getMessages),

]

urlpatterns = format_suffix_patterns(urlpatterns)
