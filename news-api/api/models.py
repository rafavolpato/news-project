from django.db import models


# Create your models here.
class Entry(models.Model):
    """
    Table that contains every news-site from each site.
    """
    site_name = models.CharField(max_length=40, null=False, db_index=True)
    link = models.CharField(max_length=500, null=True, db_index=True)
    title = models.CharField(max_length=100, null=True)
    summary = models.CharField(max_length=500, null=True)
    published = models.DateTimeField()
    click_count = models.IntegerField()
