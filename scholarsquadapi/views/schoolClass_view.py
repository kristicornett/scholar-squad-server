from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from scholarsquadapi.models import SchoolClass

class SchoolClassView(ViewSet):
    def list(self, request):

        schoolClass = SchoolClass.objects.all()
        serialized = SchoolClassSerializer(schoolClass, many=True)
        return Response(serialized.data, status=status.HTTP_200_OK)
    
    def retrieve(self, request, pk=None):
        try:
            schoolClass = SchoolClass.objects.get(pk=pk)
            serializer = SchoolClassSerializer(schoolClass)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except SchoolClass.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
        


class SchoolClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = SchoolClass
        fields = ('id', 'name', 'school', 'teacher')
