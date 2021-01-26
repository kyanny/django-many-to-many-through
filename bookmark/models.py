from django.db import models

# Create your models here.
class Bookmark(models.Model):
    url = models.TextField()
    tags = models.ManyToManyField("Tag", through="Tag2Bookmark")

    class Meta:
        db_table = 'bookmark'

    def __str__(self):
        return self.url


class Tag(models.Model):
    name = models.TextField()

    class Meta:
        db_table = 'tag'

    def __str__(self):
        return self.name


class Tag2Bookmark(models.Model):
    bookmark = models.ForeignKey("Bookmark", on_delete=models.CASCADE)
    tag = models.ForeignKey("Tag", on_delete=models.CASCADE)
    tagged_at = models.DateTimeField()

    class Meta:
        db_table = 'tag2bookmark'
