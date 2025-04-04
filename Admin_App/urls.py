# urls.py

from django.urls import path
from .views import *

urlpatterns = [
    # Department
    path('api/departments/create/', DepartmentCreateView.as_view()),
    path('api/departments/', DepartmentListView.as_view()),

    # Doctor
    path('api/doctors/create/', DoctorCreateView.as_view()),
    path('api/doctors/<int:doc_id>/update/', DoctorUpdateView.as_view()),
    path('api/doctors/<int:doc_id>/', DoctorRetrieveView.as_view()),
    path('api/doctors/', DoctorListView.as_view()),
    path('api/doctors/<int:doc_id>/deactivate/', DoctorDeactivateView.as_view()),
]

urlpatterns += [
    path('receptionists/create/', ReceptionistCreateView.as_view(), name='receptionist-create'),
    path('receptionists/<int:rec_id>/update/', ReceptionistUpdateView.as_view(), name='receptionist-update'),
    path('receptionists/<int:rec_id>/', ReceptionistRetrieveView.as_view(), name='receptionist-detail'),
    path('receptionists/', ReceptionistListView.as_view(), name='receptionist-list'),
    path('receptionists/<int:rec_id>/deactivate/', ReceptionistDeactivateView.as_view(), name='receptionist-deactivate'),
]

urlpatterns += [
    path('labtechnicians/create/', LabTechnicianCreateView.as_view(), name='labtech-create'),
    path('labtechnicians/<int:lab_id>/update/', LabTechnicianUpdateView.as_view(), name='labtech-update'),
    path('labtechnicians/<int:lab_id>/', LabTechnicianRetrieveView.as_view(), name='labtech-detail'),
    path('labtechnicians/', LabTechnicianListView.as_view(), name='labtech-list'),
    path('labtechnicians/<int:lab_id>/deactivate/', LabTechnicianDeactivateView.as_view(), name='labtech-deactivate'),
]

urlpatterns += [
    path('pharmacists/create/', PharmacistCreateView.as_view(), name='pharmacist-create'),
    path('pharmacists/<int:pharm_id>/update/', PharmacistUpdateView.as_view(), name='pharmacist-update'),
    path('pharmacists/<int:pharm_id>/', PharmacistRetrieveView.as_view(), name='pharmacist-detail'),
    path('pharmacists/', PharmacistListView.as_view(), name='pharmacist-list'),
    path('pharmacists/<int:pharm_id>/deactivate/', PharmacistDeactivateView.as_view(), name='pharmacist-deactivate'),
]