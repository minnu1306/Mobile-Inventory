from .models import Company,Mobile
from rest_framework import serializers

class CSe(serializers.Serializer):
	id=serializers.IntegerField()
	name=serializers.CharField(max_length=100)
	hq=serializers.CharField(max_length=100)
	
	def create(self, validated_data):
		return Company.objects.create(**validated_data)

	def update(self, instance,validated_data):
		instance.name= validated_data.get('name',instance.name)
		instance.hq= validated_data.get('hq',instance.hq)
		instance.save()
		return instance 

class MSe(serializers.ModelSerializer):
	def create(self,validated_data):	
		company=Company.objects.get(id=validated_data["cId"])
		validated_data["cId"]= company
		return Mobile.objects.create(**validated_data)
	
	class Meta:
		model=Mobile
		fields=['id','cId','name','price','status']
	
	
	
