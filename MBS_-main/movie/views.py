from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect
from .models import Movie, Review
from .forms import ReviewForm
from django.contrib.auth.decorators import login_required
from .models import Movie, Review
from .forms import ReviewForm
import string
import random

def home(request):
    searchTerm = request.GET.get('searchMovie')
    if searchTerm:
        movies = Movie.objects.filter(title__icontains=searchTerm)
    else:
        movies = Movie.objects.all()
    
    # Separating upcoming movies from currently playing movies
    upcoming_movies = movies.filter(upcoming=True)
    current_movies = movies.filter(upcoming=False)

    return render(request, 'home.html', {
        'searchTerm': searchTerm,
        'upcoming_movies': upcoming_movies,
        'current_movies': current_movies,
    })

def about(request):
    return HttpResponse('<h1>Welcome to About Page</h1>')

def signup(request):
    email = request.GET.get('email')
    return render(request, 'signup.html', {'email':email})

def detail(request, movie_id):
    movie = get_object_or_404(Movie,pk=movie_id)
    reviews = Review.objects.filter(movie = movie)
    return render(request, 'detail.html', {'movie':movie, 'reviews': reviews})

@login_required
def createreview(request, movie_id):
    movie = get_object_or_404(Movie,pk=movie_id)
    if request.method == 'GET':
        return render(request, 'createreview.html', {'form':ReviewForm(), 'movie':movie})
    else:
        try:
            form = ReviewForm(request.POST)
            newReview = form.save(commit=False)
            newReview.user = request.user
            newReview.movie = movie
            newReview.save()
            return redirect('detail', newReview.movie.id)
        except ValueError:
            return render(request, 'createreview.html', {'form':ReviewForm(), 'error':'bad data passed in'})

@login_required
def updatereview(request, review_id):
    review = get_object_or_404(Review, pk=review_id, user=request.user)
    if request.method == 'GET':
        form = ReviewForm(instance=review)
        return render(request, 'updatereview.html', {'review': review, 'form': form})
    else:
        try:
            form = ReviewForm(request.POST, instance=review)
            form.save()
            return redirect('detail', review.movie.id)
        except ValueError:
            return render(request, 'updatereview.html', {'review': review, 'form': form, 'error': 'Bad data in form'})

@login_required
def deletereview(request, review_id):
    review = get_object_or_404(Review, pk=review_id, user=request.user)
    review.delete()
    return redirect('detail', review.movie.id)

@login_required
def purchase_tickets(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    movies = Movie.objects.all()
    showtimes = [movie.showtime_1, movie.showtime_2, movie.showtime_3, movie.showtime_4, movie.showtime_5, movie.showtime_6]
    prices = [m.price for m in movies]
    context = {'movie': movie, 'showtimes': showtimes, 'prices': prices}
    return render(request, 'purchase_tickets.html', context)


@login_required
def purchase_confirm(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    if request.method == 'POST':
        num_tickets = int(request.POST.get('num_tickets', 0))
        theater = request.POST.get('theater_value', '')
        showtime = request.POST.get('showtime_value','')
        print("purchase-confirm",theater,showtime)
        context = {'movie': movie, 'num_tickets': num_tickets, 'theater':theater, 'showtime':showtime}
        return render(request, 'purchase_confirm.html', context)
    return redirect('purchase_tickets', movie_id=movie.id)

import datetime

@login_required
def purchase_complete(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    barcode = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
    
    num_tickets = request.POST.get('ticketCount', 'ERROR')
    theater = request.POST.get('theaterB', 'ERROR')
    showtime = request.POST.get('showtimeB', 'ERROR')
    print("sah dude",theater,showtime)
    user = request.user.username
    now = datetime.datetime.now()

    # Save purchase information to a text file
    with open('purchases.txt', 'a') as f:
        f.write(request.user.username + '\n')
        f.write(movie.title + '\n')
        f.write(str(num_tickets) + '\n')
        f.write(theater + '\n')
        f.write(showtime + '\n')
        f.write(barcode + '\n')
        f.write('\n')
    context = {'movie': movie, 'barcode':barcode, 'num_tickets':num_tickets,'theater':theater,'showtime':showtime}
    return render(request, 'purchase_complete.html', context)


