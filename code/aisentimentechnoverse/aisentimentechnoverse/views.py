from django.shortcuts import render
from .apps import AisentimentechnoverseConfig
from django.http import JsonResponse
from rest_framework.views import APIView

class call_model(APIView):
    def get(self,request):
        if request.method == 'GET':
            text = request.GET.get("text")
            vector = AisentimentechnoverseConfig.vectorizer.transform([text])
            prediction = AisentimentechnoverseConfig.model.predict(vector)[0]
            response = {'text_sentiment':prediction}
            return JsonResponse(response)
# Create your views here.
