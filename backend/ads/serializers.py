from rest_framework import serializers
from .models import Ad, Category, AdImage





class AdImageSerializer(serializers.ModelSerializer):
  class Meta:
    model = AdImage
    fields = ['id', 'image']

class AdSerializer(serializers.ModelSerializer):
  images = AdImageSerializer(many=True, read_only=True)
  image_files = serializers.ListField(child=serializers.ImageField(max_length=100000, allow_empty_file=False, use_url=False), write_only=True, required=True)

  class Meta:
    model = Ad
    fields = ['id', 'title', 'description', 'price', 'category', 'author', 'created_at', 'images', 'image_files']

  def create(self, validated_data):
    image_files = validated_data.pop('image_files', [])
    ad = Ad.objects.create(**validated_data)
    for image in image_files:
      AdImage.objects.create(ad=ad, image=image)
      
      return ad