from django.core import serializers
from django.shortcuts import render
from django.http import HttpResponseBadRequest, JsonResponse
import random
from django.contrib.auth.decorators import login_required
import json

import random


def generate_math_question(operation):
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
        return json.dumps({"error": "Invalid operation. Please choose from 'multiplication', 'addition', 'subtraction', or 'division'."})

    return json.dumps({"question": question, "answer": answer})


@login_required
def index(request):
    type = request.GET.get('type', 'noType')
    if type != 'noType':
        question = generate_math_question(type)
        return render(request, 'eduprod/index.html', {
            "questionData": question
        })
    else:
        return render(request, 'eduprod/index.html')