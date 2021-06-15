from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .forms import UserLoginForm
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
  path('', views.index, name = 'index'),
  path('signup/', views.signup, name = 'signup'),
  path('login/', LoginView.as_view(template_name='login.html', authentication_form=UserLoginForm), name = 'login'),
  path('logout/', LogoutView.as_view(), name = 'logout'),
  path('home/', views.home, name = 'home'),
  path('ended-tasks/', views.ended_tasks, name = 'ended_tasks'),
  path('all-tasks/', views.all_tasks, name = 'all_tasks'),
  path('add-task/', views.add_task, name = 'add_task'),
  path('task-edit/', views.task_edit, name = 'task_edit'),
  path('task-end/<int:task_id>', views.task_end, name = 'task_end'),
  path('task-delete/<int:task_id>', views.task_delete, name = 'task_delete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
