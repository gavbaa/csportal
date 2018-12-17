import collections

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, Http404
from django.shortcuts import render

from appable.models import Release, Product, ReleaseFile
from whatsmine.models import OwnedProduct, OwnedMainline


def homepage(request):
    return render(request, 'whatsmine/homepage.html', {})


@login_required
def my_products(request):
    groups = request.user.groups.all()
    owned_products = OwnedProduct.objects.select_related('product').filter(group__in=groups)
    return render(request, 'whatsmine/my_products.html', {
        'owned_products': owned_products,
    })


@login_required
def my_releases_for_product(request, product_id):
    groups = request.user.groups.all()
    try:
        product = Product.objects.get(pk=product_id)
    except Product.DoesNotExist:
        raise Http404
    try:
        owned_product = OwnedProduct.objects.select_related('product').get(product__pk=product_id, group__in=groups)
    except OwnedProduct.DoesNotExist:
        raise Http404
    owned_mainlines = OwnedMainline.objects.select_related('mainline').filter(owned_product__group__in=groups)
    releases = Release.objects.select_related('mainline', 'mainline__product'). \
        filter(mainline__product__pk=product_id, mainline__pk__in=[x.mainline.pk for x in owned_mainlines]). \
        filter(release_date__lte=owned_product.valid_until). \
        order_by('-mainline__release_date', '-release_date')

    mainlines_unique = collections.OrderedDict()
    for x in releases:
        mainlines_unique[x.mainline.pk] = x.mainline
    mainlines = mainlines_unique.values()
    releases_by_mainline = collections.defaultdict(list)
    for x in releases:
        releases_by_mainline[x.mainline.pk].append(x)

    return render(request, 'whatsmine/my_releases.html', {
        'product': product,
        'mainlines': mainlines,
        'releases_by_mainline': releases_by_mainline,
    })


@login_required
def release(request, product_id, release_id):
    # Check that the release belongs to the product.
    product = Product.objects.get(pk=product_id)
    try:
        rel = Release.objects.select_related('mainline__product').get(pk=release_id)
    except Release.DoesNotExist:
        raise Http404
    if rel.mainline.product.pk != product_id:
        raise Http404

    # Check that the user has permissions.
    groups = request.user.groups.all()
    try:
        OwnedProduct.objects.select_related('product').get(product=product_id, group__in=groups)
    except OwnedProduct.DoesNotExist:
        raise Http404

    files = ReleaseFile.objects.filter(release=rel)

    return render(request, 'whatsmine/release.html', {
        'product': product,
        'release': rel,
        'files': files,
    })


@login_required
def release_download(request, product_id, release_id, release_file_id):
    # Check that the release belongs to the product.
    product = Product.objects.get(pk=product_id)
    try:
        rel = Release.objects.select_related('mainline__product').get(pk=release_id)
    except Release.DoesNotExist:
        raise Http404
    if rel.mainline.product.pk != product_id:
        raise Http404

    # Check that the user has permissions.
    groups = request.user.groups.all()
    try:
        OwnedProduct.objects.select_related('product').get(product=product_id, group__in=groups)
    except OwnedProduct.DoesNotExist:
        raise Http404

    rf = ReleaseFile.objects.get(pk=release_file_id)

    filename = rf.file.name.split('/')[-1]
    response = HttpResponse(rf.file, content_type='application/octet-stream')
    response['Content-Disposition'] = 'attachment; filename=%s' % filename

    return response
