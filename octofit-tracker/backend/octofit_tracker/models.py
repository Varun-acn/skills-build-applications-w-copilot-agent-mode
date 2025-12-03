from django.db import models

class Team(models.Model):
	id = models.CharField(primary_key=True, max_length=24)
	name = models.CharField(max_length=100, unique=True)
	def __str__(self):
		return self.name

class User(models.Model):
	id = models.CharField(primary_key=True, max_length=24)
	name = models.CharField(max_length=100)
	email = models.EmailField(unique=True)
	team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='members')
	def __str__(self):
		return self.name

class Activity(models.Model):
	id = models.CharField(primary_key=True, max_length=24)
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='activities')
	type = models.CharField(max_length=100)
	duration = models.IntegerField()  # minutes
	date = models.DateField()
	def __str__(self):
		return f"{self.type} - {self.user.name}"

class Workout(models.Model):
	id = models.CharField(primary_key=True, max_length=24)
	name = models.CharField(max_length=100)
	description = models.TextField()
	suggested_for = models.CharField(max_length=100)
	def __str__(self):
		return self.name

class Leaderboard(models.Model):
	id = models.CharField(primary_key=True, max_length=24)
	team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='leaderboards')
	points = models.IntegerField(default=0)
	def __str__(self):
		return f"{self.team.name} - {self.points}"