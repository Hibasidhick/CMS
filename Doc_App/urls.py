from django.urls import path
from .views import (
    ConsultationListCreateAPIView,
    ConsultationRetrieveUpdateAPIView,
    ConsultationByAppointmentAPIView,
    DoctorConsultationListAPIView,
    MedicinePrescriptionCreateAPIView,
    MedicinePrescriptionUpdateAPIView,
    PrescriptionByAppointmentAPIView,
    PatientPrescriptionListAPIView,
    LabTestPrescriptionCreateAPIView,
    LabTestPrescriptionUpdateAPIView,
    LabTestPrescriptionByAppointmentAPIView,
    PatientLabTestPrescriptionListAPIView,
    PatientConsultationHistoryView,
    DoctorConsultationHistoryView,
    AppointmentConsultationHistoryView,
    PatientPrescriptionHistoryView,
    DoctorPrescriptionHistoryView,
    AppointmentPrescriptionHistoryView
)

urlpatterns = [
    path('consultations/', ConsultationListCreateAPIView.as_view(), name='consultation-list-create'),
    path('consultations/<int:consultationId>/', ConsultationRetrieveUpdateAPIView.as_view(), name='consultation-retrieve-update'),
    path('consultations/appointment/<int:appointmentId>/', ConsultationByAppointmentAPIView.as_view(), name='consultation-by-appointment'),
    path('consultations/doctor/<int:doctorId>/', DoctorConsultationListAPIView.as_view(), name='doctor-consultations'),
]

urlpatterns += [
    path('prescriptions/medicine/', MedicinePrescriptionCreateAPIView.as_view(), name='medicine-prescription-create'),
    path('prescriptions/medicine/<int:prescriptionId>/', MedicinePrescriptionUpdateAPIView.as_view(), name='medicine-prescription-update'),
    path('prescriptions/medicine/appointment/<int:appointmentId>/', PrescriptionByAppointmentAPIView.as_view(), name='prescription-by-appointment'),
    path('prescriptions/medicine/patient/<int:patientId>/', PatientPrescriptionListAPIView.as_view(), name='patient-prescriptions-list'),
]

urlpatterns += [
    path('prescriptions/labtest/', LabTestPrescriptionCreateAPIView.as_view()),
    path('prescriptions/labtest/<int:prescriptionId>/', LabTestPrescriptionUpdateAPIView.as_view()),
    path('prescriptions/labtest/appointment/<int:appointmentId>/', LabTestPrescriptionByAppointmentAPIView.as_view()),
    path('prescriptions/labtest/patient/<int:patientId>/', PatientLabTestPrescriptionListAPIView.as_view()),
]

urlpatterns += [
    path('consultations/patient/<int:patientId>/', PatientConsultationHistoryView.as_view()),
    path('consultations/doctor/<int:doctorId>/', DoctorConsultationHistoryView.as_view()),
    path('consultations/history/appointment/<int:appointmentId>/', AppointmentConsultationHistoryView.as_view()),
]

urlpatterns += [
    path('prescriptions/medicine/history/patient/<int:patientId>/', PatientPrescriptionHistoryView.as_view()),
    path('prescriptions/medicine/history/doctor/<int:doctorId>/', DoctorPrescriptionHistoryView.as_view()),
    path('prescriptions/medicine/history/appointment/<int:appointmentId>/', AppointmentPrescriptionHistoryView.as_view()),
]