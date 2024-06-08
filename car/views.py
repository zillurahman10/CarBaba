from django.shortcuts import render, redirect
from django.views.generic import DetailView
from . import models
from . import forms
from user.models import Order
from car.models import Car

# Create your views here.
class DetailCarView(DetailView):
    model = models.Car
    pk_url_kwarg = 'id'
    template_name = 'details.html'

    def post(self, request, *args, **kwargs):
        comment_form = forms.CommentForm(data=self.request.POST)
        car = self.get_object()
        if self.request.method == 'POST':
            new_comment = comment_form.save(commit =False)
            new_comment.car = car
            new_comment.save()
        return self.get(request, *args, **kwargs)   

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        car = self.object
        comments = car.comments.all()
        comment_form = forms.CommentForm(data=self.request.POST)
        
        
        context['comments'] = comments
        context['comment_form'] = comment_form
        return context
    
    
def buy_car(request, id):
    if request.method == "POST":
        car = Car.objects.get(id = id)
        car.quantity -= 1
        car.save()
        order = Order.objects.create(car = car, user = request.user)
        order.save()
    return redirect('profile')
