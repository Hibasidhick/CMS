
from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from CMS_App.models import Medicine,MedicineBill
from .models import MedicineStock
from .serializers import MedicineSerializer, MedicineStockSerializer,MedicineBillSerializer

# ===========================
# ✅ 5.1. Medicine Management
# ===========================

# ✅ Add New Medicine
class AddMedicineView(generics.CreateAPIView):
    queryset = Medicine.objects.all()
    serializer_class = MedicineSerializer

# ✅ Update Medicine Details
class UpdateMedicineView(APIView):
    def put(self, request, medicine_id):
        medicine = get_object_or_404(Medicine, pk=medicine_id)
        serializer = MedicineSerializer(medicine, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Medicine updated successfully", "data": serializer.data}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# ✅ Get Medicine by ID
class GetMedicineView(generics.RetrieveAPIView):
    queryset = Medicine.objects.all()
    serializer_class = MedicineSerializer
    lookup_field = 'medicine_id'

# ✅ List All Medicines
class ListMedicinesView(generics.ListAPIView):
    queryset = Medicine.objects.all()
    serializer_class = MedicineSerializer

# ✅ Deactivate Medicine
class DeactivateMedicineView(APIView):
    def patch(self, request, medicineId):
        medicine = get_object_or_404(Medicine, pk=medicineId)
        medicine.status = 'Not Available'
        medicine.save()
        return Response({"message": "Medicine deactivated successfully"}, status=status.HTTP_200_OK)



class DeleteMedicineView(APIView):
    def delete(self, request, medicine_id):
        medicine = get_object_or_404(Medicine, pk=medicine_id)
        medicine.delete()
        return Response({"message": "Medicine deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
# =====================================
# ✅ 5.2. Medicine Inventory Management
# =====================================

# ✅ Add New Inventory Item
class AddMedicineStockView(generics.CreateAPIView):
    queryset = MedicineStock.objects.all()
    serializer_class = MedicineStockSerializer

# ✅ Update Inventory Quantity
class UpdateMedicineStockView(APIView):
    def put(self, request, medicineStockId):
        stock = get_object_or_404(MedicineStock, pk=medicineStockId)
        serializer = MedicineStockSerializer(stock, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Stock updated successfully", "data": serializer.data}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# ✅ Get Inventory by Medicine ID
class GetMedicineStockView(APIView):
    def get(self, request, medicineId):
        stock = get_object_or_404(MedicineStock, medicine_id=medicineId)
        serializer = MedicineStockSerializer(stock)
        return Response(serializer.data, status=status.HTTP_200_OK)

# ✅ List All Inventory Items
class ListMedicineStockView(generics.ListAPIView):
    queryset = MedicineStock.objects.all()
    serializer_class = MedicineStockSerializer

# ✅ Flag Low Stock
class FlagLowStockView(APIView):
    def patch(self, request, medicineStockId):
        stock = get_object_or_404(MedicineStock, pk=medicineStockId)
        if stock.quantity <= stock.restock_threshold:
            return Response({"message": "Stock is low, please restock"}, status=status.HTTP_200_OK)
        return Response({"message": "Stock is sufficient"}, status=status.HTTP_200_OK)


# ✅ Create Medicine Bill
class CreateMedicineBillView(APIView):
    def post(self, request):
        serializer = MedicineBillSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  # total will be auto-calculated
            return Response({
                "message": "Medicine bill created successfully",
                "data": serializer.data
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# ✅ Retrieve Single Bill
class GetMedicineBillView(APIView):
    def get(self, request, billId):
        bill = get_object_or_404(MedicineBill, pk=billId)
        serializer = MedicineBillSerializer(bill)
        return Response(serializer.data, status=status.HTTP_200_OK)

# ✅ Update Medicine Bill
class UpdateMedicineBillView(APIView):
    def put(self, request, billId):
        bill = get_object_or_404(MedicineBill, pk=billId)
        serializer = MedicineBillSerializer(bill, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()  # total will be auto-updated in `save()`
            return Response({
                "message": "Medicine bill updated successfully",
                "data": serializer.data
            }, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# ✅ Delete Medicine Bill
class DeleteMedicineBillView(APIView):
    def delete(self, request, billId):
        bill = get_object_or_404(MedicineBill, pk=billId)
        bill.delete()
        return Response({"message": "Medicine bill deleted successfully"}, status=status.HTTP_204_NO_CONTENT)

# ✅ List All Bills
class ListMedicineBillsView(APIView):
    def get(self, request):
        bills = MedicineBill.objects.all()
        serializer = MedicineBillSerializer(bills, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

