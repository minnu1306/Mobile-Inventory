from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Company,Mobile
from django.http import Http404
from rest_framework import status
from . import serializers
# Create your views here.

class CompanyL(APIView):
	def get(self,request):
		company= Company.objects.all()
		serializer=serializers.CSe(company, many= True)
		return Response(serializer.data)
		
	def post(self,request):
		serializer=serializers.CSe(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
		
class CompanyDetails(APIView):
	def get(self,request,id):
		try:
			company=Company.objects.get(id=id)
		except Company.DoesNotExist:
			raise Http404
		serializer=serializers.CSe(company)
		return Response(serializer.data)
		
	def put(self,request,id):
		try:
			company=Company.objects.get(id=id)
		except Company.DoesNotExist:
			raise Http404
		serializer= serializers.CSe(company,data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
		
	def delete(self,request,id):
		try:
			company=Company.objects.get(id=id)
		except Company.DoesNotExist:
			raise Http404
		company.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)
		
class MobileL(APIView):
	def get(self,request,id):
		
		mobile= Mobile.objects.filter(cId=id)
		serializer=serializers.MSe(mobile, many= True)
		return Response(serializer.data)
		
	def post(self,request,id):
		try:
			Company.objects.get(id=id)
		except Company.DoesNotExist:
			raise Http404
		serializer=serializers.MSe(data=request.data)
		if serializer.is_valid():
			serializer.save(cId=id)
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MobileDetails(APIView):
	
	def get(self, request, cId, id):
		try:
			mobile=Mobile.objects.get(cId=cId,id=id)
		except Mobile.DoesNotExist:
			raise Http404
		serializer=serializers.MSe(mobile)
		return Response(serializer.data)
		
	def put(self,request,cId,id):
		try:
			mobile=Mobile.objects.get(id=id)
		except Mobile.DoesNotExist:
			raise Http404
		serializer= serializers.MSe(mobile,data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
		
	def delete(self,request,cId,id):
		try:
			mobile=Mobile.objects.get(id=id)
		except Mobile.DoesNotExist:
			raise Http404
		mobile.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)
