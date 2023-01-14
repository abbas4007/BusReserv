from django.shortcuts import get_object_or_404, render
from .forms import SeatRegisterForm
from django.views import View
from django.contrib import messages
from django.shortcuts import redirect
from .models import Bus
# Create your views here.


class Resveratin(View):
    form_class=SeatRegisterForm
    template_name="Reserve/registerseat.html"
    def get(self,request):
        return render(request,self.template_name,{'form':self.form_class})

    def post(self,request):
        form = self.form_class(request.POST)
        if form.is_valid():          
            bus_number = form.cleaned_data['bus_number']
            bus=get_object_or_404(Bus,bus_number=bus_number)
            seat_num = form.cleaned_data['seat_num']
            bus_number = form.cleaned_data['bus_number']
            bus=Bus.objects.get(bus_number=bus_number ,seat_num=seat_num)
            return render(request,self.template_name,{'bus':'bus'})

            if bus.seat_num_available==False:
                return redirect('Reserve:registerseat')   
                messages.error(request, 'this seat does not exists', 'error')
            bus.seat_num_available=False
            return redirect('Reserve:home')   
            messages.success(request, 'this seat reserved succes', 'succes')

        return redirect('Reserve:home', request)   


class Home(View):
    # form_class=SeatRegisterForm
    bus=Bus.objects.all()
    template_name="Reserve/registerseat.html"
    def get(self,request):
        return render(request,self.template_name,{'bus':'bus'})
