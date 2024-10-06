from django.shortcuts import render
from django.http import JsonResponse

def calculator(request):
    if request.method == 'POST':
        num1 = float(request.POST.get('num1', 0))
        num2 = float(request.POST.get('num2', 0))
        operation = request.POST.get('operation', '+')

        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            result = num1 / num2 if num2 != 0 else 'Error: Division by zero'
        else:
            result = 'Error: Invalid operation'

        return JsonResponse({'result': result})
    return render(request, 'calculator/calculator.html')