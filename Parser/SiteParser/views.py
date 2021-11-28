from django.shortcuts import render
from django.http import HttpResponse
import requests
from bs4 import BeautifulSoup
from .models import SiteLinkModel
from .forms import Filter


def index(request):
    filter = Filter(initial={'filterField':request.POST.get("filterField")})
    links = []
    if request.method == "POST":
        filterStr = request.POST.get("filterField")
        filter.filterField=filterStr
        if filterStr:
            links=SiteLinkModel.objects.filter(title__icontains=filterStr)

    return render(request, 'index.html', {"links": links,"filter":filter})

def reparse(request,typeUrl):
    url=''
    if(typeUrl==1):
        url = 'https://metanit.com/sharp/tutorial/'
    if (typeUrl == 2):
        url = 'https://metanit.com/python/tutorial/'
    response = requests.get(url)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'lxml')
    page_allLinks = soup.find("ol", class_="content").find_all("a")

    links = SiteLinkModel.objects.all()
    links.delete()

    for link in page_allLinks:
        linkToSave = SiteLinkModel.objects.create(title=link.text, link=url+link.get('href'))
        linkToSave.save()

    return render(request, 'reparse.html')
