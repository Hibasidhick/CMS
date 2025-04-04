# views.py

from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.views import APIView
from django.contrib.auth.models import User
from CMS_App.models import Doctor, Receptionist, LabTechnician, Pharmacist, Department
from .serializers import DoctorSerializer, DepartmentSerializer,LabTechnicianSerializer,ReceptionistSerializer,PharmacistSerializer
from .permissions import IsAdminGroupUser

# -------------------- Department Views --------------------
class DepartmentCreateView(APIView):
    permission_classes = [IsAuthenticated, IsAdminGroupUser]

    def post(self, request):
        serializer = DepartmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DepartmentListView(APIView):
    permission_classes = [IsAuthenticated, IsAdminGroupUser]

    def get(self, request):
        departments = Department.objects.all()
        serializer = DepartmentSerializer(departments, many=True)
        return Response(serializer.data)

# -------------------- Doctor Views --------------------
class DoctorCreateView(APIView):
    permission_classes = [IsAuthenticated, IsAdminGroupUser]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        if not username or not password:
            return Response({"error": "Username and password are required."}, status=status.HTTP_400_BAD_REQUEST)

        # ✅ Check if username already exists
        if User.objects.filter(username=username).exists():
            return Response({"error": "Username already exists."}, status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.create_user(
            username=username,
            password=password
        )

        request_data = request.data.copy()  # Make a mutable copy
        request_data['user'] = user.id

        serializer = DoctorSerializer(data=request_data)
        if serializer.is_valid():
            serializer.save(user=user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        # Clean up user if serializer fails
        user.delete()
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DoctorUpdateView(APIView):
    permission_classes = [IsAuthenticated, IsAdminGroupUser]

    def put(self, request, doc_id):
        doctor = Doctor.objects.get(doc_id=doc_id)
        serializer = DoctorSerializer(doctor, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DoctorRetrieveView(APIView):
    permission_classes = [IsAuthenticated, IsAdminGroupUser]

    def get(self, request, doc_id):
        doctor = Doctor.objects.get(doc_id=doc_id)
        serializer = DoctorSerializer(doctor)
        return Response(serializer.data)

class DoctorListView(APIView):
    permission_classes = [IsAuthenticated, IsAdminGroupUser]

    def get(self, request):
        doctors = Doctor.objects.all()
        serializer = DoctorSerializer(doctors, many=True)
        return Response(serializer.data)

class DoctorDeactivateView(APIView):
    permission_classes = [IsAuthenticated, IsAdminGroupUser]

    def patch(self, request, doc_id):
        doctor = Doctor.objects.get(doc_id=doc_id)
        doctor.is_active = False
        doctor.save()
        return Response({'message': 'Doctor deactivated successfully'})
    

#----------------------- views_receptionist.py------------------
class ReceptionistCreateView(APIView):
    permission_classes = [IsAuthenticated, IsAdminGroupUser]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        if not username or not password:
            return Response({"error": "Username and password are required."}, status=status.HTTP_400_BAD_REQUEST)

        if User.objects.filter(username=username).exists():
            return Response({"error": "Username already exists."}, status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.create_user(username=username, password=password)
        request_data = request.data.copy()
        request_data['user'] = user.id

        serializer = ReceptionistSerializer(data=request_data)
        if serializer.is_valid():
            serializer.save(user=user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        user.delete()
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ReceptionistUpdateView(APIView):
    permission_classes = [IsAuthenticated, IsAdminGroupUser]

    def put(self, request, rec_id):
        receptionist = Receptionist.objects.get(rec_id=rec_id)
        serializer = ReceptionistSerializer(receptionist, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ReceptionistRetrieveView(APIView):
    permission_classes = [IsAuthenticated, IsAdminGroupUser]

    def get(self, request, rec_id):
        receptionist = Receptionist.objects.get(rec_id=rec_id)
        serializer = ReceptionistSerializer(receptionist)
        return Response(serializer.data)

class ReceptionistListView(APIView):
    permission_classes = [IsAuthenticated, IsAdminGroupUser]

    def get(self, request):
        receptionists = Receptionist.objects.all()
        serializer = ReceptionistSerializer(receptionists, many=True)
        return Response(serializer.data)

class ReceptionistDeactivateView(APIView):
    permission_classes = [IsAuthenticated, IsAdminGroupUser]

    def patch(self, request, rec_id):
        receptionist = Receptionist.objects.get(rec_id=rec_id)
        receptionist.is_active = False
        receptionist.save()
        return Response({'message': 'Receptionist deactivated successfully'})
    
#-----------------------views_labtechnician.py---------------------

class LabTechnicianCreateView(APIView):
    permission_classes = [IsAuthenticated, IsAdminGroupUser]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        if not username or not password:
            return Response({"error": "Username and password are required."}, status=status.HTTP_400_BAD_REQUEST)

        if User.objects.filter(username=username).exists():
            return Response({"error": "Username already exists."}, status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.create_user(username=username, password=password)
        request_data = request.data.copy()
        request_data['user'] = user.id

        serializer = LabTechnicianSerializer(data=request_data)
        if serializer.is_valid():
            serializer.save(user=user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        user.delete()
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LabTechnicianUpdateView(APIView):
    permission_classes = [IsAuthenticated, IsAdminGroupUser]

    def put(self, request, lab_id):
        labtech = LabTechnician.objects.get(lab_id=lab_id)
        serializer = LabTechnicianSerializer(labtech, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LabTechnicianRetrieveView(APIView):
    permission_classes = [IsAuthenticated, IsAdminGroupUser]

    def get(self, request, lab_id):
        labtech = LabTechnician.objects.get(lab_id=lab_id)
        serializer = LabTechnicianSerializer(labtech)
        return Response(serializer.data)

class LabTechnicianListView(APIView):
    permission_classes = [IsAuthenticated, IsAdminGroupUser]

    def get(self, request):
        labtechs = LabTechnician.objects.all()
        serializer = LabTechnicianSerializer(labtechs, many=True)
        return Response(serializer.data)

class LabTechnicianDeactivateView(APIView):
    permission_classes = [IsAuthenticated, IsAdminGroupUser]

    def patch(self, request, lab_id):
        labtech = LabTechnician.objects.get(lab_id=lab_id)
        labtech.is_active = False
        labtech.save()
        return Response({'message': 'Lab Technician deactivated successfully'})
    
#------------------- views_pharmacist.py--------------

class PharmacistCreateView(APIView):
    permission_classes = [IsAuthenticated, IsAdminGroupUser]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        if not username or not password:
            return Response({"error": "Username and password are required."}, status=status.HTTP_400_BAD_REQUEST)

        if User.objects.filter(username=username).exists():
            return Response({"error": "Username already exists."}, status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.create_user(username=username, password=password)
        request_data = request.data.copy()
        request_data['user'] = user.id

        serializer = PharmacistSerializer(data=request_data)
        if serializer.is_valid():
            serializer.save(user=user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        user.delete()
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PharmacistUpdateView(APIView):
    permission_classes = [IsAuthenticated, IsAdminGroupUser]

    def put(self, request, pharm_id):
        pharmacist = Pharmacist.objects.get(pharm_id=pharm_id)
        serializer = PharmacistSerializer(pharmacist, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PharmacistRetrieveView(APIView):
    permission_classes = [IsAuthenticated, IsAdminGroupUser]

    def get(self, request, pharm_id):
        pharmacist = Pharmacist.objects.get(pharm_id=pharm_id)
        serializer = PharmacistSerializer(pharmacist)
        return Response(serializer.data)

class PharmacistListView(APIView):
    permission_classes = [IsAuthenticated, IsAdminGroupUser]

    def get(self, request):
        pharmacists = Pharmacist.objects.all()
        serializer = PharmacistSerializer(pharmacists, many=True)
        return Response(serializer.data)

class PharmacistDeactivateView(APIView):
    permission_classes = [IsAuthenticated, IsAdminGroupUser]

    def patch(self, request, pharm_id):
        pharmacist = Pharmacist.objects.get(pharm_id=pharm_id)
        pharmacist.is_active = False
        pharmacist.save()
        return Response({'message': 'Pharmacist deactivated successfully'})