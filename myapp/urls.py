# from django.urls import path

# from .import views

# urlpatterns = [

#     path('', views.index, name= "index"),
#     path('register', views.register, name= "register"),
#     path('dashboard', views.dashboard, name= "dashboard"),
#     path('my-login', views.mylogin, name= "my-login"),
#     path('profile_management', views.profilemanagement, name= "profile_management"),
#     path('plot/', views.plot_view, name='plot_view'),

# ]


#-----------------------------------------


from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('register/', views.register, name="register"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('my-login/', views.mylogin, name="my-login"),
    path('profile_management/', views.profilemanagement, name="profile_management"),
    path('plot/', views.plot_view, name='plot_view'),
    path('plotchart/', views.plot_chart, name='plot_chart'),
    path('plotchart/<str:bus_id>/', views.plot_chart, name='plot_chart'),
    path('plotchart/<str:bus_id>/', views.plot_chart, name='plot_chart'),   
    path('plotchart/', views.plot_chart, name='plot_chart'),
]
