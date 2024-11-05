from rest_framework import serializers
from ...models import Wedding, Guest, Checklist, BudgetItem, Vendor, WeddingVendor
from django.contrib.auth import get_user_model

from django.utils import timezone

User = get_user_model()

class WeddingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wedding
        fields = '__all__'  # Include all fields for simplicity
        read_only_fields = ['created_at', 'updated_at']  # Protect timestamps from being overwritten

class GuestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guest
        fields = '__all__'
    
    def validate_email(self, value):
        if Guest.objects.filter(email=value).exists():
            raise serializers.ValidationError("A guest with this email already exists.")
        return value

    def validate(self, attrs):
        if attrs.get('attending') is None:
            raise serializers.ValidationError("Attending status must be specified.")
        return attrs

class ChecklistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Checklist
        fields = '__all__'

    def validate_due_date(self, value):
        if value < timezone.now().date():
            raise serializers.ValidationError("Due date cannot be in the past.")
        return value

class BudgetItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = BudgetItem
        fields = '__all__'

    def validate(self, attrs):
        if attrs['spent_amount'] > attrs['allocated_amount']:
            raise serializers.ValidationError("Spent amount cannot exceed allocated amount.")
        return attrs

class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = '__all__'

    def validate_cost(self, value):
        if value < 0:
            raise serializers.ValidationError("Cost cannot be negative.")
        return value

class WeddingVendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeddingVendor
        fields = '__all__'

    def validate(self, attrs):
        if attrs['payment_status'] not in ['paid', 'pending', 'cancelled']:
            raise serializers.ValidationError("Payment status must be either 'paid', 'pending', or 'cancelled'.")
        return attrs
