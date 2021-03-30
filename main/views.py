from django.shortcuts import render
from .models import Option, Data
from .forms import ChoiceForm


def index(request):
    options = Option.objects.all()

    if request.method == 'POST':
        form = ChoiceForm(request.POST)
        if form.is_valid():
            gender = form.cleaned_data['gender']
            exercise = form.cleaned_data['exercise']
            endurance_or_strength = form.cleaned_data['endurance_or_strength']
            body_part = form.cleaned_data['body_part']
            problems = form.cleaned_data['problems']
            context = {'result': Data.objects.all(), 'r1': gender, 'r2': exercise,
                       'r3': endurance_or_strength, 'r4': body_part, 'r5': problems}
            return render(request, 'main/result.html', context)
    else:
        form = ChoiceForm()

    context = {'options': options, 'form': form}

    return render(request, 'main/index.html', context)


def result(request, r1, r2, r3, r4, r5):
    result = Data.objects.all()
    context = {'result': result, 'r1': r1, 'r2': r2, 'r3': r3, 'r4': r4, 'r5': r5}
    return render(request, 'main/result.html', context)
