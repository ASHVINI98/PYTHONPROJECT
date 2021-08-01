from django.shortcuts import render
from  mainApp.models import *
from  mainApp.forms import *
#from  main_page.forms import PaymentForm
from django.urls import reverse_lazy
from bootstrap_modal_forms.generic import BSModalCreateView
from django.views import View
from django.http import HttpResponse


# class PaymentNet(View):
    
#     def get(self, request):
#         form=PaymentForm()
#         title=request.GET.get('title')
#         base=request.GET.get('price')
#         price=base
#         if request.method == 'GET':
#             return render(request,'payment.html',context={'title':title,'price':price,'form':form})

#     def post(self, request):
#         form=PaymentForm()
#         title=request.GET.get('title')
#         base=request.GET.get('price')
#         price=base
#         if request.method=='POST':
#             print('post')
#             form=PaymentForm(request.POST)

#             if form.is_valid():
#                 form.save()
#             else:
#                 print(form.errors)
#         return render(request,'payment.html',context={'title':title,'price':price,'form':form})
def test(request):
    return render(request,'index.html')
    
class CreateNetwork(View):
    
    def get(self, request):
        
        form=CustomizeOrderForm()
        AdvertisementPan=Advertisement2.objects.all()
        ExperienceFlavoursT = Flavours.objects.all()
        Dryc=DryCakes_and_Cookie.objects.all()
        Shakes=shakes_and_Smoothie.objects.all()
        Cupcakes=CupCakes_and_Brownie.objects.all()
        SliderX=Slider.objects.all()
        SliderT = Slider.objects.all()[0:1]
        SliderT1=Slider.objects.all()[1:]
        Ad=Advertisement.objects.all()
        PhotoCakesT = PhotoCakes.objects.all()
        DesignerCakesT=DesignerCakes.objects.all()
        PremiumTableT=PremiumTable.objects.all()
        SomethingElseT=SomethingElse.objects.all()
        Blogs=BrowseBlog.objects.all()
        if request.method == 'GET':
            return render (request, 'index.html', context={'form':form,'slid1':SliderT,'slid':SliderX,'slid2':SliderT1,'ef' : ExperienceFlavoursT,'pc':PhotoCakesT,'dc':DesignerCakesT,'pt':PremiumTableT,'se':SomethingElseT,'adv':Ad,'dry':Dryc,'blog':Blogs,'shake':Shakes,'cup':Cupcakes,'advert':AdvertisementPan})

    def post(self, request):
        form=CustomizeOrderForm()
        AdvertisementPan=Advertisement2.objects.all()
        ExperienceFlavoursT = Flavours.objects.all()
        Dryc=DryCakes_and_Cookie.objects.all()
        Shakes=shakes_and_Smoothie.objects.all()
        Cupcakes=CupCakes_and_Brownie.objects.all()
        SliderX=Slider.objects.all()
        SliderT = Slider.objects.all()[0:1]
        SliderT1=Slider.objects.all()[1:]
        Ad=Advertisement.objects.all()
        PhotoCakesT = PhotoCakes.objects.all()
        DesignerCakesT=DesignerCakes.objects.all()
        PremiumTableT=PremiumTable.objects.all()
        SomethingElseT=SomethingElse.objects.all()
        Blogs=BrowseBlog.objects.all()
        if request.method=='POST':
            print('post')
            form=CustomizeOrderForm(request.POST)

            if form.is_valid():
                form.save()
            else:
                print('invalid fields')
            return render (request, 'index.html', context={'form':form,'slid1':SliderT,'slid':SliderX,'slid2':SliderT1,'ef' : ExperienceFlavoursT,'pc':PhotoCakesT,'dc':DesignerCakesT,'pt':PremiumTableT,'se':SomethingElseT,'adv':Ad,'dry':Dryc,'blog':Blogs,'shake':Shakes,'cup':Cupcakes,'advert':AdvertisementPan})


def product(request):
    flav=request.GET.get('flav')
    print(flav)
    print("111111111111111111111111111111111111111")
    view=FlavouredCake.objects.all().filter(flavour_id=flav)
    print(view)
    if request.method == 'GET':
        return render (request, 'landing-page.html',context={'obj':view})