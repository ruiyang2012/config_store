from rest_framework import generics

from config_store.models import ConfigObjectDefinition, ConfigObjectField, ConfigObjectFieldScope, ConfigInstance, ConfigInstanceValue
from config_store import serializers

class ConfigObjectDefinitionList(generics.ListCreateAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = ConfigObjectDefinition.objects.all()
    serializer_class = serializers.ConfObjDefSerializer

class ConfigObjectDefinitionDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = ConfigObjectDefinition.objects.all()
    serializer_class = serializers.ConfObjDefSerializer