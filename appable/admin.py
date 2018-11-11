from django.contrib import admin
from appable.models import Product, Mainline, Release, ReleaseFile, ReleaseFileType

admin.site.register(Product)
admin.site.register(Mainline)
admin.site.register(Release)
admin.site.register(ReleaseFileType)
admin.site.register(ReleaseFile)
