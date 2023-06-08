from django.http import JsonResponse
from dotenv import dotenv_values
from dotenv import load_dotenv
import os
from openai import ChatCompletion
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response

load_dotenv()
dotenv_values()
openai_api_key = os.getenv("OPENAI_API_KEY")

class ScholarAI(ViewSet):
    def create(self, request):
        user_input = request.data.get('user_input')

        completion = ChatCompletion.create(
            api_key=openai_api_key,
            model="gpt-3.5-turbo", temperature= 0.8,
            messages=[
                {
                    "role": "system",
                    "content": "You are a high school English teacher. The only thing you return are quiz questions you create"
                                "You have a brilliant vocabulary and are considered the best because you reference the input from other teachers"
                                "You analyze the input from your users to better understand what they are wanting" 
                                "You are an excellent linguist and have an exceptional vocabulary"
                                "You enjoy making tests to help prepare students have a wide and varied vocabulary"
                },
                {
                    "role": "user",
                    "content": user_input
                }
            ]
        )

        response = completion.choices[0].message.content

        return Response({'response': response})