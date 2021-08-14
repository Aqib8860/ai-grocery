from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from core.models import *
from .models import *
from datetime import date, datetime


# Create your views here.


class AddItemView(LoginRequiredMixin, TemplateView):
    login_url = 'core:user-login'
    redirect_field_name = 'core:user-login'
    template_name = 'core/add.html'

    def post(self, request):
        name = request.POST['item_name']
        quantity = request.POST['quantity']
        status = request.POST['item_status']
        date = request.POST['date']

        items = Item.objects.create(user=request.user, name=name, quantity=quantity, status=status, date=date)
        items.save()
        messages.success(request, 'Item Add Successfully ')
        return redirect('store:add-item')


class TodayItemsView(LoginRequiredMixin, TemplateView):
    login_url = 'core:user-login'
    redirect_field_name = 'core:user-login'
    template_name = 'core/index.html'

    def get_context_data(self, **kwargs):
        today = date.today()
        items = Item.objects.filter(date=today, user=self.request.user)
        context = {'items': items}
        return context


class UpdateItemView(LoginRequiredMixin, TemplateView):
    login_url = 'core:user-login'
    redirect_field_name = 'core:user-login'
    template_name = 'core/update.html'

    def get(self, request, item_id):
        item = get_object_or_404(Item, pk=item_id, user=request.user)
        # if item.user is request.user:
        context = {'item': item}
        return render(request, self.template_name, context)
        

    def post(self,request, item_id):
        name = request.POST['item_name']
        quantity = request.POST['quantity']
        status = request.POST.get('item_status')
        date = request.POST['date']


        item = get_object_or_404(Item, pk=item_id)
        items = Item.objects.filter(pk=item_id).update(user=request.user, name=name, quantity=quantity, status=status, date=date)
        # item.objects.update(user=request.user, name=name, quantity=quantity, status=status, date=date)
        
        return redirect('core:home')


class DeleteItemView(LoginRequiredMixin, TemplateView):
    login_url = 'core:user-login'
    redirect_field_name = 'core:user-login'
    template_name = 'core/index.html'

    def get(self, request, item_id):
        item = get_object_or_404(Item, pk=item_id)
        item.delete()
        return redirect('core:home')
