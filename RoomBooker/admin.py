from django.contrib import admin
from .models import User, Organisation, Room, Booking

models = [User, Organisation, Room, Booking]

for model in models:
    admin.site.register(model)
