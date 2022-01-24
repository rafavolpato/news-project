from rest_framework import serializers
from api.models import Entry


class EntrySerializer(serializers.ModelSerializer):
    """
    serialize Entry table
    """
    site_name = serializers.CharField()
    link = serializers.CharField()
    title = serializers.CharField()
    published = serializers.DateTimeField
    summary = serializers.CharField()
    click_count = serializers.IntegerField

    class Meta:
        model = Entry
        fields = [
            'id', 'site_name', 'link', 'title', 'published', 'summary', 'click_count'
        ]
