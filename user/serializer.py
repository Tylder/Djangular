from django.contrib.auth import get_user_model
from rest_framework import serializers

# Get the UserModel
UserModel = get_user_model()

class UserDetailsSerializer(serializers.ModelSerializer):
    """
    User model w/o password
    """
    teacherprofile = serializers.PrimaryKeyRelatedField(many=False, read_only=True)
    studentprofile = serializers.PrimaryKeyRelatedField(many=False, read_only=True)

    class Meta:
        model = UserModel
        fields = ('pk', 'username', 'email', 'first_name', 'last_name', 'teacherprofile', 'studentprofile')
        read_only_fields = ('email', )