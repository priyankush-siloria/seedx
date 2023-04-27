from collections.abc import Mapping

from rest_framework.serializers import (
    ModelSerializer
)
from .models import (
    Seed,
    Tag
)


class TagSerializer(ModelSerializer):
    class Meta:
        model = Tag
        fields = "__all__"

    def to_internal_value(self, data: Mapping):
        # If we get null value for short_name, we give it one ourselves.
        if data.get("tag_type"):
            data["tag_type"] = data["tag_type"].title()
        if data.get("value"):
            data["value"] = data["value"].title()
        if not data.get("short_name") and data.get("value"):
            count = 1
            short_name = data.get("value")[:count]
            while Tag.objects.filter(short_name=short_name).exists():
                count += 1
                short_name = data.get("value")[:count]
            data["short_name"] = short_name
        return super().to_internal_value(data)


class SeedSerializer(ModelSerializer):
    tags = TagSerializer(read_only=True, many=True)

    class Meta:
        model = Seed
        fields = "__all__"
