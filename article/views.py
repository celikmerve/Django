from django.contrib.auth import authenticate
from django.shortcuts import redirect, render,HttpResponse,redirect
from.forms import ArticleForm
from django.contrib import messages
from.models import Article
# Create your views here.
def index(request):
    context={
        "number1":100,
    }
    liste={
        "numbers":[1,2,3,4,5,6]
    }
    return render(request,"index.html",liste)

def index(request):
    return render(request,"index.html")

def Kullanim_Klavuzlari(request):
    return render(request,"Kullanim_Klavuzlari.html")

def Notlar(request):
    return render(request,"Notlar.html")

def Python(request):
    return render(request,"Python.html")

def veri_yapilari(request):
    return render(request,"veri_yapilari.html")

def Siber_Ataklar(request):
    return render(request,"Siber_Ataklar.html")

def yeni(request):
    return render(request,"yeni.html")

def detail(request,id):
    return HttpResponse("Detail:" + str(id))

def dashboard(request):
    articles=Article.objects.filter(author=request.user)
    context={
        "articles":articles
    }
    return render(request,"dashboard.html",context)

def addArticle(request):
    form=ArticleForm(request.POST or None)
    if form.is_valid():
        article=form.save(commit=False)
        article.author=request.user
        article.save()
        messages.success(request,"Makale başarıyla oluşturuldu.")
        return redirect("index")
   
    return render(request,"addarticle.html",{"form": form})

def detail(request,id): 
    article=Article.objects.filter(id=id).first()
    return render(request,"detail.html",{"article":article})

