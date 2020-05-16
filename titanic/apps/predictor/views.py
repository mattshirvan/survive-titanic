from django.shortcuts import render, redirect, reverse

from . import predictor
from .forms import PredictorForm


# Create your views here.

def index(request):
    form = PredictorForm()
    return render(request, "predictor/index.html", {'form': form})


    
def result(request):
    """
    Sex.replace(('male', 'female'), (0, 1))
    
    Embarked.replace(('S', 'C', 'Q'), (0, 1, 2))
    
    Title.replace(('Mr', 'Miss', 'Mrs', 'Master', 'Dr', 'Rev', 'Officer', 'Royalty'), (0,1,2,3,4,5,6,7))
    
    """
    form = PredictorForm(request.POST)
    
    prediction = None

    if form.is_valid():
        pclass = int(form.cleaned_data['pclass'])
        sex = int(form.cleaned_data['pclass'])
        age = int(form.cleaned_data['age'])
        sibsp = int(form.cleaned_data['sibsp'])
        parch = int(form.cleaned_data['parch'])
        fare = int(form.cleaned_data['fare'])
        embarked = int(form.cleaned_data['embarked'])
        title = int(form.cleaned_data['title'])

        prediction = predictor.prediction_model(pclass, sex, age, sibsp, parch, fare, embarked, title)
    print(prediction)
    if prediction[0] == 0:
        html = 'result.html'
    elif prediction[0] == 1:
        html = 'result1.html'
    else:
        return redirect(reverse('predictor:index'))

    return render(request, "predictor/{}".format(html))