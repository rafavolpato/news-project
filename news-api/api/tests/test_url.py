from django.urls import reverse, resolve
import api

entry_list_url = reverse('entry-list')
entry_detail_url = reverse('entry-detail', args=[1])


def test_entry_list_resolves() -> None:
    """
    Check if the URL file resolves entry-list urls and use the correct ViewSet (EntryViewSet)
    """
    assert resolve(entry_list_url).func.cls == api.views.EntryViewSet

def test_entry_detail_resolves() -> None:
    """
    Check if the URL file resolves entry-detail urls and use the correct ViewSet (EntryViewSet)
    """
    assert resolve(entry_detail_url).func.cls == api.views.EntryViewSet
