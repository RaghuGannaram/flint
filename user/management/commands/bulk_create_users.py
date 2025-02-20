"""
    user/management/commands/bulk_create_users.py
    Command to generate and insert bulk Silicon Valley users into the database
"""

import os
import shutil
from django.core.management.base import BaseCommand
from django.contrib.auth.hashers import make_password
from django.conf import settings
from user.models import User

LOCAL_AVATAR_FOLDER = r"C:\Users\Raghu Gannaram\Desktop\silicon_valley"
MEDIA_FOLDER = os.path.join(settings.MEDIA_ROOT, "avatars")

os.makedirs(MEDIA_FOLDER, exist_ok=True)


class Command(BaseCommand):
    """Command class"""

    help = "Bulk create Silicon Valley users with avatars"

    def handle(self, *args, **kwargs):  # pylint: disable=unused-argument
        users_data = [
            {
                "username": "richard",
                "first_name": "Richard",
                "last_name": "Hendricks",
                "email": "richard@piedpiper.com",
                "bio": "💾 CEO of Pied Piper | Compression is everything! 📉",
                "password": "richard@1234",
                "avatar": "richard.avif",
            },
            {
                "username": "erlich",
                "first_name": "Erlich",
                "last_name": "Bachman",
                "email": "erlich@aviato.com",
                "bio": "🚀 Founder of Aviato | Tech Visionary 🌟",
                "password": "erlich@1234",
                "avatar": "erlich.avif",
            },
            {
                "username": "dinesh",
                "first_name": "Dinesh",
                "last_name": "Chugtai",
                "email": "dinesh@piedpiper.com",
                "bio": "🖥️ Python + GPUs = ❤️ | Superior coder 🏆",
                "password": "dinesh@1234",
                "avatar": "dinesh.avif",
            },
            {
                "username": "gilfoyle",
                "first_name": "Bertram",
                "last_name": "Gilfoyle",
                "email": "gilfoyle@piedpiper.com",
                "bio": "⛧ Satanist | Cybersecurity & Crypto 👹",
                "password": "gilfoyle@1234",
                "avatar": "gilfoyle.avif",
            },
            {
                "username": "jared",
                "first_name": "Donald",
                "last_name": "Dunn",
                "email": "jared@piedpiper.com",
                "bio": "📊 Operations & Strategy | I make things work smoothly 🏗️",
                "password": "jared@1234",
                "avatar": "jared.avif",
            },
            {
                "username": "gavin",
                "first_name": "Gavin",
                "last_name": "Belson",
                "email": "gavin@hooli.com",
                "bio": "🤖 AI, Tech & World Domination 🌎",
                "password": "gavin@1234",
                "avatar": "gavin.avif",
            },
            {
                "username": "russ",
                "first_name": "Russ",
                "last_name": "Hanneman",
                "email": "russ@billionaire.com",
                "bio": "💰 I put radio on the internet 📡",
                "password": "russ@1234",
                "avatar": "russ.avif",
            },
            {
                "username": "monica",
                "first_name": "Monica",
                "last_name": "Hall",
                "email": "monica@raviga.com",
                "bio": "💼 Tech Investor | Raviga Capital",
                "password": "monica@1234",
                "avatar": "monica.avif",
            },
            {
                "username": "laurie",
                "first_name": "Laurie",
                "last_name": "Bream",
                "email": "laurie@raviga.com",
                "bio": "📈 Efficiency drives investment decisions",
                "password": "laurie@1234",
                "avatar": "laurie.avif",
            },
            {
                "username": "bighead",
                "first_name": "Nelson",
                "last_name": "Bighetti",
                "email": "bighead@hooli.com",
                "bio": "🤷 I don't know what I'm doing...",
                "password": "bighead@1234",
                "avatar": "bighead.avif",
            },
            {
                "username": "peter",
                "first_name": "Peter",
                "last_name": "Gregory",
                "email": "peter@raviga.com",
                "bio": "💡 Only invest in the inevitable",
                "password": "peter@1234",
                "avatar": "peter.avif",
            },
            {
                "username": "ron",
                "first_name": "Ron",
                "last_name": "LaFlamme",
                "email": "ron@piedpiper.com",
                "bio": "⚖️ Chillest lawyer in tech. I bill you, but I'm on your side. 🍃",
                "password": "dan@1234",
                "avatar": "ron.avif",
            },
            {
                "username": "carla",
                "first_name": "Carla",
                "last_name": "Walton",
                "email": "carla@bighetti.com",
                "bio": "👩‍💻 Hardware hacker | 'Fix it yourself' enthusiast | CPUs > GPUs 🚀",
                "password": "nelson@1234",
                "avatar": "carla.avif",
            },
        ]

        users_to_create = []
        for data in users_data:
            users_to_create.append(
                User(
                    username=data["username"],
                    first_name=data["first_name"],
                    last_name=data["last_name"],
                    email=data["email"],
                    bio=data["bio"],
                    password=make_password(data["password"]),
                )
            )

        # Bulk create users
        created_users = User.objects.bulk_create(users_to_create)

        # Assign avatars separately
        for user, data in zip(created_users, users_data):
            local_path = os.path.join(LOCAL_AVATAR_FOLDER, data["avatar"])
            new_avatar_path = os.path.join(MEDIA_FOLDER, f"{user.username}.jpg")

            if os.path.exists(local_path):
                shutil.copy(local_path, new_avatar_path)
                user.avatar = f"avatars/{user.username}.jpg"
                user.save()

        self.stdout.write(
            self.style.SUCCESS(  # pylint: disable=no-member
                "Successfully created users with avatars!"
            )
        )
