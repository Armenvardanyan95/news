from rest_framework import serializers
from django.contrib.auth import update_session_auth_hash
from .models import User


class UserSerializer(serializers.HyperlinkedModelSerializer):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].allow_blank = False
        self.fields['email'].required = True

        if self.instance:
            self.fields['password'].required = False
            self.fields['repeat_password'].required = False

    class Meta:
        model = User
        fields = ('id', 'email', 'repeat_password', 'password', 'topics',)
        extra_kwargs = {
            'password': {'write_only': True, },
        }

    repeat_password = serializers.CharField(allow_blank=False, write_only=True)
    id = serializers.CharField(read_only=True)

    def create(self, validated_data):

        validated_data.pop('repeat_password')
        new_object = super().create(validated_data)
        new_object.set_password(validated_data['password'])
        new_object.save()
        return new_object

    def update(self, instance, validated_data):

        validated_data.pop('repeat_password')
        updated_object = super().update(instance, validated_data)
        if 'password' in validated_data:
            updated_object.set_password(validated_data['password'])
            updated_object.save()
            update_session_auth_hash(self.context['request'], updated_object)

        return updated_object

    def validate(self, data):
        self.check_unique_email(data)
        if data['password'] != data['repeat_password']:
            raise serializers.ValidationError({'password': 'Passwords don\'t match'})

        return data

    def check_unique_email(self, data):

        exist = User.objects.filter(email=data['email'])
        if self.instance:
            exist = exist.exclude(pk=self.instance.pk)

        if exist.exists():
            raise serializers.ValidationError({'email': 'This email is already taken'})

