from rest_framework import serializers
from .models import Consultation,LabTestPrescription
from CMS_App.models import Prescription, PrescriptionMedicine, Medicine, Doctor, Patient,LabTest

class ConsultationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consultation
        fields = '__all__'
        read_only_fields = ('doctor', 'patient', 'created_at')  # These are set automatically

    def create(self, validated_data):
        # Automatically set doctor and patient from appointment
        appointment = validated_data['appointment']
        validated_data['doctor'] = appointment.doctor
        validated_data['patient'] = appointment.patient
        return super().create(validated_data)
    
'''---------------------2)-------------'''

class PrescriptionMedicineSerializer(serializers.ModelSerializer):
    medicine_name = serializers.CharField(source='medicine.medicine_name', read_only=True)
    medicine_id = serializers.IntegerField(source='medicine.medicine_id', read_only=True)
    
    class Meta:
        model = PrescriptionMedicine
        fields = ['id', 'medicine', 'medicine_id', 'medicine_name', 'number_of_days', 'dosage', 'frequency']
        extra_kwargs = {
            'medicine': {'required': True}
        }

class PrescriptionSerializer(serializers.ModelSerializer):
    medicines = PrescriptionMedicineSerializer(many=True, required=False)
    doctor_name = serializers.CharField(source='doctor.doc_name', read_only=True)
    patient_name = serializers.CharField(source='patient.full_name', read_only=True)
    patient_registration_id = serializers.CharField(source='patient.registration_id', read_only=True)

    class Meta:
        model = Prescription
        fields = [
            'prescription_id',
            'doctor',
            'doctor_name',
            'patient',
            'patient_name',
            'patient_registration_id',
            'diagnosis',
            'prescription_date',
            'medicines'
        ]
        read_only_fields = ['prescription_date']

    def create(self, validated_data):
        medicines_data = validated_data.pop('medicines', [])
        prescription = Prescription.objects.create(**validated_data)
        
        for medicine_data in medicines_data:
            PrescriptionMedicine.objects.create(prescription=prescription, **medicine_data)
            
        return prescription

    def update(self, instance, validated_data):
        medicines_data = validated_data.pop('medicines', None)
        
        # Update prescription fields
        instance.diagnosis = validated_data.get('diagnosis', instance.diagnosis)
        instance.save()
        
        # Update medicines if provided
        if medicines_data is not None:
            # Clear existing medicines
            instance.medicines.all().delete()
            # Add new medicines
            for medicine_data in medicines_data:
                PrescriptionMedicine.objects.create(prescription=instance, **medicine_data)
        
        return instance
    

'''---------3)--------'''

class LabTestSerializer(serializers.ModelSerializer):
    class Meta:
        model = LabTest
        fields = ['test_id', 'test_name', 'price']

class LabTestPrescriptionSerializer(serializers.ModelSerializer):
    tests = LabTestSerializer(many=True, read_only=True)
    test_ids = serializers.PrimaryKeyRelatedField(
        queryset=LabTest.objects.all(),
        many=True,
        write_only=True,
        source='tests'
    )
    doctor_name = serializers.CharField(source='doctor.doc_name', read_only=True)
    patient_name = serializers.CharField(source='patient.full_name', read_only=True)

    class Meta:
        model = LabTestPrescription
        fields = [
            'prescription_id',
            'doctor',
            'doctor_name',
            'patient',
            'patient_name',
            'appointment',
            'test_ids',
            'tests',
            'notes',
            'status',
            'created_at'
        ]
        read_only_fields = ['created_at']

'''--------5)-----'''

class PrescriptionHistorySerializer(serializers.ModelSerializer):
    medicines = PrescriptionMedicineSerializer(many=True, read_only=True)
    doctor_name = serializers.CharField(source='doctor.doc_name', read_only=True)
    patient_name = serializers.CharField(source='patient.full_name', read_only=True)

    class Meta:
        model = Prescription
        fields = [
            'prescription_id',
            'doctor',
            'doctor_name',
            'patient',
            'patient_name',
            'diagnosis',
            'prescription_date',
            'medicines'
        ]