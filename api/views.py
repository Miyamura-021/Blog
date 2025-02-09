from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .serializers import ContactModelSerializer
# Create your views here.
class ContactListAPIView(ListAPIView):
    queryset = Contact.object.all()
    serializer_class = ContactModelSerializer 