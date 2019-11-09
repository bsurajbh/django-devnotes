from django.db import models
from django.shortcuts import reverse


class Devnote(models.Model):
    """ developer notes model"""
    name = models.CharField(max_length=255, null=False, blank=False)
    description = models.TextField()
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    completed_at = models.DateTimeField(blank=True, null=True)

    def get_absolute_url(self):
        """redirect on success"""
        return reverse('devnotes:list')
