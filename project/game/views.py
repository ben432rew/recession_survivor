from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth.models import User

class Index(View):
    def get(self, request):
        