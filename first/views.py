from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse, Http404
from .models import FileModel
import os
from .serializers import FileSerializer, MultipleFileSerializer
from django.conf import settings
from .utils import results



class FileViewSet(viewsets.ModelViewSet):
    queryset = FileModel.objects.all()
    serializer_class = FileSerializer

    @action(detail=False, methods=["POST"])
    def multiple_upload(self, request, *args, **kwargs):
        """Upload multiple files and create objects."""
        serializer = MultipleFileSerializer(data=request.data or None)
        serializer.is_valid(raise_exception=True)
        files = serializer.validated_data.get("files")

        files_list = []
        for file in files:
            files_list.append(
                FileModel(file=file)
            )
        if files_list:
            FileModel.objects.bulk_create(files_list)

        return Response("Success")

# WITHOUT DRF UPLOADS

def single_upload(request):
    file = request.FILES.get("file")
    FileModel.objects.create(file=file)
    return JsonResponse({"message": "Success"})


def multiple_upload(request):
    files = request.FILES.getlist("files")

    files_list = []
    for file in files:
        files_list.append(FileModel(file=file))

    if files_list:
        FileModel.objects.bulk_create(files_list)

    results()
    return JsonResponse({"message": "Success"})


def index(request):
    return render(template_name="index.html", request=request)

def home(request):
    context = {'file': FileModel.objects.all()}
    return render(request, 'home.html', context)

def download(request, path):
    file_path = os.path.join(settings.MEDIA_ROOT, path)

    if os.path.exist(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/file")
            response['Content-Disposition'] = 'inline;filename=' + os.path.basename(file_path)
            return response
    raise Http404

