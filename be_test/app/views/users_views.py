from rest_framework import filters, viewsets
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from django.db.transaction import atomic
from rest_framework.decorators import action

from be_test.app.serializers.user_serializers import UserSerializers


class UsersViewsSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializers
    http_method_names = ['get', 'post', 'put', 'delete']
    queryset = User.objects.all()

    @action(detail=False, methods=['POST'], url_path='login')
    def register(self, request, *args, **kwargs):
        pass
