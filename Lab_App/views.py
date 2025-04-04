from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.utils.dateparse import parse_date
from .models import LabTestPrescription
from CMS_App.models import LabReport, LabTest,LabTestBill
from .serializers import LabReportSerializer, LabTestPrescriptionSerializer,LabTestSerializer,LabTestBillSerializer





# ✅ CREATE Lab Report
class CreateLabReportView(APIView):
    def post(self, request):
        serializer = LabReportSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Lab report created successfully", "data": serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# ✅ RETRIEVE Lab Report by ID
class GetLabReportByIdView(APIView):
    def get(self, request, reportId):
        report = get_object_or_404(LabReport, pk=reportId)
        serializer = LabReportSerializer(report)
        return Response(serializer.data, status=status.HTTP_200_OK)


# ✅ UPDATE Lab Report
class UpdateLabReportView(APIView):
    def put(self, request, reportId):
        report = get_object_or_404(LabReport, pk=reportId)
        serializer = LabReportSerializer(report, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Lab report updated successfully", "data": serializer.data}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# ✅ DELETE Lab Report
class DeleteLabReportView(APIView):
    def delete(self, request, reportId):
        report = get_object_or_404(LabReport, pk=reportId)
        report.delete()
        return Response({"message": "Lab report deleted successfully"}, status=status.HTTP_204_NO_CONTENT)


# ✅ LIST All Lab Reports
class ListLabReportsView(APIView):
    def get(self, request):
        reports = LabReport.objects.all()
        serializer = LabReportSerializer(reports, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


# ✅ 1. Record Lab Test Result (PUT /api/labtests/results/{labTestPrescriptionId}/)
class RecordLabTestResultView(APIView):
    def put(self, request, labTestPrescriptionId):
        lab_report = get_object_or_404(LabReport, pk=labTestPrescriptionId)
        serializer = LabReportSerializer(lab_report, data=request.data, partial=True)
        
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Lab test result updated successfully", "data": serializer.data}, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# ✅ 2. Get Lab Test Result by Appointment ID (GET /api/labtests/results/appointment/{appointmentId}/)
class GetLabTestByAppointmentView(APIView):
    def get(self, request, appointmentId):
        lab_reports = LabReport.objects.filter(appointment__appointment_id=appointmentId)  # ✅ Corrected Query
        if not lab_reports.exists():
            return Response({"message": "No lab test results found for this appointment"}, status=status.HTTP_404_NOT_FOUND)

        serializer = LabReportSerializer(lab_reports, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)



# ✅ 3. List Lab Test Results by Date Range (GET /api/labtests/results?startDate={startDate}&endDate={endDate})
class ListLabTestsByDateView(APIView):
    def get(self, request):
        start_date = request.GET.get('startDate')
        end_date = request.GET.get('endDate')

        if not start_date or not end_date:
            return Response({"error": "Both startDate and endDate are required"}, status=status.HTTP_400_BAD_REQUEST)

        start_date = parse_date(start_date)
        end_date = parse_date(end_date)

        if not start_date or not end_date:
            return Response({"error": "Invalid date format. Use YYYY-MM-DD"}, status=status.HTTP_400_BAD_REQUEST)

        lab_reports = LabReport.objects.filter(created_at__date__range=[start_date, end_date])
        
        if not lab_reports.exists():
            return Response({"message": "No lab test results found in this date range"}, status=status.HTTP_404_NOT_FOUND)

        serializer = LabReportSerializer(lab_reports, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


# ✅ 4. Deactivate Lab Test Prescription (PATCH /api/labtests/{labTestPrescriptionId}/deactivate/)
class DeactivateLabTestPrescriptionView(APIView):
    def patch(self, request, labTestPrescriptionId):
        prescription = get_object_or_404(LabTestPrescription, pk=labTestPrescriptionId)
        prescription.is_active = False
        prescription.save()
        return Response({"message": "Lab test prescription deactivated successfully"}, status=status.HTTP_200_OK)

# ✅ 1. Add New Lab Test (POST /api/labtests/)
class AddLabTestView(APIView):
    def post(self, request):
        serializer = LabTestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Lab test added successfully", "data": serializer.data}, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# ✅ 2. Update Lab Test Details (PUT /api/labtests/{labTestId}/)
class UpdateLabTestView(APIView):
    def put(self, request, labTestId):
        lab_test = get_object_or_404(LabTest, pk=labTestId)
        serializer = LabTestSerializer(lab_test, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Lab test updated successfully", "data": serializer.data}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# ✅ 3. Get Lab Test by ID (GET /api/labtests/{labTestId}/)
class GetLabTestByIdView(APIView):
    def get(self, request, labTestId):
        lab_test = get_object_or_404(LabTest, pk=labTestId)
        serializer = LabTestSerializer(lab_test)
        return Response(serializer.data, status=status.HTTP_200_OK)


# ✅ 4. List All Lab Tests (GET /api/labtests/)
class ListLabTestsView(APIView):
    def get(self, request):
        lab_tests = LabTest.objects.all()
        serializer = LabTestSerializer(lab_tests, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


# ✅ 5. Deactivate Lab Test (PATCH /api/labtests/{labTestId}/deactivate/)
class DeactivateLabTestView(APIView):
    def patch(self, request, labTestId):
        lab_test = get_object_or_404(LabTest, pk=labTestId)
        lab_test.is_active = False  # Ensure the model has an `is_active` field
        lab_test.save()
        return Response({"message": "Lab test deactivated successfully"}, status=status.HTTP_200_OK)


# ✅ Create LabTechBill (POST /api/labtechbills/)
class CreateLabTechBillView(APIView):
    def post(self, request):
        serializer = LabTechBillSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Bill created successfully", "data": serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# ✅ Retrieve Single Bill (GET /api/labtechbills/{billId}/)
class GetLabTechBillByIdView(APIView):
    def get(self, request, billId):
        bill = get_object_or_404(LabTechBill, pk=billId)
        serializer = LabTechBillSerializer(bill)
        return Response(serializer.data, status=status.HTTP_200_OK)

# ✅ Update LabTechBill (PUT /api/labtechbills/{billId}/)
class UpdateLabTechBillView(APIView):
    def put(self, request, billId):
        bill = get_object_or_404(LabTechBill, pk=billId)
        serializer = LabTechBillSerializer(bill, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Bill updated successfully", "data": serializer.data}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# ✅ Delete LabTechBill (DELETE /api/labtechbills/{billId}/)
class DeleteLabTechBillView(APIView):
    def delete(self, request, billId):
        bill = get_object_or_404(LabTechBill, pk=billId)
        bill.delete()
        return Response({"message": "Bill deleted successfully"}, status=status.HTTP_204_NO_CONTENT)

# ✅ List All LabTechBills (GET /api/labtechbills/)
class ListLabTechBillsView(APIView):
    def get(self, request):
        bills = LabTechBill.objects.all()
        serializer = LabTechBillSerializer(bills, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
