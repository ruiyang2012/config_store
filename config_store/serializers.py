from rest_framework import serializers
from config_store.models import ConfigObjectDefinition, ConfigObjectField, ConfigObjectFieldScope, ConfigInstance, ConfigInstanceValue

class ConfigObjectFieldScopeSerializer(serializers.ModelSerializer):
    read_only_fields = ("uuid")
    class Meta:
        model = ConfigObjectFieldScope
        fields = ('value')

class ConfObjFieldsSerializer(serializers.ModelSerializer):
    read_only_fields = ("uuid")
    class Meta:
        model = ConfigObjectField
        fields = ('uuid', 'property_name', 'property_type', 'property_display_name', "default_value")

class ConfObjDefSerializer(serializers.ModelSerializer):
    cols = serializers.RelatedField(many=True)
    read_only_fields = ("uuid")
    class Meta:
        model = ConfigObjectDefinition
        fields = ('uuid', 'parent_obj_def', 'name', 'display_name', "cols")
