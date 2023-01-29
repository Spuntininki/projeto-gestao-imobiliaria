from django.contrib import admin


from .models import Owner, Renter, Contract, immobile
# Register your models here.

admin.site.register(Owner)
admin.site.register(Renter)
admin.site.register(Contract)
admin.site.register(immobile)