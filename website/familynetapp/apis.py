from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.response import Response

from familynetapp.models import Person, Relation
from familynetapp.serializers import PersonSerializer, RelationSerializer


@api_view(['GET', 'POST'])
def person_list(request, format=None):
    if request.method == 'GET':
        return Response(PersonSerializer(Person.objects.all(), many=True).data)
    elif request.method == 'POST':
        serializer = PersonSerializer(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def person_detail(request, pk, format=None):
    try:
        person = Person.objects.get(pk=pk)
    except Person.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        return Response(PersonSerializer(person).data)
    elif request.method == 'PUT':
        serializer = PersonSerializer(person, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        person.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def relation_list(request, format=None):
    if request.method == 'GET':
        return Response(RelationSerializer(Relation.objects.all(), many=True).data)
    elif request.method == 'POST':
        serializer = RelationSerializer(request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def relation_detail(request, pk, format=None):
    try:
        relation = Relation.objects.get(pk=pk)
    except Relation.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        return Response(RelationSerializer(relation).data)
    elif request.method == 'PUT':
        serializer = RelationSerializer(relation, data=JSONParser().parse(request))
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        relation.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
