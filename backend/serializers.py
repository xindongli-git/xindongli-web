from rest_framework import serializers
from .models import AcademicRecord, ResearchPaper

class AcademicRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = AcademicRecord
        fields = '__all__'

class ResearchPaperSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResearchPaper
        fields = '__all__' 