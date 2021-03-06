from django.db import models


# TODO Instead of assuming all mainlines are automatically owned, make ownership a list of rules
#   of the different ways people can have access to releases.
#   Potential options:
#     All releases for a product
#     All releases within a mainline
#     All releases after X and before Y date (end of current support)
#     Cherry-picked releases


class OwnedProduct(models.Model):
    group = models.ForeignKey('auth.Group', on_delete=models.CASCADE)
    product = models.ForeignKey('appable.Product', on_delete=models.CASCADE)
    purchased_on = models.DateTimeField()
    valid_until = models.DateTimeField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta(object):
        ordering = ['group__name', 'product__name']

    def __str__(self):
        return '%s, %s' % (self.group, self.product)


class OwnedMainline(models.Model):
    owned_product = models.ForeignKey(OwnedProduct, on_delete=models.CASCADE)
    mainline = models.ForeignKey('appable.Mainline', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta(object):
        ordering = ['owned_product__group__name', 'owned_product__product__name', 'mainline__name']

    def __str__(self):
        return '%s, %s' % (self.owned_product, self.mainline)
