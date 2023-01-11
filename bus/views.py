from django.shortcuts import render
from django.views import View
from .models import Bus
from .forms import ReserveForm
# Create your views here.
class TicketResveration(View):
    form_class=ReserveForm
    template_name='bus/home.html'
    def get(self,request):
        form=self.form_class
        return render(request,self.template_name,{'form':form})

    def post(self,requset):
        form=self.form_class(requset.POST)
        if form.is_valid():
            clean_form=form.cleaned_data[' ']