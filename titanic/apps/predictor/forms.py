from django import forms
from django.core.validators import MaxValueValidator, MinValueValidator

# choices for Sex field
PREDICTOR_FORM_SEX_CHOICES = [
    ('0', 'Male'),
    ('1', 'Female')
]


# choices for Embarked field
PREDICTOR_FORM_EMBARKED_CHOICES = [
    ('0', 'Southampton'),
    ('1', 'Cherbourg'),
    ('2', 'Queenstown')
]


# choices for Title field ('Mr', 'Miss', 'Mrs', 'Master', 'Dr', 'Rev', 'Officer', 'Royalty')
PREDICTOR_FORM_TITLE_CHOICES = [
    ('0', 'Mr.'),
    ('1', 'Miss',),
    ('2', 'Mrs.'),
    ('3', 'Master'),
    ('4', 'Doctor'),
    ('5', 'Reverend'),
    ('6', 'Officer'),
    ('7', 'Royalty'),
]


# pclass, sex, age, sibsp (number of siblings or spouse), parch (number of parents or children), fare, embarked, title
class PredictorForm(forms.Form):
    pclass = forms.IntegerField(min_value=1, max_value=3)
    sex = forms.ChoiceField(choices=PREDICTOR_FORM_SEX_CHOICES)
    age = forms.IntegerField(max_value=80, min_value=1)
    sibsp = forms.IntegerField(max_value=15, min_value=0)
    parch = forms.IntegerField(max_value=15, min_value=0)
    fare = forms.IntegerField(max_value=1000, min_value=0)
    embarked = forms.ChoiceField(choices=PREDICTOR_FORM_EMBARKED_CHOICES)
    title = forms.ChoiceField(choices=PREDICTOR_FORM_TITLE_CHOICES)

    def __repr__(self):
        return f'{self.pclass} {self.sex} {self.age} {self.sibsp} {self.parch} {self.fare} {self.embarked} {self.title}'