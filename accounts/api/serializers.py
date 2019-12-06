from rest_framework import serializers
from accounts.models import User

#Userserializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'owner_id',
            'email',
            'name',
            'surname',
            'registiration_date',
            'age',
            'gender',
            'education_level',
            'active',
            'staff',
            'admin',
        ]

    #read_only_fields = ['user']

    #def validate_title(self, value):
