from django.db import models

# категория товара
class Category(models.Model):
    title = models.CharField(max_length=300, unique=True)

    class Meta:
        db_table = 'Category'

    def __str__(self):
        return self.title


# производитель
class Manufacturer(models.Model):
    title = models.CharField(max_length=300, unique=True)

    class Meta:
        db_table = 'Manufacturer'

    def __str__(self):
        return self.title


# поставщик
class Supplier(models.Model):
    title = models.CharField(max_length=300, unique=True)

    class Meta:
        db_table = 'Supplier'

    def __str__(self):
        return self.title


# товар
class Product(models.Model):
    article = models.CharField(max_length=50)
    name = models.CharField(max_length=300)
    unit = models.CharField(max_length=200)
    price = models.FloatField()

    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, null=True)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)

    discount = models.FloatField()
    amount = models.PositiveIntegerField()
    description = models.TextField()
    photo = models.ImageField(upload_to='images', blank=True, null=True)

    class Meta:
        db_table = 'Product'

    def __str__(self):
        return self.name