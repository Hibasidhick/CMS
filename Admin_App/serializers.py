# serializers.py

from rest_framework import serializers
from django.contrib.auth.models import User
from CMS_App.models import Doctor, Receptionist, LabTechnician, Pharmacist, Department

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']

# Department
class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'

# Doctor
class DoctorSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Doctor
        fields = '__all__'

# Receptionist
class ReceptionistSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Receptionist
        fields = '__all__'

# Lab Technician
class LabTechnicianSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = LabTechnician
        fields = '__all__'

# Pharmacist
class PharmacistSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Pharmacist
        fields = '__all__'
