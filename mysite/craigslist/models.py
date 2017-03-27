from django.db import models
from django.core.urlresolvers import reverse


# Create your models here.
class State(models.Model):
    state = models.CharField(max_length=20)

    def __repr__(self):
        return "{}".format(self.state)

    def __str__(self):
        return self.__repr__()


class City(models.Model):
    city = models.CharField(max_length=21)
    state = models.ForeignKey(State, on_delete=models.CASCADE)

    def __repr__(self):
        return "{}, {}".format(self.city, self.state)

    def __str__(self):
        return self.__repr__()


class Category(models.Model):
    category = models.CharField(max_length=30)

    def __repr__(self):
        return "{}".format(self.category.upper())

    def __str__(self):
        return self.__repr__()


class SubCategory(models.Model):
    sub_category = models.CharField(max_length=30)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __repr__(self):
        return "{} > {}".format(self.category, self.sub_category)

    def __str__(self):
        return self.__repr__()


class Lister(models.Model):
    name = models.CharField(max_length=21)
    default_city = models.ForeignKey(City, on_delete=models.CASCADE)

    def __repr__(self):
        return "{}".format(self.name)

    def __str__(self):
        return self.__repr__()


class Listing(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=9, decimal_places=2)
    last_modified = models.DateTimeField(auto_now=True)
    img_url = models.URLField(max_length=200)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    lister = models.ForeignKey(Lister, on_delete=models.CASCADE)
    sub_category = models.ForeignKey(SubCategory, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('listings:detail', kwargs={'pk': self.pk})

    def __repr__(self):
        return "{} ({}: {}, {})".format(self.title, self.lister.name, self.city, self.city.state)

    def __str__(self):
        return self.__repr__()
