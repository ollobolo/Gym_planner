from django.shortcuts import render
from django.views.generic import ListView, CreateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Exercise, Workout
from .forms import ExerciseForm, WorkoutForm


class ExerciseListView(LoginRequiredMixin, ListView):
    model = Exercise
    template_name = 'exercises/exercise_list.html'
    context_object_name = 'exercises'

    def get_queryset(self):
        return Exercise.objects.filter(user=self.request.user)


class ExerciseCreateView(LoginRequiredMixin, CreateView):
    model = Exercise
    form_class = ExerciseForm
    template_name = 'exercises/exercise_form.html'
    success_url = reverse_lazy('exercise_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ExerciseDeleteView(LoginRequiredMixin, DeleteView):
    model = Exercise
    template_name = 'exercises/exercise_confirm_delete.html'
    success_url = reverse_lazy('exercise_list')

    def get_queryset(self):
        return Exercise.objects.filter(user=self.request.user)


class WorkoutListView(LoginRequiredMixin, ListView):
    model = Workout
    template_name = 'workouts/workout_list.html'
    context_object_name = 'workouts'

    def get_queryset(self):
        return Workout.objects.filter(user=self.request.user)


class WorkoutCreateView(LoginRequiredMixin, CreateView):
    model = Workout
    form_class = WorkoutForm
    template_name = 'workouts/workout_form.html'
    success_url = reverse_lazy('workout_list')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class WorkoutDeleteView(LoginRequiredMixin, DeleteView):
    model = Workout
    template_name = 'workouts/workout_confirm_delete.html'
    success_url = reverse_lazy('workout_list')

    def get_queryset(self):
        return Workout.objects.filter(user=self.request.user)
