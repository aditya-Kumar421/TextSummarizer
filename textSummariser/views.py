from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings
from rest_framework.permissions import IsAuthenticated
import requests

class SummarizeTextView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        text = request.data.get('text')
        if not text:
            return Response({'error': 'No text provided'}, status=status.HTTP_400_BAD_REQUEST)
        API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
        headers = {"Authorization": f'Bearer {settings.HUGGINGFACE_API_KEY}'}
        data = {
            'inputs': text
        }
    
        response = requests.post(API_URL, headers=headers, json=data)
    
        if response.status_code == 200:
            summary = response.json()[0]['summary_text']
            return Response({'summary': summary})
        else:
            return Response({'error': 'Failed to summarize text', 'status_code': response.status_code})
