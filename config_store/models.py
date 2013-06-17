from django.db import models
import uuid

def make_uuid():
    return str(uuid.uuid4())

class ConfigObjectDefinition(models.Model):
    parent_obj_def = models.ForeignKey('self', null=True, related_name='children',blank=True)
    uuid = models.CharField(max_length=36, primary_key=True,
      default=make_uuid, editable=False)
    name = models.CharField(max_length=20)
    display_name = models.CharField(max_length=60)


class ConfigObjectField(models.Model):
    TYPE_CHOISE = (
       ("s", "string"),
       ("i", "integer"),
       ("b", "boolean"),
       ("e", "enum"),

    )
    conf_object_def = models.ForeignKey('ConfigObjectDefinition', related_name='cols')
    uuid = models.CharField(max_length=36, primary_key=True,
      default=make_uuid, editable=False)
    property_name = models.CharField(max_length=20)
    property_display_name = models.CharField(max_length=60)
    property_type = models.CharField(max_length=10, choices = TYPE_CHOISE)
    default_value = models.TextField()

    class Meta:
        unique_together = ('conf_object_def', "property_name")

    def __unicode__(self):
        return '%s' % (self.property_name)

# when object field type is enum, will look up from this table to get value scope.
class ConfigObjectFieldScope(models.Model):
    conf_obj_field = models.ForeignKey('ConfigObjectField', related_name="scope")
    uuid = models.CharField(max_length=36, primary_key=True,
      default=make_uuid, editable=False)
    value = models.CharField(max_length=20)


class ConfigInstance(models.Model):
    parent_instance = models.ForeignKey('self', null=True)
    conf_object_def = models.ForeignKey('ConfigObjectDefinition')
    uuid = models.CharField(max_length=36, primary_key=True,
      default=make_uuid, editable=False)
    value = models.TextField()


class ConfigInstanceValue(models.Model):
    conf_instance = models.ForeignKey('ConfigInstance', related_name="fields")
    conf_obj_field = models.ForeignKey('ConfigObjectField')
    uuid = models.CharField(max_length=36, primary_key=True,
      default=make_uuid, editable=False)
    value = models.TextField()


