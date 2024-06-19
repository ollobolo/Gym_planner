from django import forms
from .models import Exercise, Workout


class ExerciseForm(forms.ModelForm):
    class Meta:
        model = Exercise
        fields = ['name', 'part']


class WorkoutForm(forms.ModelForm):
    exercises = forms.ModelMultipleChoiceField(
        queryset=Exercise.objects.none(),
        widget=forms.CheckboxSelectMultiple
    )

    class Meta:
        model = Workout
        fields = ['exercises']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user:
            self.fields['exercises'].queryset = Exercise.objects.filter(user=user)
