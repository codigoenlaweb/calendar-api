from rest_framework import serializers
from modules.events.models import Event
from modules.users.models import User
from django.utils.translation import gettext_lazy as _

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['id', 'title', 'note', 'start', 'end']
        read_only_fields = ('user', 'id')

    def create(self, validated_data):
        user = self.context['request'].user
        return Event.objects.create(user=user, **validated_data)

    def validate(self, data):
        """
        Check that the start is before the stop.
        """
        if data['start'] >= data['end']:
            raise serializers.ValidationError(_("the start date must be less than the end date"))
        return data