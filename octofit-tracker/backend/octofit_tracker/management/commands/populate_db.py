from django.core.management.base import BaseCommand
from django.conf import settings
from pymongo import MongoClient
from datetime import timedelta
from bson import ObjectId
from ...models import User, Team, Activity, Leaderboard, Workout
from ...test_data import test_users, test_teams, test_activities, test_leaderboard, test_workouts

class Command(BaseCommand):
    help = 'Populate the database with test data for users, teams, activities, leaderboard, and workouts'

    def handle(self, *args, **kwargs):
        # Connect to MongoDB
        client = MongoClient(settings.DATABASES['default']['HOST'], settings.DATABASES['default']['PORT'])
        db = client[settings.DATABASES['default']['NAME']]

        # Drop existing collections
        db.users.drop()
        db.teams.drop()
        db.activity.drop()
        db.leaderboard.drop()
        db.workouts.drop()

        # Populate users
        users = []
        for user_data in test_users:
            user = User(_id=ObjectId(), **user_data)
            user.save()
            users.append(user)

        # Populate teams
        for team_data in test_teams:
            team = Team(_id=ObjectId(), **team_data)
            team.save()
            team.members.add(*users)

        # Populate activities
        for activity_data in test_activities:
            user = User.objects.get(username=activity_data.pop('username'))
            activity = Activity(_id=ObjectId(), user=user, **activity_data)
            activity.save()

        # Populate leaderboard
        for leaderboard_data in test_leaderboard:
            user = User.objects.get(username=leaderboard_data.pop('username'))
            leaderboard_entry = Leaderboard(_id=ObjectId(), user=user, **leaderboard_data)
            leaderboard_entry.save()

        # Populate workouts
        for workout_data in test_workouts:
            workout = Workout(_id=ObjectId(), **workout_data)
            workout.save()

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data.'))
