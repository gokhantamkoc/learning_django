from django.apps import AppConfig
from first_app.models import Topic, Webpage, AccessRecord

class FirstAppConfig(AppConfig):
    name = 'first_app'

admin.site.register(Topic)
admin.site.register(Webpage)
admin.site.register(AccessRecord)
