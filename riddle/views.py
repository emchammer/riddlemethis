from django.shortcuts import render

def riddle_one(request):
    return render(request, 'riddle/riddle_one.html', {})
