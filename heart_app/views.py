from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from django.core import serializers
from django.conf import settings
import json
import pickle
import numpy as np
import pandas as pd


@api_view(["POST"])
def IdealWeight(heartdata):
    try:
        data = json.load(heartdata)
        model = pickle.load(open("heart_app/heart_model.pkl","rb"))
        arr = pd.DataFrame([[data['age'],data['sex'],data['cp'],data['trestbps'],data['chol'],data['fbs'],data['restecg'],data['thalach'],data['exang'],data['oldpeak'],data['slope'],data['ca'],data['thal']]])
        mypred = model.predict(arr)[0]
        return Response(mypred)
    except ValueError as e:
        return Response(e.args[0],status.HTTP_400_BAD_REQUEST)
        