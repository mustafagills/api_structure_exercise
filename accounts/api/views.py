from rest_framework import generics
from accounts.models import User
from .serializers import UserSerializer

class UserGetView(generics.RetrieveAPIView):
    lookup_field = 'owner_id'
    serializer_class = UserSerializer
    queryset = User.objects.all()

class UserDeleteView(generics.DestroyAPIView):
    lookup_field = 'owner_id'
    serializer_class = UserSerializer
    queryset = User.objects.all()

class UserCreateView(generics.CreateAPIView):
    lookup_field = 'owner_id'
    serializer_class = UserSerializer
    queryset = User.objects.all()

class UserUpdateView(generics.UpdateAPIView):
    lookup_field = 'owner_id'
    serializer_class = UserSerializer
    queryset = User.objects.all()

class UserListView(generics.ListAPIView):
    lookup_field = 'owner_id'
    serializer_class = UserSerializer
    queryset = User.objects.all()
