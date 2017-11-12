import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "model_template_and_view_paradigm.settings")

import django
django.setup()

import random
from first_app.models import Webpage, Topic, AccessRecord
from faker import Faker

fakegen = Faker()
topics = ['Search', 'Social', 'Marketplace', 'News', 'Games']

def add_topic():
    t = Topic.objects.get_or_create(name=random.choice(topics))[0]
    t.save()
    return t

def populate(max_insertions=5):
    for item in range(max_insertions):

        # create the topic entry
        topic = add_topic()

        # create fake data
        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()

        # create fake webpage entry
        webpage = Webpage.objects.get_or_create(topic = topic, url = fake_url, name = fake_name)[0]

        # create fake access record entry
        access_record = AccessRecord.objects.get_or_create(webpage=webpage, date=fake_date)[0]

if __name__ == '__main__':
    print('Adding initial data to database!')
    populate(10)
    print('Finished!')
