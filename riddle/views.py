from django.shortcuts import render

def riddle_one(request):
    return render(request, 'riddle/riddle_one.html', {})

def riddle_two(request):
    return render(request, 'riddle/riddle_two.html', {})

def riddle_three(request):
    return render(request, 'riddle/riddle_three.html', {})

def riddle_four(request):
    return render(request, 'riddle/riddle_four.html', {})

