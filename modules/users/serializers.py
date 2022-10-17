from django.db import transaction
from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer
from modules.users.models import User
from modules.events.serializers import EventSerializer

class CustomRegisterSerializer(RegisterSerializer):

    # Define transaction.atomic to rollback the save operation in case of error
    @transaction.atomic
    def save(self, request):
        user = super().save(request)
        user.save()
        return user


class CustomUserDetailsSerializer(serializers.ModelSerializer):
    events = EventSerializer(many=True)

    class Meta:
        model = User
        fields = (
            'id',
            'email',
            'username',
            'events',
        )
        read_only_fields = ('id', 'email', 'email')