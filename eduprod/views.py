from django.core import serializers
from django.shortcuts import render
from django.http import HttpResponseBadRequest, JsonResponse
import random
from django.contrib.auth.decorators import login_required
import json

@login_required
def index(request):
    type = request.GET.get('type', 'noType')
    if type != 'noType':
        print(type)

    return render(request, 'eduprod/index.html')

'''
    # Get the first and last question ID
    first_id = Question.objects.order_by('id').first().id
    last_id = Question.objects.order_by('id').last().id

    # Initialize an array to store unique question IDs
    random_ids = []

    # Generate 5 unique random question IDs
    while len(random_ids) < 5:
        random_id = random.randint(first_id, last_id)
        # Check if the random ID matches an existing question ID and is not already in the array
        if Question.objects.filter(id=random_id).exists() and random_id not in random_ids:
            random_ids.append(random_id)

    # Retrieve the questions matching the random IDs
    questions = Question.objects.filter(id__in=random_ids)

    # Serialize the questions to JSON
    questions_json = serializers.serialize('json', questions)

    # Get distinct categories for all questions
    categories = Question.objects.values_list('category', flat=True).distinct()
'''
