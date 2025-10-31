from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from drf_spectacular.utils import extend_schema, extend_schema_view, OpenApiParameter
from drf_spectacular.types import OpenApiTypes
from .models import User, Task, Project
from .serializers import (
    UserSerializer, 
    UserCreateSerializer,
    LoginSerializer,
    TaskSerializer, 
    ProjectSerializer
)


@extend_schema_view(
    list=extend_schema(description='List all users', tags=['Users']),
    retrieve=extend_schema(description='Get a specific user', tags=['Users']),
    create=extend_schema(description='Create a new user', tags=['Users']),
    update=extend_schema(description='Update a user', tags=['Users']),
    partial_update=extend_schema(description='Partially update a user', tags=['Users']),
    destroy=extend_schema(description='Delete a user', tags=['Users']),
)
class UserViewSet(viewsets.ModelViewSet):
    """CRUD operations for User"""
    queryset = User.objects.all()
    
    def get_serializer_class(self):
        if self.action == 'create':
            return UserCreateSerializer
        return UserSerializer


@extend_schema_view(
    list=extend_schema(description='List all tasks', tags=['Tasks']),
    retrieve=extend_schema(description='Get a specific task', tags=['Tasks']),
    create=extend_schema(description='Create a new task', tags=['Tasks']),
    update=extend_schema(description='Update a task', tags=['Tasks']),
    partial_update=extend_schema(description='Partially update a task', tags=['Tasks']),
    destroy=extend_schema(description='Delete a task', tags=['Tasks']),
)
class TaskViewSet(viewsets.ModelViewSet):
    """CRUD operations for Task"""
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]
    
    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


@extend_schema_view(
    list=extend_schema(description='List all projects', tags=['Projects']),
    retrieve=extend_schema(description='Get a specific project', tags=['Projects']),
    create=extend_schema(description='Create a new project', tags=['Projects']),
    update=extend_schema(description='Update a project', tags=['Projects']),
    partial_update=extend_schema(description='Partially update a project', tags=['Projects']),
    destroy=extend_schema(description='Delete a project', tags=['Projects']),
)
class ProjectViewSet(viewsets.ModelViewSet):
    """CRUD operations for Project"""
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


@extend_schema(
    request=LoginSerializer,
    responses={
        200: {
            'type': 'object',
            'properties': {
                'refresh': {'type': 'string'},
                'access': {'type': 'string'},
                'user': {
                    'type': 'object',
                    'properties': {
                        'id': {'type': 'integer'},
                        'username': {'type': 'string'},
                        'email': {'type': 'string'},
                        'role': {'type': 'string'}
                    }
                }
            }
        }
    },
    description='Login with email and password to receive JWT tokens',
    tags=['Authentication']
)
@api_view(['POST'])
@permission_classes([AllowAny])
def login(request):
    """Login user and return JWT tokens"""
    serializer = LoginSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.validated_data['user']
        refresh = RefreshToken.for_user(user)
        
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            'user': UserSerializer(user).data
        }, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@extend_schema(
    request=UserCreateSerializer,
    responses={201: UserCreateSerializer},
    description='Register a new user account',
    tags=['Authentication']
)
@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
    """Register a new user"""
    serializer = UserCreateSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

