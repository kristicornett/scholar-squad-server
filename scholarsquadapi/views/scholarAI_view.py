from django.http import JsonResponse
from dotenv import dotenv_values
from dotenv import load_dotenv
import os
from openai import ChatCompletion
import openai
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response

load_dotenv()
dotenv_values()
openai.api_key = os.getenv("OPENAI_API_KEY")

class ScholarAI(ViewSet):
    def create(self, request):
        user_input = request.data.get('keywords')

        #{'keywords':['Believe', 'Yesterday']}

        completion = ChatCompletion.create(
        
            model="gpt-3.5-turbo", temperature= 0.8,
            messages=[
                {
                    "role": "system",
                    "content": "You are ai language model whose purpose is to write high school English teacher. The only thing you return are quiz questions you create"
                                "You analyze the input from your users to better understand what they are wanting" 
                                "You are an excellent linguist and have an exceptional vocabulary"
                                "You enjoy making tests to help prepare students have a wide and varied vocabulary"
                                "Use the keywords given by me to generate a quiz appropriate appropriate for a 9th grade student"
                                "The quiz you generate should present a sentence that contains the keyword"
                                "Put each question and answer set as an object in an array in a json object"
                                "The question should provide one question per keyword"
                                "Only create questions for keywords I provide"
                                "remove tabs, spaces, new lines from string you give me"
                                "Each sentence should have multiple choice answers and one correct answer with the given keyword"
                                "Each sentence should have four possible answers with one correct answer"
                                "Only one answer can be an option"
                                "Make the response have the correct word as an answer"
                               

                },
                {
                    "role": "user",
                    "content": str(user_input)
                },
                {
                    "role": "assistant",
                    "content": "Here is a sample json return for a quiz json block to follow: "
                                "{\"quiz\":{\"questions\":[{\"question\":\"The store had a ______ of different types of candy.\",\"answers\":[\"pilfer\",\"plethora\",\"paragon\",\"palliate\"],\"correctAnswer\":\"plethora\"},{\"question\":\"It is always best to be ________ in your relationships with others.\",\"answers\":[\"abysmal\",\"honest\",\"imperious\",\"obtuse\"],\"correctAnswer\":\"honest\"}]}}"
                }
            ]
        )

        response = str(completion.choices[0].message.content)
        print(response)
        firstBracket = response.index('{')
        lastBracket = response.rindex('}')
        jsonBlock = response[firstBracket:lastBracket+1]
        jsonBlock = jsonBlock.replace("\n", "")
        jsonBlock = jsonBlock.replace("\\", "")
        print(jsonBlock)
        return Response(jsonBlock)