from rest_framework import serializers

from . import models

class GoogleAuth(serializers.Serializer):
    """ Сариализация данных от google """

    email = serializers.EmailField()
    token = serializers.CharField()

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.AuthUser
        fields = ('avatar', 'country', 'city', 'bio', 'display_name')

class SocialLinkSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = models.SocialLinks
        fields = ('id', 'link')

class AuthorSerializer(serializers.ModelSerializer):
    social_links = SocialLinkSerializer(many=True)
    class Meta:
        model = models.AuthUser
        fields = ('id', 'avatar', 'country', 'city', 'bio', 'display_name', 'social_links')



