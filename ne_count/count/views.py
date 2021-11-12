from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls.base import reverse_lazy
from django.views.generic import ListView, CreateView
from django.core import serializers
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout
import datetime

from .forms import *
from .models import *
from .utils import *


class Explorer(DataMixin, ListView):
    model = Parameters
    #ordering = '-time_work'
    template_name = 'count/index.html'
    context_object_name = 'parameters'

    def get_queryset(self):
        list_parameters = []
        parameters = Parameters.objects.all().order_by('-time_create')
        for i in range(1, 13):
            for p in parameters:
                if p.station.pk == i:
                    list_parameters.append(p)
                    break
        return list_parameters

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Эксплуатация', date_now=date.today())
        return {**context, **c_def}


class JournalView(DataMixin, ListView):
    model = Parameters
    template_name = 'count/journal.html'
    context_object_name = 'parameters'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Журнал')
        return {**context, **c_def}


class AddParamrters(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddParametersForm
    template_name = 'count/add_parameters.html'
    login_url = reverse_lazy('home')
    raise_exception = True

    def get_context_data(self, *, object_list=None, **kwarg):
        context = super().get_context_data(**kwarg)
        c_def = self.get_user_context(title='Добавление параметров')
        return {**context, **c_def}


def ShowEngine(request, station_id):
    station = Station.objects.all()
    parameters = Parameters.objects.filter(station_id=station_id).order_by('-time_work')
    my_ser = serializers.serialize('json', Parameters.objects.filter(station_id=station_id).order_by('-time_work'))
    context = {
        'station': station,
        'parameters': parameters,
        'cat_selected': station_id,
        'menu': menu,
        'my_ser': my_ser,
    }
    return render(request, 'count/parameters.html', context)


class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'count/login.html'

    def get_context_data(self, **kwargs):
        content = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Авторизация")
        return {**content, **c_def}

    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    logout(request)
    return redirect('login')
