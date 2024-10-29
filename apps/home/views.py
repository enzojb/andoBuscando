from typing import Any
from django.shortcuts import render
from django.views.generic import TemplateView
from apps.home.models import Home

# Create your views here.
class HomeView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        context["home"] = Home.objects.all()
        return context
    