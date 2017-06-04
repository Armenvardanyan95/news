from django.db.models import ManyToManyField, ForeignKey


class Utilities:

    @classmethod
    def to_dict(cls, instance):
        opts = instance._meta
        data = {}
        for f in opts.concrete_fields + opts.many_to_many:
            if isinstance(f, ManyToManyField):
                if instance.pk is None:
                    data[f.name] = []
                else:
                    data[f.name] = list(f.value_from_object(instance).values())
            elif isinstance(f, ForeignKey):
                data[f.name + "_details"] = f.rel.to.objects.filter(id=f.value_from_object(instance)).values()[0]
            else:
                data[f.name] = f.value_from_object(instance)
        return data