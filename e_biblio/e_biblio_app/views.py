from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout
from django.forms import modelform_factory

from e_biblio_data.models import Ouvrage, Chercheur, Emprunt


# Create your views here.
def welcome_fct(request):
    return render(request, "e_biblio_app/welcome.html")


def page_ouvrages(request):
    return render(request,
                  "e_biblio_app/ouvrages.html",
                  {"mes_ouvrages": Ouvrage.objects.all()})


def page_chercheurs(request):
    return render(request,
                  "e_biblio_app/chercheurs.html",
                  {"mes_chercheurs": Chercheur.objects.all()})


def page_emprunts(request):
    return render(request,
                  "e_biblio_app/emprunts.html",
                  {"mes_emprunts": Emprunt.objects.all()})


def login_admin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is None:
            return render(request, 'e_biblio_app/login_admin.html')
        else:
            return redirect('/home')

    return render(request, 'e_biblio_app/login_admin.html')


def logout_admin(request):
    logout(request)
    return redirect('/')


# ----------------------------------------------------------------------------OUVRAGE:
OuvrageForm = modelform_factory(Ouvrage, exclude=[])


def new_ouvrage(request):
    if request.method == "POST":
        form = OuvrageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/ouvrages")
    else:
        form = OuvrageForm()
    return render(request,
                  "e_biblio_app/new_ouvrage.html",
                  {"form": form})


def update_ouvrage(request, id):
    ouvrage = Ouvrage.objects.get(id=id)
    form = OuvrageForm(request.POST, instance=ouvrage)
    if form.is_valid():
        form.save()
        return redirect("/ouvrages")
    return render(request, 'e_biblio_app/update_ouvrage.html', {'ouvrage': ouvrage})


def destroy_ouvrage(request, id):
    ouvrage = Ouvrage.objects.get(id=id)
    ouvrage.delete()
    return redirect("/ouvrages")


# ----------------------------------------------------------------------------CHERCHEUR:
ChercheurForm = modelform_factory(Chercheur, exclude=[])


def new_chercheur(request):
    if request.method == "POST":
        form = ChercheurForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/chercheurs")
    else:
        form = ChercheurForm()
    return render(request,
                  "e_biblio_app/new_chercheur.html",
                  {"form": form})


def update_chercheur(request, id):
    chercheur = Chercheur.objects.get(id=id)
    form = ChercheurForm(request.POST, instance=chercheur)
    if form.is_valid():
        form.save()
        return redirect("/chercheurs")
    return render(request, 'e_biblio_app/update_chercheur.html', {'chercheur': chercheur})


def destroy_chercheur(request, id):
    chercheur = Chercheur.objects.get(id=id)
    chercheur.delete()
    return redirect("/chercheurs")


# ----------------------------------------------------------------------------EMPRUNT:
EmpruntForm = modelform_factory(Emprunt, exclude=[])


def new_emprunt(request):
    if request.method == "POST":
        form = EmpruntForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/emprunts")
    else:
        form = EmpruntForm()
    return render(request,
                  "e_biblio_app/new_emprunt.html",
                  {"form": form})


def update_emprunt(request, id):
    emprunt = Emprunt.objects.get(id=id)
    form = EmpruntForm(request.POST, instance=emprunt)
    if form.is_valid():
        form.save()
        return redirect("/emprunts")
    return render(request, 'e_biblio_app/update_emprunt.html',
                  {'emprunt': emprunt,
                   "mes_chercheurs": Chercheur.objects.all(),
                   "mes_ouvrages": Ouvrage.objects.all(),
                   }
                  )


def destroy_emprunt(request, id):
    emprunt = Chercheur.objects.get(id=id)
    emprunt.delete()
    return redirect("/emprunts")
