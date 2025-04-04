<<<<<<< HEAD
=======
from django.db import models
from CMS_App.models import Medicine
from django.core.validators import MinValueValidator

# Create your models here.

# ✅ Medicine Stock Model
class MedicineStock(models.Model):
    stock_id = models.AutoField(primary_key=True)
    medicine = models.OneToOneField('CMS_App.Medicine', on_delete=models.CASCADE, related_name="stock")
    quantity = models.PositiveIntegerField(default=0, validators=[MinValueValidator(0)])
    restock_threshold = models.PositiveIntegerField(default=10, help_text="Minimum stock before restock alert")
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.medicine.medicine_name} - {self.quantity} units"

    def save(self, *args, **kwargs):
        """Automatically update medicine availability based on stock quantity."""
        self.medicine.stock_quantity = self.quantity
        self.medicine.save()
        super().save(*args, **kwargs)
>>>>>>> a448412acc0820a43bc3ddd79cc947af4045fe38
