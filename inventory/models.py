from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=100)
    total_stock = models.IntegerField()

    def __str__(self):
        return self.name


class Allocation(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    barangay = models.CharField(max_length=100)
    allocated_quantity = models.IntegerField()
    distributed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.barangay} - {self.item.name}"


class DistributionHistory(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    barangay = models.CharField(max_length=100)
    quantity = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)
