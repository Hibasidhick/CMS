from django.db import models
from CMS_App.models import Appointment,Doctor,Patient,LabTest
# Create your models here.

class Consultation(models.Model):
    consultation_id = models.AutoField(primary_key=True)
    appointment = models.ForeignKey('CMS_App.Appointment', on_delete=models.CASCADE)
    appointment = models.ForeignKey('CMS_App.Appointment', on_delete=models.CASCADE)
    patient = models.ForeignKey('CMS_App.Patient', on_delete=models.CASCADE)
    symptoms = models.TextField()  # What the patient reports
    diagnosis = models.TextField()  # Doctor's diagnosis
    treatment = models.TextField()  # Recommended treatment
    notes = models.TextField(blank=True)  # Additional notes
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Consultation #{self.consultation_id} - {self.patient.full_name}"
    
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

    def __str__(self):
        return f"LabTestPrescription #{self.prescription_id} - {self.patient.full_name}"