from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)
    product_key = models.CharField(max_length=100)
    notes = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Mainline(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    notes = models.TextField(blank=True)
    release_date = models.DateField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s - %s' % (self.product, self.name)


class Release(models.Model):
    mainline = models.ForeignKey(Mainline, on_delete=models.CASCADE)
    version_number = models.CharField(max_length=100)
    release_date = models.DateField()
    notes = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta(object):
        ordering = ['mainline__product__name', 'mainline__name', '-version_number']

    def __str__(self):
        return '%s - %s' % (self.mainline, self.version_number)


def release_file_path(instance, filename):
    return 'products/{0}/{1}/{2}/{3}'.format(instance.release.mainline.product.pk,
                                             instance.release.mainline.pk,
                                             instance.release.pk,
                                             filename)


class ReleaseFileType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class ReleaseFile(models.Model):
    release = models.ForeignKey(Release, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, blank=True)
    file_type = models.ForeignKey(ReleaseFileType, on_delete=models.CASCADE)
    file = models.FileField(upload_to=release_file_path)
    notes = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def get_filename(self):
        return self.file.name.split('/')[-1]

    def __str__(self):
        return '%s - %s (%s)' % (self.release, self.name or '(no name)', self.file.name)
