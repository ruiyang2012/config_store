from rest_framework import serializers
from config_store.models import ConfigObjectDefinition, ConfigObjectField, ConfigObjectFieldScope, ConfigInstance, ConfigInstanceValue

class ConfObjDefSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConfigObjectDefinition
        fields = ('uuid', 'parent_obj_def', 'name', 'display_name')