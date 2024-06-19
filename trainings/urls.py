from django.urls import path
from .views import (ExerciseListView, ExerciseCreateView, ExerciseDeleteView, WorkoutListView, WorkoutCreateView,
                    WorkoutDeleteView)


urlpatterns = [
    path('exercises/', ExerciseListView.as_view(), name='exercise_list'),
    path('exercises/new/', ExerciseCreateView.as_view(), name='exercise_create'),
    path('exercises/delete/<int:pk>/', ExerciseDeleteView.as_view(), name='exercise_delete'),
    path('workouts/', WorkoutListView.as_view(), name='workout_list'),
    path('workouts/new/', WorkoutCreateView.as_view(), name='workout_create'),
    path('workouts/delete/<int:pk>/', WorkoutDeleteView.as_view(), name='workout_delete'),
]
