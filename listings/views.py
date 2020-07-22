from django.shortcuts import render, get_object_or_404
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from .models import Listing

def index(request):
    listings = Listing.objects.order_by('naslov_knjige').filter(is_published=True)

    paginator = Paginator(listings, 9)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    context = {
        'listings': paged_listings
    }

    return render(request, 'listings/listings.html', context)


def listing(request, listing_id):

    listing = get_object_or_404(Listing, pk=listing_id)

    context = {
        'listing': listing
    }


    return render(request, 'listings/listing.html', context)


def search(request):

    queryset_list = Listing.objects.order_by('-list_date')

    # Keywords(naslov_knjige)
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(naslov_knjige__icontains=keywords)
    
    # Ime_pisca
    if 'ime_p' in request.GET:
        ime_p = request.GET['ime_p']
        if ime_p:
            queryset_list = queryset_list.filter(ime_pisca__iexact=ime_p)
    
    # Prezime_pisca
    if 'prezime_p' in request.GET:
        prezime_p = request.GET['prezime_p']
        if prezime_p:
            queryset_list = queryset_list.filter(prezime_pisca__iexact=prezime_p)
    

    context = {
        'listings': queryset_list
    }

    return render(request, 'listings/search.html', context)


