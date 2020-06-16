from django.contrib import admin
from .models import Hospital, Bed, Ventilator, Patient


admin.site.register(Ventilator)
admin.site.register(Hospital)
admin.site.register(Bed)
admin.site.register(Patient)


# Register your models here.
