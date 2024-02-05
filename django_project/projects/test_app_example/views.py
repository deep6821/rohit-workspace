from datetime import datetime
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from django.utils import timezone
from rest_framework.decorators import api_view
from .models import User


@api_view(['GET'])
def index(request):
    return HttpResponse("Hello word")


@api_view(['POST'])
def register_user(request):
    request_params = request.data
    try:
        username = str(request_params["username"])
        password = str(request_params["password"])
        email = str(request_params["email"])
        current_time = datetime.now()
        records = User.objects.filter(username=username).first()
        if records is not None:
            records.username = username
            records.password = password
            records.email = email
            records.created_at = current_time
            records.updated_at = current_time
            result = "Record is already being created for the {username}".format(username=username)

        else:
            records = User.objects.create(
                username=username,
                password=password,
                email=email,
                created_at=current_time,
                updated_at=current_time
            )
            result = "New record is created for the {username}".format(username=username)
        records.save()
        return JsonResponse({"Success_response": result})

    except KeyError as e:
        return JsonResponse({"Keyerror": str(e)})

    except Exception as e:
        return JsonResponse({"Error": str(e)})


@api_view(['GET'])
def get_user(request):
    request_params = request.GET
    response = []
    try:
        username = str(request_params["username"])
        records = User.objects.all()
        if username:
            records = User.objects.filter(username=username)

        for data in records:
            response.append({"username": data.username, "password": data.password, "email": data.email})

        return JsonResponse({"Success_message": response})

    except KeyError as e:
        return JsonResponse({"Keyerror": str(e)})

    except Exception as e:
        return JsonResponse({"Error": str(e)})

