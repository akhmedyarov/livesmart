
from rest_framework import serializers

from .models import Test


class TestSerializer(serializers.ModelSerializer):
    ideal_range = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Test
        fields = '__all__'

    def get_ideal_range(self, obj):
        if obj.lower and obj.upper:
            return f"{obj.lower} <= value <= {obj.upper}"

        elif obj.lower and not obj.upper:
            return f'value >= {obj.lower}'

        elif not obj.lower and obj.upper:
            return f'value <= {obj.upper}'

    def validate(self, data):
        lower = data.get('lower', None)
        upper = data.get('upper', None)

        is_lower_and_upper_exists = lower and upper
        if is_lower_and_upper_exists and upper < lower:
            raise serializers.ValidationError("Lower value can't exceed upper value")

        if not lower and not upper:
            raise serializers.ValidationError("Lower and upper cannot both be null")

        return data
