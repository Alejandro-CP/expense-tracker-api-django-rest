from rest_framework import serializers

from restapi import models


class ExpenseSerializer(serializers.ModelSerializer):
    amount = serializers.FloatField(required=True)
    merchant = serializers.CharField(required=True)
    description = serializers.CharField(required=False)
    category = serializers.CharField(required=True)
    created_at = serializers.DateTimeField(required=False)
    last_updated = serializers.DateTimeField(required=False)

    class Meta:
        model = models.Expense
        fields = "__all__"
        read_only_fileds = ["id", "created_at", "last_updated"]
