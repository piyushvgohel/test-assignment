import requests
import uuid 

from lxml import etree

from django.shortcuts import render
from django.http import Http404

from bs4 import BeautifulSoup

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Pacemaker
from selenium import webdriver

#API List 

class PacemakerScrape(APIView):

    def get(self, request):
        driver = webdriver.Chrome('./chromedriver')
        driver.get('https://www.medtronic.com/us-en/patients/treatments-therapies/pacemakers/our.html')
        try:
            for tr in driver.find_elements_by_xpath("//table[contains(@id,'table-')]/tbody/tr"):
                name = tr.find_element_by_xpath(".//td[1]").text
                if Pacemaker.objects.filter(name=name):
                    continue
                model_number = tr.find_element_by_xpath(".//td[2]").text
                if model_number:
                    model_number = ','.join(model_number.split('\n')).strip(',')
                desc = tr.find_element_by_xpath(".//td[3]").text
                pacemaker_obj = Pacemaker.objects.create(uuid=uuid.uuid4(), name=name, model_number=model_number, dimensions_description=desc)
        except Exception as e:
            print(e)
        driver.close()
        return Response({'data':'success'})

class PacemakerList(APIView):

    def get(self, request, format=None):
        pacemaker_objs = Pacemaker.objects.filter(model_number__icontains=request.GET.get("q"))

        data_dict = [
                    {"name":obj.name,
                    "model_number":obj.model_number,
                    "dimensions_description":obj.dimensions_description
                    } for obj in pacemaker_objs]
        return Response(data_dict)


def index(request):
    return render(request, 'index.html', {})