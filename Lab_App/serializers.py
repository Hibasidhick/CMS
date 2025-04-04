from rest_framework import serializers
from CMS_App.models import LabTest, LabReport, LabTestBill
from Doc_App.models import LabTestPrescription

class LabTestSerializer(serializers.ModelSerializer):
    class Meta:
        model = LabTest
        fields = '__all__'  # Includes test_id, test_name, price, and description

class LabReportSerializer(serializers.ModelSerializer):
    patient_name = serializers.CharField(source='patient.full_name', read_only=True)
    doctor_name = serializers.CharField(source='doctor.doc_name', read_only=True)
    test_name = serializers.CharField(source='test.test_name', read_only=True)

    class Meta:
        model = LabReport
        fields = ['report_id', 'patient', 'patient_name', 'doctor', 'doctor_name', 'test', 'test_name', 'normal_range', 'actual_value', 'created_at']

class LabTestBillSerializer(serializers.ModelSerializer):
    patient_name = serializers.CharField(source='patient.full_name', read_only=True)
    doctor_name = serializers.CharField(source='doctor.doc_name', read_only=True)
    test_name = serializers.CharField(source='test.test_name', read_only=True)

    class Meta:
        model = LabTestBill
        fields = ['l_bill_id', 'patient', 'patient_name', 'test', 'test_name', 'doctor', 'doctor_name', 'price', 'gst', 'total_amount']
# ✅ Serializer for LabTestPrescription (Doctor's Order)

class LabTestPrescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = LabTestPrescription
        fields = '__all__'