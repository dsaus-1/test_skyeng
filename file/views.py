from django.views.generic import ListView, CreateView, \
    UpdateView, DeleteView
from django.contrib.auth.mixins import UserPassesTestMixin
from django.urls import reverse_lazy
from django.shortcuts import render, get_object_or_404
import json

from file.models import File
from file.forms import FileForm
from config.settings import BASE_DIR


class FileListView(UserPassesTestMixin, ListView):
    model = File

    def test_func(self):
        return self.request.user.is_authenticated


class FileCreateView(UserPassesTestMixin, CreateView):
    model = File
    form_class = FileForm
    success_url = reverse_lazy('file:home')

    def form_valid(self, form):
        '''
        Если данные валидны, сохраняет текущего пользователя
        '''

        if form.is_valid():
            self.object = form.save()
            self.object.user = self.request.user
            self.object.save()
        return super(FileCreateView, self).form_valid(form)

    def test_func(self):
        return self.request.user.is_authenticated


class FileUpdateView(UserPassesTestMixin, UpdateView):
    model = File
    form_class = FileForm
    success_url = reverse_lazy('file:home')

    def test_func(self):
        file = self.get_object()

        return file.user == self.request.user

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()

        self.object.verified = False
        self.object.status = File.STATUS_UPDATED
        self.object.save()
        return super().post(request, *args, **kwargs)


class FileDeleteView(UserPassesTestMixin, DeleteView):
    model = File
    success_url = reverse_lazy('file:home')

    def test_func(self):
        file = self.get_object()

        return file.user == self.request.user


def page_logging(request):
    user_log = []

    with open('logging.log', 'r') as data:
        for log in data:
            log = json.loads(log)

            if log['user'] == request.user.pk:
                file = File.objects.get(pk=log['file'])
                if file:
                    log['file'] = file   
                    user_log.append(log)

    return render(request, 'file/logging_list.html', context={'user_log': user_log})
