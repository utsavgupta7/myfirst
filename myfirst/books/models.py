from django.db import models

class publisher(models.Model):
    name=models.CharField(max_length=30)
    address=models.CharField(max_length=50)
    city=models.CharField(max_length=20)
    website=models.URLField()

    def __unicode__(self):
        return self.name

class author(models.Model):
    first_name=models.CharField(max_length=10)
    last_name=models.CharField(max_length=10)
    email=models.EmailField()

    def __unicode__(self):
        return u'%s%s' %(self.first_name,self.last_name)

class books(models.Model):
    title=models.CharField(max_length=30)
    authors=models.ManyToManyField(author)
    publisher=models.ForeignKey(publisher)
    date=models.DateField()

    def __unicode__(self):
        return self.itle
    
