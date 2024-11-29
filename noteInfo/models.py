from django.db import models
from django.utils.text import slugify
from django.utils.crypto import get_random_string

# Create your models here.
class Blog(models.Model):
    CATEGORY = (('EDUCATION','Education'),
                ('BITCOIN','Bitcoin'),
                ('GAMING','Gaming'),
                ('DATA ENGINEERING','Data engineering'),
                ('TYPESCRIPT','Typesript'),
                ('CYBERSECURITY','Cybersecurity'),
                ('CROSS PLATFORM','Cross platform'),
                ('FRONTEND','Frontend'),
                ('BACKEND','Backend'),
                ('QUANTUM','Quantum'),
                ('MECHANICAL','Mechanical'),
                ('IOT','Iot'))
    
    title = models.CharField(max_length=100)
    body = models.TextField()
    slug = models.SlugField(unique=True, blank=True, null=True)
    category = models.CharField(max_length=50,choices=CATEGORY,default='EDUCATION')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

#the value of the slug will come from the title slugify(title) plus 5 random characters    
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug:
            slug_base = slugify(self.title)
            slug = slug_base
            #check if slug is unique and modify if not
            if Blog.objects.filter(slug=slug).exists():
                slug = f'{slug_base}-{get_random_string(5)}'
            self.slug = slug
        super(Blog,self).save(*args, **kwargs)


