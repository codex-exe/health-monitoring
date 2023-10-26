from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from health.utils import save_kb

@csrf_exempt
def create(request):
    if request.method == 'POST':
        user = request.POST.get('user')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        weight = request.POST.get('weight')
        height = request.POST.get('height')

        kb = f"""
        name({user}).
        age({user}, {age}).
        gender({user}, {gender}).
        weight({user}, {weight}).
        height({user}, {height}).
        """
        save_kb(kb, f'health/database/{user}_kb.pl')
        
        return JsonResponse({"message": f"Welcome {user}!"})
    else:
        return JsonResponse({"error": "Invalid request method"})