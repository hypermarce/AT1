from django.core import serializers
from django.shortcuts import render
from django.http import HttpResponseBadRequest, JsonResponse
import random
from django.contrib.auth.decorators import login_required
import json

import random
# Function to generate a math question based on the provided operation

def generate_math_question(operation):
    # Generate random numbers for the operation
    if operation == "multiplication":
        num1 = random.randint(1, 12)
        num2 = random.randint(1, 12)
        question = f"{num1} x {num2}?"
        answer = num1 * num2
    elif operation == "addition":
        num1 = random.randint(1, 50)
        num2 = random.randint(1, 50)
        question = f"{num1} + {num2}?"
        answer = num1 + num2
    elif operation == "subtraction":
        num1 = random.randint(1, 50)
        num2 = random.randint(1, 50)
        # Ensure num1 is greater than or equal to num2
        num1, num2 = max(num1, num2), min(num1, num2)
        question = f"{num1} - {num2}?"
        answer = num1 - num2
    elif operation == "division":
        # Ensure a simple division with no remainders
        divisor = random.randint(1, 12)
        quotient = random.randint(1, 12)
        dividend = divisor * quotient
        question = f"{dividend} ÷ {divisor}?"
        answer = quotient
    else:
        # Return an error for invalid operation
        return json.dumps({"error": "Invalid operation. Please choose from 'multiplication', 'addition', 'subtraction', or 'division'."})

    # Return the generated question and answer
    return json.dumps({"question": question, "answer": answer})


@login_required
def index(request):
    # Get the type of math operation from the request query parameter
    type = request.GET.get('type', 'noType')
    if type != 'noType':
        # Generate a math question based on the provided type
        question = generate_math_question(type)
        return render(request, 'eduprod/index.html', {
            "questionData": question
        })
    else:
        # Render the index page without a question if no type is provided
        return render(request, 'eduprod/index.html')