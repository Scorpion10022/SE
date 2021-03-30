from django.db import models


class Data(models.Model):
    index = models.AutoField(primary_key=True)
    gender = models.CharField(max_length=10)
    exercise = models.CharField(max_length=10)
    endurance_or_strength = models.CharField(max_length=10)
    body_part = models.CharField(max_length=10)
    problems = models.CharField(max_length=10)
    exercise_name = models.CharField(max_length=25, default=None)
    description = models.CharField(max_length=500, default=None)

    def __str__(self):
        return self.exercise_name


class Option(models.Model):
    gender = models.CharField(max_length=10)
    exercise = models.CharField(max_length=10)
    endurance_or_strength = models.CharField(max_length=10)
    body_part = models.CharField(max_length=10)
    problems = models.CharField(max_length=10)


gender_choices = [('Male', 'Male'), ('Female', 'Female')]
exercise_choices = [('Yes', 'Yes'), ('No', 'No')]
endurance_or_strength_choices = [('Endurance', 'Endurance'), ('Strength', 'Strength')]
body_part_choice = [('Upper', 'Upper'), ('Lower', 'Lower'), ('Core', 'Core')]

class Option2(models.Model):
    gender = models.CharField(max_length=10, choices=gender_choices)
    exercise = models.CharField(max_length=10, choices=exercise_choices)
    endurance_or_strength = models.CharField(max_length=10, choices=endurance_or_strength_choices)
    body_part = models.CharField(max_length=10, choices=body_part_choice)
    problems = models.CharField(max_length=10, choices=exercise_choices)
