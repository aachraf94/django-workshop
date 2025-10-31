from rest_framework import serializers
from .models import User, Task, Project


class UserSerializer(serializers.ModelSerializer):
    """Simple serializer for User model"""
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'role']
        read_only_fields = ['id']


class UserCreateSerializer(serializers.ModelSerializer):
    """Serializer for user registration"""
    password = serializers.CharField(write_only=True)
    
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'role']
        read_only_fields = ['id']
    
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class TaskSerializer(serializers.ModelSerializer):
    """Simple serializer for Task model"""
    assigned_to_email = serializers.EmailField(source='assigned_to.email', read_only=True)
    created_by_email = serializers.EmailField(source='created_by.email', read_only=True)
    
    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'project', 'assigned_to', 
                  'assigned_to_email', 'created_by', 'created_by_email', 'created_at']
        read_only_fields = ['id', 'created_by', 'created_at']


class ProjectSerializer(serializers.ModelSerializer):
    """Simple serializer for Project model"""
    owner_email = serializers.EmailField(source='owner.email', read_only=True)
    
    class Meta:
        model = Project
        fields = ['id', 'name', 'description', 'owner', 'owner_email', 
                  'created_at']
        read_only_fields = ['id', 'owner', 'created_at']
