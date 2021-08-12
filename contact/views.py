from django.shortcuts import render
from rest_framework.decorators import api_view, parser_classes
from rest_framework.response import Response
from .serializers import *
from rest_framework import status
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from .models import Contact


@swagger_auto_schema(
    method='put',
    request_body=ContactSerializer,
    responses={404: 'data not found', 200: 'trash is empty'},
    operation_description="Creationg of contact for a particular user"
)
@api_view(['PUT'])
def createContact(request):
    context = ContactSerializer(data=request.data)
    if(context.is_valid()):
        context.save()
        return Response({'message': "Contact created"}, status=status.HTTP_201_CREATED)
    return Response(context.errors, status=status.HTTP_400_BAD_REQUEST)




@swagger_auto_schema(
    method='put',
    request_body=ContactSerializer,
    responses={404: 'data not found', 200: 'trash is empty'},
    operation_description="Update of contact for a particular user"
)
@api_view(['PUT'])
def updateContact(request):
    request_data = request.data.copy()  # deep copy deep copy is mutable
    data_to_update = {}
    for param in request_data:
        data_to_update[i] = request_data[param]
    contact_id = request_data['contact_id'] #return id and pop it off
    context = Todo.objects.filter(contact_id=contact_id).update(**data_to_update)


@swagger_auto_schema(
    method='put',
    request_body=ContactSerializer,
    responses={404: 'data not found', 200: 'trash is empty'},
    operation_description="Soft delete of contact"
)
@api_view(['PUT'])
def trashContact(request):
    request_data = request.data.copy()  # deep copy deep copy is mutable
    user_id = request_data['contact_id'] #return id and pop it off
    Contact.objects.all().filter(user=user_id).update(is_trashed=True)
    return Response({'message': "Contact archived"}, status=status.HTTP_201_CREATED)



@swagger_auto_schema(
    method='delete',
    request_body=ContactSerializer,
    responses={404: 'data not found', 200: 'trash is empty'},
    operation_description="deletion of contact for"
)
@api_view(['DELETE'])
def emptyContactTrash(request):
    request_data = request.data.copy()  # deep copy deep copy is mutable
    user_id = request_data['user_id'] #return id and pop it off
    Contact.objects.all().filter(is_trashed=True, user=user_id).delete()
    return Response({'message': "Contact archived"}, status=status.HTTP_201_CREATED)




@swagger_auto_schema(
    method='get',
    responses={404: 'data not found', 200: 'trash is empty'},
    operation_description="get contacts for a particular user"
)
@api_view(['GET'])
def getUserContact(request):
    # convert the string to int request_data is immutable
    request_data = request.data.copy()  # deep copy deep copy is mutable
    user_id = request_data['user_id'] #return id and pop it off
    query = Contact.objects.all().filter(user=int(user_id))
    context =ContactSerializer(query, many=True)
    return Response({'data': context.data, 'message': "All users gotten"}, status=status.HTTP_201_CREATED)





@swagger_auto_schema(
    method='put',
    request_body=ContactSerializer,
    responses={404: 'data not found', 200: 'trash is empty'},
    operation_description="Archive of contact"
)
@api_view(['PUT'])
def archiveContact(request):
        # convert the string to int request_data is immutable
    request_data = request.data.copy()  # deep copy deep copy is mutable
    contact_id = request_data['contact_id'] #return id and pop it off
    context = Contact.objects.filter(contact_id=contact_id).update(is_archived = True)
    return Response({'message': "Contact archived"}, status=status.HTTP_201_CREATED)
# Create your views here.
