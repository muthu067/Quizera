from django.db import models
from django.utils.text import slugify

class course(models.Model):
    title=models.CharField(max_length=100)
    img_url=models.URLField(max_length=500,null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    slug=models.SlugField(blank=True, null=True)
    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        base_slug = slugify(self.title)
        slug = base_slug
        num = 1
        while course.objects.filter(slug=slug).exclude(pk=self.pk).exists():
            slug = f"{base_slug}-{num}"
            num += 1
        self.slug = slug
        super().save(*args, **kwargs)

class about_us(models.Model):
    content=models.TextField()