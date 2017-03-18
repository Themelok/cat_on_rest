from django.db import models


# Create your models here.
class Author(models.Model):
    last_name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)

    def __unicode__(self):
        return '%s %s' % (self.last_name, self.first_name)


class Cat(models.Model):
    name = models.CharField(max_length=50)
    age = models.PositiveSmallIntegerField()
    description = models.TextField(blank=True, null=True)
    image = models.ImageField('Uploaded image')
    author = models.ForeignKey(Author, related_name='cats')
