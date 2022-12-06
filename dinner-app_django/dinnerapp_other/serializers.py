from rest_framework import serializers
from .models import Profile
from .models import Dinner
from .models import Chat
from .models import Message
from .models import User
from .models import Photos


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__' 

class PhotosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photos
        fields = '__all__' 

class DinnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dinner
        fields = '__all__' 

class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = '__all__' 

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__' 

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__' 
