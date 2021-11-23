from rest_framework import serializers

from ...models import User


class UserDataSerializer(serializers.ModelSerializer):
    firstname = serializers.CharField(source='first_name')
    secondname = serializers.CharField(source='last_name')
    fathername = serializers.CharField(source='father_name')
    ship_adress = serializers.CharField(source='ship_address')
    is_anonymous = serializers.BooleanField(source='anonymous')

    class Meta:
        model = User
        fields = [
            'id', 'username', 'firstname', 'secondname', 'fathername', 'phone', 'email', 'ship_adress',
            'birthday', 'is_anonymous',
        ]