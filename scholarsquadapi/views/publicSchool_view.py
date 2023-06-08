from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from scholarsquadapi.models import School
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny


    

@api_view(['GET'])
@permission_classes([AllowAny])
    
def getAllSchools(request):
        """Handles GET requests for schools"""

        schools = School.objects.all()
        serialized = SchoolSerializer(schools, many=True)
        return Response(serialized.data, status=status.HTTP_200_OK)

class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = ('id', 'name')