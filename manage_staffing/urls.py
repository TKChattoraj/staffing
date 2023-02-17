from django.urls import path, include

from  manage_staffing import views


urlpatterns = [
    path('', views.index, name='index'),
    path('persons/', views.persons),
    path('employers/', views.employers),
    path('jobs/', views.jobs),
    path('person/<int:pk>', views.person),
    path('employer/<int:pk>', views.employer),
    path('job/<int:pk>', views.job),
    path('accounts/', include('django.contrib.auth.urls')),
    path('logout/', views.logout_user),
    path('login/', views.login_user)
]