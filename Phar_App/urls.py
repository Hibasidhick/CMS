from django.urls import path
from .views import *



urlpatterns = [
    # 🔹 Medicine Management
    path('medicines/', AddMedicineView.as_view(), name='add-medicine'),
    path('medicines/<int:medicine_id>/', GetMedicineView.as_view(), name='get-medicine'),
    path('medicines/<int:medicine_id>/update/', UpdateMedicineView.as_view(), name='update-medicine'),
    path('medicines/all/', ListMedicinesView.as_view(), name='list-medicines'),
    path('medicines/<int:medicine_id>/deactivate/', DeactivateMedicineView.as_view(), name='deactivate-medicine'),
    path('medicines/<int:medicine_id>/delete/', DeleteMedicineView.as_view(), name='delete-medicine'),  # ✅ Fixed URL pattern

    # 🔹 Medicine Inventory Management
    path('inventory/medicine/', AddMedicineStockView.as_view(), name='add-medicine-stock'),
    path('inventory/medicine/<int:medicineStockId>/', UpdateMedicineStockView.as_view(), name='update-medicine-stock'),
    path('inventory/medicine/<int:medicine_id>/stock/', GetMedicineStockView.as_view(), name='get-medicine-stock'),
    path('inventory/medicine/all/', ListMedicineStockView.as_view(), name='list-medicine-stock'),
    path('inventory/medicine/<int:medicineStockId>/flag-low/', FlagLowStockView.as_view(), name='flag-low-stock'),

    # 🔹 Medicine Bills
    path('medicinebills/', ListMedicineBillsView.as_view()),
    path('medicinebills/create/', CreateMedicineBillView.as_view()),
    path('medicinebills/<int:billId>/', GetMedicineBillView.as_view()),
    path('medicinebills/<int:billId>/update/', UpdateMedicineBillView.as_view()),
    path('medicinebills/<int:billId>/delete/', DeleteMedicineBillView.as_view()),
]
