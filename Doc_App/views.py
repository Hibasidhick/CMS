from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Consultation,LabTestPrescription
from CMS_App.models import Prescription, Appointment, Patient
from .serializers import ConsultationSerializer,PrescriptionSerializer,LabTestPrescriptionSerializer,PrescriptionHistorySerializer

class ConsultationListCreateAPIView(APIView):
    def post(self, request):
        # Create new consultation
        serializer = ConsultationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ConsultationRetrieveUpdateAPIView(APIView):
    def put(self, request, consultationId):
        # Update consultation
        consultation = get_object_or_404(Consultation, pk=consultationId)
        serializer = ConsultationSerializer(consultation, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ConsultationByAppointmentAPIView(APIView):
    def get(self, request, appointmentId):
        # Get consultation by appointment ID
        appointment = get_object_or_404(Appointment, pk=appointmentId)
        consultation = get_object_or_404(Consultation, appointment=appointment)
        serializer = ConsultationSerializer(consultation)
        return Response(serializer.data)

class DoctorConsultationListAPIView(APIView):
    def get(self, request, doctorId):
        # List all consultations by doctor
        consultations = Consultation.objects.filter(doctor=doctorId)
        serializer = ConsultationSerializer(consultations, many=True)
        return Response(serializer.data)
    
'''-------------------prescription-------'''
class MedicinePrescriptionCreateAPIView(APIView):
    def post(self, request):
        serializer = PrescriptionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MedicinePrescriptionUpdateAPIView(APIView):
    def put(self, request, prescriptionId):
        prescription = get_object_or_404(Prescription, pk=prescriptionId)
        serializer = PrescriptionSerializer(prescription, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PrescriptionByAppointmentAPIView(APIView):
    def get(self, request, appointmentId):
        appointment = get_object_or_404(Appointment, pk=appointmentId)
        # Assuming you want to get prescriptions for the patient in this appointment
        prescriptions = Prescription.objects.filter(patient=appointment.patient)
        serializer = PrescriptionSerializer(prescriptions, many=True)
        return Response(serializer.data)

class PatientPrescriptionListAPIView(APIView):
    def get(self, request, patientId):
        patient = get_object_or_404(Patient, pk=patientId)
        prescriptions = Prescription.objects.filter(patient=patient).order_by('-prescription_date')
        serializer = PrescriptionSerializer(prescriptions, many=True)
        return Response(serializer.data)
    
'''---------Lab Test Prescription'''

class LabTestPrescriptionCreateAPIView(APIView):
    def post(self, request):
        serializer = LabTestPrescriptionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LabTestPrescriptionUpdateAPIView(APIView):
    def put(self, request, prescriptionId):
        prescription = get_object_or_404(LabTestPrescription, pk=prescriptionId)
        serializer = LabTestPrescriptionSerializer(prescription, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LabTestPrescriptionByAppointmentAPIView(APIView):
    def get(self, request, appointmentId):
        prescriptions = LabTestPrescription.objects.filter(appointment=appointmentId)
        serializer = LabTestPrescriptionSerializer(prescriptions, many=True)
        return Response(serializer.data)

class PatientLabTestPrescriptionListAPIView(APIView):
    def get(self, request, patientId):
        prescriptions = LabTestPrescription.objects.filter(patient=patientId)
        serializer = LabTestPrescriptionSerializer(prescriptions, many=True)
        return Response(serializer.data)
    
'''--------4)-------'''
class PatientConsultationHistoryView(APIView):
    def get(self, request, patientId):
        consultations = Consultation.objects.filter(patient=patientId).order_by('-created_at')
        serializer = ConsultationSerializer(consultations, many=True)
        return Response(serializer.data)

class DoctorConsultationHistoryView(APIView):
    def get(self, request, doctorId):
        consultations = Consultation.objects.filter(doctor=doctorId).order_by('-created_at')
        serializer = ConsultationSerializer(consultations, many=True)
        return Response(serializer.data)

class AppointmentConsultationHistoryView(APIView):
    def get(self, request, appointmentId):
        consultation = get_object_or_404(Consultation, appointment=appointmentId)
        serializer = ConsultationSerializer(consultation)
        return Response(serializer.data)
    
'''-------5)--------------'''
class PatientPrescriptionHistoryView(APIView):
    def get(self, request, patientId):
        prescriptions = Prescription.objects.filter(patient=patientId).order_by('-prescription_date')
        serializer = PrescriptionHistorySerializer(prescriptions, many=True)
        return Response(serializer.data)

class DoctorPrescriptionHistoryView(APIView):
    def get(self, request, doctorId):
        prescriptions = Prescription.objects.filter(doctor=doctorId).order_by('-prescription_date')
        serializer = PrescriptionHistorySerializer(prescriptions, many=True)
        return Response(serializer.data)

class AppointmentPrescriptionHistoryView(APIView):
    def get(self, request, appointmentId):
        prescriptions = Prescription.objects.filter(appointment=appointmentId)
        serializer = PrescriptionHistorySerializer(prescriptions, many=True)
        return Response(serializer.data)
