from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from .models import Title, Author, Publisher, Reservation
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponseRedirect
from .forms import LoginForm, SignUpForm
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError

# Vue pour la connexion
def login_view(request):
    form=LoginForm()
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, 'You have successfully logged in.')
                return redirect('home')  
            else:
                messages.error(request, 'Invalid username or password.')
           
    return render(request, './registration/login.html', {"form":form})

# Vue pour l'inscription
def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  
    else:
        form = SignUpForm() 

    return render(request, './registration/signup.html', {'form': form})

# Vue pour la déconnexion
def logout_view(request):
    logout(request)
    return redirect('home')

# Vue pour la base.html
def base(request):
    return render(request, 'base.html')

# Vue pour la page d'accueil
def home(request):
    return render(request, 'home.html')

# Vue pour afficher la liste des auteurs
def author_list(request):
    authors = Author.objects.all()  # Récupère tous les auteurs
    return render(request, 'authors/list.html', {'authors': authors})

# Vue pour afficher les détails d'un auteur
def author_detail(request, au_id):
    author = get_object_or_404(Author, pk=au_id)
    return render(request, 'authors/detail.html', {'author': author})

# # Vue pour afficher les détails d'un livre par ISBN
def title_detail(request, isbn):
    title = get_object_or_404(Title, isbn=isbn)
    is_reserved = title.reservation_set.filter(is_active=True).exists()
    return render(request, 'titles/detail.html', {'title': title, 'is_reserved': is_reserved})


# Vue pour afficher la liste des éditeurs
def publishers_list(request):
    publishers = Publisher.objects.all()
    return render(request, 'publishers/list.html', {'publishers': publishers})

# Vue pour afficher les détails d'un éditeur
def publisher_detail(request, pubid):
    publisher = get_object_or_404(Publisher, pk=pubid)
    return render(request, 'publishers/detail.html', {'publisher': publisher})

# Vue pour afficher la liste des livres
def title_list(request):
    query = request.GET.get('q', '') 
    if query:
        titles = Title.objects.filter(title__icontains=query) 
    else:
        titles = Title.objects.all()

    titles = titles.order_by('year_published') 
    paginator = Paginator(titles, 6) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'titles/list.html', {'titles': page_obj, 'query': query})

# Vue pour la reservation
@login_required
def reserve_title(request, isbn):
    title = get_object_or_404(Title, isbn=isbn)
    user = request.user

    if Reservation.objects.filter(user=user, is_active=True).count() >= 3:
        messages.error(request, "Vous ne pouvez pas réserver plus de 3 livres à la fois.")
        return redirect('title_detail', isbn=isbn)
    
    try:
        Reservation.objects.create(user=user, title=title)
        messages.success(request, "Livre réservé avec succès.")
    except IntegrityError:
        messages.error(request, "Ce livre est déjà réservé.")

    return redirect('title_detail', isbn=isbn)


