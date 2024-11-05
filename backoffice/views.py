from django.shortcuts import render, get_object_or_404, HttpResponse
from .models import Title, Author, Publisher  
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect

# Vue pour la page d'accueil
def home(request):
    return render(request, 'registration/home.html')

# # Vue pour afficher la liste des livres
def title_list(request):
    titles = Title.objects.all()  # Récupère tous les livres
    return render(request, 'titles/list.html', {'titles': titles})

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
    return render(request, 'titles/detail.html', {'title': title})

# Vue pour afficher la liste des éditeurs
def publishers_list(request):
    publishers = Publisher.objects.all()
    return render(request, 'publishers/list.html', {'publishers': publishers})

# Vue pour afficher les détails d'un éditeur
def publisher_detail(request, pubid):
    publisher = get_object_or_404(Publisher, pk=pubid)
    return render(request, 'publishers/detail.html', {'publisher': publisher})

# Vue pour la connexion
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/')  # Redirige vers la page d'accueil après connexion
        else:
            return HttpResponse("Échec de la connexion. Vérifiez vos identifiants.")
    return render(request, 'login.html')  # Affiche le formulaire de connexion

# Vue de test existante
def test(request): 
    html = "<html><body>TRY</body></html>"
    return HttpResponse(html)

# Vue hello existante, avec un paramètre optionnel 'nom'
def hello(request, nom="Test"):
    html = f"<html><body>Hello {nom}</body></html>"
    return HttpResponse(html)


