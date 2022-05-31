
from django.contrib import admin
from django.urls import path
from app.views import home, login, SignUp, add_todo,signout, delete_todo, change_todo


urlpatterns = [
   path('', home, name='home'),
   path('Login/', login, name='Login'),
   path('SignUp/', SignUp),
   path('add-todo/',add_todo),
   path('delete-todo/<int:id>',delete_todo),
   path('change-status/<int:id>/<str:status>',change_todo),
   path('Logout/',signout)
]