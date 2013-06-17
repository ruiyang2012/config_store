from rest_framework import serializers
from config_store.models import ConfigObjectDefinition, ConfigObjectField, ConfigObjectFieldScope, ConfigInstance, ConfigInstanceValue

PARENT_DEPTH = 10

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
    parent_obj_def = serializers.PrimaryKeyRelatedField()
    cols = ConfObjFieldsSerializer(many=True)
    read_only_fields = ("uuid")
    class Meta:
        model = ConfigObjectDefinition
        fields = ('uuid', "parent_obj_def", 'name', 'display_name', "cols")
# seems to be a bug in restfrwamework, it is only include one level of parent at a time.
for i in range(PARENT_DEPTH):
  ConfObjDefSerializer.base_fields['parent_obj_def'] = ConfObjDefSerializer()

class ConfInstanceSerializer(serializers.ModelSerializer):
    read_only_fields = ("uuid")

    class Meta:
        model = ConfigInstance
        fields = ('uuid', 'parent_instance', 'conf_object_def', 'value')


class ConfInstanceFieldSerializer(serializers.ModelSerializer):
    read_only_fields = ("uuid")
    conf_obj_field = serializers.SlugRelatedField(read_only=True, slug_field='property_name')
    class Meta:
        model = ConfigInstanceValue
        fields = ('conf_obj_field', 'value')

class ConfInstanceDetailsSerializer(serializers.ModelSerializer):
    read_only_fields = ("uuid")
    fields = ConfInstanceFieldSerializer(many=True)
    conf_object_def = ConfObjDefSerializer()

    class Meta:
        model = ConfigInstance
        fields = ('uuid', 'parent_instance', 'conf_object_def', 'value', 'fields')
for i in range(PARENT_DEPTH):
  ConfInstanceDetailsSerializer.base_fields['parent_instance'] = ConfInstanceDetailsSerializer()



