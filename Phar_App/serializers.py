from rest_framework import serializers
from CMS_App.models import Medicine, MedicineBill
from .models import MedicineStock

# ✅ Medicine Serializer
class MedicineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicine
        fields = '__all__'

# ✅ Medicine Stock Serializer
class MedicineStockSerializer(serializers.ModelSerializer):
    medicine_name = serializers.CharField(source='medicine.medicine_name', read_only=True)

    class Meta:
        model = MedicineStock
        fields = '__all__'

# ✅ Medicine Bill Serializer
class MedicineBillSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicineBill
        fields = '__all__'
