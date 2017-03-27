from django.contrib import admin

from .models import State, City, Category, SubCategory
from .models import Lister, Listing

admin.site.register(State)
admin.site.register(City)
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Lister)
admin.site.register(Listing)
