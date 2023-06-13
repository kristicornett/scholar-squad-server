from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from scholarsquadapi.models import Classroom

class ClassroomView(ViewSet):
    
    def list(self, request):
        school_id = request.query_params.get("school_id")
        if (school_id is not None):
            schoolClass = Classroom.objects.filter(school=school_id)
        else:
            schoolClass = Classroom.objects.all()

        serialized = ClassroomSerializer(schoolClass, many=True)
        return Response(serialized.data, status=status.HTTP_200_OK)
    
    def retrieve(self, request, pk=None):
        try:
            schoolClass = Classroom.objects.get(pk=pk)
            serializer = ClassroomSerializer(schoolClass)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Classroom.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
        


class ClassroomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classroom
        fields = ('id', 'name', 'school', 'teacher')
