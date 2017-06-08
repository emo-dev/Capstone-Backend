from django.conf.urls import url
import todo.views 

app_name = "todo"
urlpatterns = [
    url(r'^home$', todo.views.home, name='home'),
    url(r'^register$', todo.views.register, name='register'),
    url(r'^login$', todo.views.login_user, name='login_user'),
    url(r'^logout$', todo.views.logout_user, name='logout_user'),
    url(r'^create$', todo.views.create, name='create'),
    url(r'^delete$', todo.views.delete, name='delete'),
    url(r'^todo/(?P<todo_id>[0-9]+)$', todo.views.todo, name='todo')
]
