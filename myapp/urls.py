
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.todo_list, name='todo_list'),
    path('complete/<int:todo_id>/', views.complete_todo, name='complete_todo'),
    path('delete/<int:todo_id>/', views.delete_todo, name='delete_todo'),
    
    # Existing login/logout paths
    path('login/', auth_views.LoginView.as_view(template_name='myapp/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    
    # New signup path
    path('signup/', views.signup, name='signup'),
]