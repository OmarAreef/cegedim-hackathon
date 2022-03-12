from rest_framework import serializers
from .models import result_store

class resultSerializer(serializers.ModelSerializer):
    class Meta:
        model = result_store
        fields = [
            "fever",
            "sore_throat",
            "shortness_of_breath",
            "head_ache",
            "age_60_and_above",
            "corona_result"
        ]