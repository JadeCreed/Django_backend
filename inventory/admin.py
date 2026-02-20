from django.contrib import admin
from .models import Item, Allocation, DistributionHistory

admin.site.register(Item)
admin.site.register(Allocation)
admin.site.register(DistributionHistory)
