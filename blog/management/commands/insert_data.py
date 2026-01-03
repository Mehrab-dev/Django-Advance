from django.core.management.base import BaseCommand
from faker import Faker
from accounts.models import User , Profile
from blog.models import Post , Category
import random
from datetime import datetime


category_list = [
        'it',
        'fun',
        'software',
        'sport'
    ]

class Command(BaseCommand) :
    help = 'inserting fake data'

    

    def __init__(self,*args,**kwargs):
        super(Command,self).__init__(*args,**kwargs)
        self.fake = Faker()

    def handle(self, *args, **options):
        user = User.objects.create_user(email=self.fake.email(),password='Mm20399990')
        profile = Profile.objects.get(user=user)
        profile.first_name = self.fake.first_name()
        profile.last_name = self.fake.last_name()
        profile.description = self.fake.paragraph(nb_sentences=5)
        profile.save()

        for name in category_list :
            Category.objects.get_or_create(name=name)

        for _ in range(5) :
            Post.objects.create(
                author = profile,
                title = self.fake.paragraph(nb_sentences=1),
                category = Category.objects.get(name=random.choice(category_list)),
                content = self.fake.paragraph(nb_sentences=7),
                status = random.choice([True,False]),
                published_date = datetime.now()
            )