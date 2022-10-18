from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from modules.events.models import Event
from .serializers import EventSerializer


class EventViewSet(viewsets.ModelViewSet):
    """
    Manage ingredients in the databases
    """
    serializer_class = EventSerializer
    queryset = Event.objects.all()
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
        Filter queryset to authenticated user.
        """
        if not self.request.user.pk:
            return self.queryset.filter(pk=0)
        return self.queryset.filter(user=self.request.user).order_by('-id')
