from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response


# UI 설정부분
from accountapp.models import NewModel
from accountapp.serializers import NewModelSerializer


def hello_world_template(request):
    return render(request, 'accountapp/hello_world.html')


# 로직 처리 부분
@api_view(['GET','POST'])
def hello_world(request):

    if request.method == "POST":
        input_data = request.data.get('input_data')

        new_model = NewModel()
        new_model.text = input_data
        new_model.save()

        # Serialize 하는 부분
        serializer = NewModelSerializer(new_model)

        return Response(serializer.data)

    return Response({"new_model":"Return Text"})