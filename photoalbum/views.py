from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView
from django.views.generic.base import View
from rest_framework import viewsets
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import ReviewSerializer
from rest_framework.response import Response

from .models import Post, PostImage, PremAlbum, Premium, Vip, VipAlbum, Category, FullAlbum, Full, Author, Review
from .forms import ContactForm
from .filters import CategotyFilter

class ReviewViewSet(viewsets.ModelViewSet):

    serializer_class = ReviewSerializer
    queryset = Review.objects.all()


class SingleReviewView(RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


def main_view(request):
    return render(request, 'main.html')


def blog_view(request):
    posts = Post.objects.all()
    prems = Premium.objects.all()
    vips = Vip.objects.all()
    fulls = Full.objects.all()
    return render(request, 'blog.html', {'posts': posts, 'prems': prems, 'vips': vips, 'fulls': fulls})


def detail_view(request, id):
    post = get_object_or_404(Post, id=id)
    photos = PostImage.objects.filter(post=post)
    return render(request, 'detail.html', {
        'post': post,
        'photos': photos
    })


def create_post_view(request):
    if request.method == 'POST':
        length = request.POST.get('length')
        title = request.POST.get('title')
        description = request.POST.get('description')

        post = Post.objects.create(
            title=title,
            description=description
        )

        for file_num in range(0, int(length)):
            PostImage.objects.create(
                post=post,
                images=request.FILES.get(f'images{file_num}')
            )

    return render(request, 'create-post.html')


def premdetail_view(request, id):
    prem = get_object_or_404(Premium, id=id)
    photos = PremAlbum.objects.filter(post=prem)
    return render(request, 'detail.html', {
        'prem': prem,
        'photos': photos
    })


def create_prem_view(request):
    if request.method == 'POST':
        length = request.POST.get('length')
        title = request.POST.get('title')
        description = request.POST.get('description')

        prem = Premium.objects.create(
            title=title,
            description=description
        )

        for file_num in range(0, int(length)):
            PremAlbum.objects.create(
                post=prem,
                images=request.FILES.get(f'images{file_num}')
            )

    return render(request, 'createprem-post.html')


def vipdetail_view(request, id):
    vip = get_object_or_404(Vip, id=id)
    photos = VipAlbum.objects.filter(post=vip)
    return render(request, 'vipdetail.html', {
        'vip': vip,
        'photos': photos
    })


def create_vip_view(request):
    if request.method == 'POST':
        length = request.POST.get('length')
        title = request.POST.get('title')
        description = request.POST.get('description')

        vip = Vip.objects.create(
            title=title,
            description=description
        )

        for file_num in range(0, int(length)):
            VipAlbum.objects.create(
                post=vip,
                images=request.FILES.get(f'images{file_num}')
            )

    return render(request, 'createvip-post.html')


def fulldetail_view(request, id):
    full = get_object_or_404(Full, id=id)
    photos = FullAlbum.objects.filter(post=full)
    return render(request, 'fulldatail.html', {
        'vip': full,
        'photos': photos
    })


def create_full_view(request):
    if request.method == 'POST':
        length = request.POST.get('length')
        title = request.POST.get('title')
        description = request.POST.get('description')

        full = Full.objects.create(
            title=title,
            description=description
        )

        for file_num in range(0, int(length)):
            FullAlbum.objects.create(
                post=full,
                images=request.FILES.get(f'images{file_num}')
            )

    return render(request, 'createfull-post.html')


def catalog_view(request):
    categories = Category.objects.all()

    return render(request, 'catalog.html', {'categories': categories})


def contact_view(request):
    return render(request, 'contacts.html')


class AddContact(View):
    def post(self, request):
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("/")

