from rest_framework import viewsets
from .models import AcademicRecord, ResearchPaper
from .serializers import AcademicRecordSerializer, ResearchPaperSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.core.files.storage import FileSystemStorage

class AcademicRecordViewSet(viewsets.ModelViewSet):
    queryset = AcademicRecord.objects.all()
    serializer_class = AcademicRecordSerializer

class ResearchPaperViewSet(viewsets.ModelViewSet):
    queryset = ResearchPaper.objects.all()
    serializer_class = ResearchPaperSerializer

@api_view(['POST'])
def upload_file(request):
    if request.method == 'POST' and request.FILES['file']:
        file = request.FILES['file']
        fs = FileSystemStorage()
        filename = fs.save(file.name, file)
        # 这里可以调用 Celery 任务进行文件分析
        analyze_file.delay(filename)  # 假设 analyze_file 是之前定义的 Celery 任务
        return Response({'filename': filename}, status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST) 