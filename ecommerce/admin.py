from django.contrib import admin
from .models import CustomUser,Product,car,Genre,Comment
# Register your models here.


admin.site.register(CustomUser)
admin.site.register(Product)
admin.site.register(car)
admin.site.register(Genre)
admin.site.register(Comment)

