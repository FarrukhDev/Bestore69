from django.shortcuts import render, redirect
from django.views import View
from mijoz.models import Mijoz


class HomeView(View):
    def get(self,request):
        return render(request,'index.html')
    def post(self,request):
        Mijoz.objects.create(
            ism = request.POST.get('ism'),
            telefon = request.POST.get('telefon')
        )
        return redirect('home')

class AntiView(View):
    def get(self,request):
        return render(request,'antipashsha.html')
    def post(self,request):
        Mijoz.objects.create(
            ism = request.POST.get('ism'),
            telefon = request.POST.get('telefon'),
            citi = request.POST.get('citi')
        )
        return redirect('home')

class MuscleView(View):
    def get(self,request):
        return render(request,'muscle.html')
    def post(self,request):
        Mijoz.objects.create(
            ism = request.POST.get('ism'),
            telefon = request.POST.get('telefon'),
            citi=request.POST.get('citi')

        )
        return redirect('home')

class VibroView(View):
    def get(self,request):
        return render(request,'vibro.html')
    def post(self,request):
        Mijoz.objects.create(
            ism = request.POST.get('ism'),
            telefon = request.POST.get('telefon'),
            citi=request.POST.get('citi')

        )
        return redirect('home')