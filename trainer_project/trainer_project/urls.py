from django.contrib import admin
from django.urls import path

import trainer_app.views as trainer_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', trainer_view.UserListView.as_view())
]
