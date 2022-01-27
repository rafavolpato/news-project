from rest_framework import viewsets, status, views
from rest_framework.exceptions import ValidationError
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from api import serializers
from api.models import Entry


# @action(methods=['GET', 'PUT'])
class EntryViewSet(viewsets.ModelViewSet):
    """
    Allows only get and patch:
        - get (/api/entry/) : get data from Entry using site_name
        - patch (/api/entry/id): add 1 to click count
    """
    http_method_names = ['get', 'patch']
    serializer_class = serializers.EntrySerializer
    queryset = Entry.objects.all().order_by('-published')

    def get_queryset(self):
        """
        Check if is a knows site (if no raise Invalid Site) and if a knows one
        :return:
        - all news-site from a specific site
        """
        sites = ["mashable", "techrunch", "theverge"]
        site_name = self.request.query_params.get('site', None)
        id = self.request.query_params.get('id', None)
        if site_name not in sites:
            raise ValidationError(f"Invalid site")

        queryset = Entry.objects.all().filter(site_name=site_name)
        if id:
            queryset.filter(id=id)
        return queryset

    def update(self, request, *args, **kwargs):
        """
        Updates click_count from pk
        """
        entry = get_object_or_404(Entry, id=kwargs["pk"])
        if entry:
            entry.click_count += 1
            entry.save()
            return Response(serializers.EntrySerializer(entry).data)

