from django.core.management.base import BaseCommand

from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
import uuid

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Clear existing data in correct order
        Activity.objects.filter().delete()
        Leaderboard.objects.filter().delete()
        Workout.objects.filter().delete()
        User.objects.filter().delete()
        Team.objects.filter().delete()

        # Create teams

        marvel = Team.objects.create(id=str(uuid.uuid4()), name='Marvel')
        dc = Team.objects.create(id=str(uuid.uuid4()), name='DC')

        # Create users
        users = [
            User.objects.create(id=str(uuid.uuid4()), name='Spider-Man', email='spiderman@marvel.com', team=marvel),
            User.objects.create(id=str(uuid.uuid4()), name='Iron Man', email='ironman@marvel.com', team=marvel),
            User.objects.create(id=str(uuid.uuid4()), name='Wonder Woman', email='wonderwoman@dc.com', team=dc),
            User.objects.create(id=str(uuid.uuid4()), name='Batman', email='batman@dc.com', team=dc),
        ]

        # Create activities
        Activity.objects.create(id=str(uuid.uuid4()), user=users[0], type='Running', duration=30, date='2025-12-01')
        Activity.objects.create(id=str(uuid.uuid4()), user=users[1], type='Cycling', duration=45, date='2025-12-02')
        Activity.objects.create(id=str(uuid.uuid4()), user=users[2], type='Swimming', duration=60, date='2025-12-03')
        Activity.objects.create(id=str(uuid.uuid4()), user=users[3], type='Yoga', duration=50, date='2025-12-04')

        # Create workouts
        Workout.objects.create(id=str(uuid.uuid4()), name='Hero HIIT', description='High intensity for heroes', suggested_for='Marvel')
        Workout.objects.create(id=str(uuid.uuid4()), name='Gotham Strength', description='Strength training for Gotham defenders', suggested_for='DC')

        # Create leaderboard
        Leaderboard.objects.create(id=str(uuid.uuid4()), team=marvel, points=100)
        Leaderboard.objects.create(id=str(uuid.uuid4()), team=dc, points=90)

        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data!'))
