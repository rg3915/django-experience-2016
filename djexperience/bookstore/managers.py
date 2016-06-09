from django.db import models


class PublishedManager(models.Manager):

    def published(self):
        return self.filter(published=True)
