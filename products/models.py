from django.db import models
from django.utils.html import format_html
from django.contrib.auth import get_user_model

# Create your models here.


class Category(models.Model):
    """
    This class has the necessary fields for products category
    """
    parent = models.ForeignKey(
        "self", default=None, blank=True, null=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)

    def __str__(self):
        return self.title


class Product(models.Model):
    """
    This class is a minimal products model.
    All fields is required.
    """
    seller = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    category = models.ManyToManyField(Category)
    name = models.CharField(max_length=150)
    price = models.PositiveIntegerField()
    stock = models.PositiveIntegerField()
    image = models.ImageField(upload_to='images')
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def image_tag(self):
        """
        This function returns a body to display the image in the admin panel.
        """
        return format_html("<img height=60 width=100 style='border-radius: 8px;' src='{}'>".format(self.image.url))

    def category_to_str(self):
        """
        This function returns product categories in a specific format for display in the admin panel.
        Put / between categories.
        """
        categories = self.category.all()
        if categories:
            return ' / '.join([category.title for category in categories])
        else:
            return '-'
