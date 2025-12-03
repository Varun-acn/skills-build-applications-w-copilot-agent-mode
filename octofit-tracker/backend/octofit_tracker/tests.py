from django.test import TestCase
from .models import User, Team, Activity, Leaderboard, Workout

class ModelTests(TestCase):
    def test_team_creation(self):
        team = Team.objects.create(id='t1', name='Test Team')
        self.assertEqual(team.name, 'Test Team')

    def test_user_creation(self):
        team = Team.objects.create(id='t2', name='Test Team')
        user = User.objects.create(id='u1', name='Test User', email='test@example.com', team=team)
        self.assertEqual(user.email, 'test@example.com')

    def test_activity_creation(self):
        team = Team.objects.create(id='t3', name='Test Team')
        user = User.objects.create(id='u2', name='Test User', email='test2@example.com', team=team)
        activity = Activity.objects.create(id='a1', user=user, type='Running', duration=30, date='2025-12-01')
        self.assertEqual(activity.type, 'Running')

    def test_workout_creation(self):
        workout = Workout.objects.create(id='w1', name='Test Workout', description='Desc', suggested_for='Test')
        self.assertEqual(workout.name, 'Test Workout')

    def test_leaderboard_creation(self):
        team = Team.objects.create(id='t4', name='Test Team')
        leaderboard = Leaderboard.objects.create(id='l1', team=team, points=50)
        self.assertEqual(leaderboard.points, 50)
