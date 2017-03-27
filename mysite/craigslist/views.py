from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# from django.http import Http404
# from django.template import loader


from .models import State, Listing


class ListingCreate(CreateView):
    model = Listing
    fields = ['sub_category', 'title', 'description', 'price', 'img_url', 'city']


def view_login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        # Redirect to a success page.
        return redirect('to their city page')

    return render(request)  # add a template and a form


def index(request):
    state_query_set = State.objects.all().order_by('state')

    # location = get_object_or_404(Location, pk=location_id)
    # cities = [thing.city for thing in Location.objects.filter(state=location.state)]
    # cities.sort()
    return render(request, 'craigslist/index.html', {'states': state_query_set, 'length': len(state_query_set)})


def city(request, city_id):
    return render(request, 'craigslist/location.html')


def listings(request, location_id):
    return HttpResponse("list of listing for a give city amd sub-cat")


def listings_detail(request, location_id):
    return HttpResponse("individual listing")
