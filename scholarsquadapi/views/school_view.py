from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from scholarsquadapi.models import School
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny


class SchoolView(ViewSet):
    """ScholarSquad school view"""
    
    def list(self, request):
        """Handles GET requests for schools"""

        schools = School.objects.all()
        serialized = SchoolSerializer(schools, many=True)
        return Response(serialized.data, status=status.HTTP_200_OK)
    
    def retrieve(self, request, pk=None):
        """Handles GET for a single school"""

        try:
            school = School.objects.get(pk=pk)
            serializer = SchoolSerializer(school)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except School.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def create(self, request):
        """Handles Post"""

        school = School.objects.get(user=request.auth.user)
        serializer = CreateSchoolSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(school=school)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def update(self, request, pk):
        """Handles PUT request for school"""
        school = School.objects.get(pk=pk)
        school.name = request.data["name"]
        school.save()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
    def destroy(self, request, pk):
        school = School.objects.get(pk=pk)
        school.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = ('id', 'name')

class CreateSchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = ['id', 'name']

