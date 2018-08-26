from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView

from trainer_app.models import *



class UserListView(TemplateView):
    template_name = "user_list.html"

    def get(self, request, *args, **kwargs):
        context = super(UserListView, self).get_context_data(**kwargs)
        
        users = User.objects.all()
        context['users'] = users        
        
        return render(self.request, self.template_name, context)
