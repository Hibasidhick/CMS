from django.urls import path
from .views import (
    RecordLabTestResultView, GetLabTestByAppointmentView, ListLabTestsByDateView,
    DeactivateLabTestPrescriptionView, AddLabTestView, UpdateLabTestView, 
    GetLabTestByIdView, ListLabTestsView, DeactivateLabTestView,
    CreateLabReportView, GetLabReportByIdView, UpdateLabReportView,
    DeleteLabReportView, ListLabReportsView, ListLabTechBillsView,
    GetLabTechBillByIdView,UpdateLabTechBillView,DeleteLabTechBillView,CreateLabTechBillView,
)


# ✅ API Endpoints
urlpatterns = [
    path('labreports/', ListLabReportsView.as_view()),
    path('labreports/create/', CreateLabReportView.as_view()),
    path('labreports/<int:reportId>/', GetLabReportByIdView.as_view()),
    path('labreports/<int:reportId>/update/', UpdateLabReportView.as_view()),
    path('labreports/<int:reportId>/delete/', DeleteLabReportView.as_view()),

    path('labtests/results/<int:labTestPrescriptionId>/', RecordLabTestResultView.as_view()),
    path('labtests/results/appointment/<int:appointmentId>/', GetLabTestByAppointmentView.as_view()),
    path('labtests/results/', ListLabTestsByDateView.as_view()),
    path('labtests/<int:labTestPrescriptionId>/deactivate/', DeactivateLabTestPrescriptionView.as_view()),
    path('labtests/', AddLabTestView.as_view()),  # POST
    path('labtests/<int:labTestId>/', UpdateLabTestView.as_view()),  # PUT
    path('labtests/<int:labTestId>/deactivate/', DeactivateLabTestView.as_view()),
    path('labtechbills/', ListLabTechBillsView.as_view()),
    path('labtechbills/create/', CreateLabTechBillView.as_view()),
    path('labtechbills/<int:billId>/', GetLabTechBillByIdView.as_view()),
    path('labtechbills/<int:billId>/update/', UpdateLabTechBillView.as_view()),
    path('labtechbills/<int:billId>/delete/', DeleteLabTechBillView.as_view()),
]

