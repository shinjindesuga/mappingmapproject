
from django.urls import path
from .views import signupfunc, loginfunc, HomeView, MapList, logoutfunc, MapDetail, MapCreate

urlpatterns = [
    path('signup/', signupfunc, name='signup'),
    path('login/', loginfunc, name = 'login'),
    path('', MapList.as_view(), name = 'list'),
    path('home/', HomeView.as_view()),
    path('logout/', logoutfunc, name='logout'),
    path('detail/<int:pk>', MapDetail.as_view(), name='detail'),
    path('create/', MapCreate.as_view(), name='create'),
]
