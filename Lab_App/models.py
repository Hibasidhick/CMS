from django.db import models

# Create your models here.
from django.db import models

class LabTestPrescription(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]
    
    prescription_id = models.AutoField(primary_key=True)
    doctor = models.ForeignKey('CMS_App.Doctor', on_delete=models.CASCADE)
    patient = models.ForeignKey('CMS_App.Patient', on_delete=models.CASCADE)
    appointment = models.ForeignKey('CMS_App.Appointment', on_delete=models.SET_NULL, null=True, blank=True)
    tests = models.ManyToManyField('CMS_App.LabTest')
    notes = models.TextField(blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return f"LabTestPrescription #{self.prescription_id} - {self.patient.full_name}"