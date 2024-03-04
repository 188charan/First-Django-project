# Register your models here.
from django.contrib import admin
from myapp.models import Users
from myapp.models import Donation
from myapp.models import Order

admin.site.register(Donation)
admin.site.register(Users)
admin.site.register(Order)
