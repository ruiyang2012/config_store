from rest_framework import generics

from config_store.models import ConfigObjectDefinition, ConfigObjectField, ConfigObjectFieldScope, ConfigInstance, ConfigInstanceValue
from config_store import serializers

class ConfigObjectDefinitionList(generics.ListAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = ConfigObjectDefinition.objects.all()
    serializer_class = serializers.ConfObjDefSerializer

class ConfigObjectDefinitionDetail(generics.RetrieveAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    lookup_fields = ("uuid")
    queryset = ConfigObjectDefinition.objects.all()
    serializer_class = serializers.ConfObjDefSerializer


class ConfigInstanceList(generics.ListAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = ConfigInstance.objects.all()
    serializer_class = serializers.ConfInstanceSerializer


class ConfigInstanceDetail(generics.RetrieveAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    lookup_fields = ("uuid")
    queryset = ConfigInstance.objects.all()
    serializer_class = serializers.ConfInstanceDetailsSerializer