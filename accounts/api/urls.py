from django.contrib import admin
from django.urls import path, include
from .views import UserGetView, UserDeleteView, UserCreateView, UserUpdateView, UserListView

urlpatterns = [
    path('get/<int:owner_id>/', UserGetView.as_view(), name='user-get'),
    path('delete/<int:owner_id>/', UserDeleteView.as_view(), name='user-delete'),
    path('update/<int:owner_id>/', UserUpdateView.as_view(), name='user-update'),
    path('create/<int:owner_id>/', UserCreateView.as_view(), name='user-create'),
    path('list/', UserListView.as_view(), name='user-list'),
]
