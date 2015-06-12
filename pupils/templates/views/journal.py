# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse


def journal_list(request):
    return render(request, 'pupils/visiting.html', {})

def journal_pupil(request, gid):
    return HttpResponse('<h1>Journal pupil %s</h1>' % gid)

def journal_group(request, gid):
    return HttpResponse('<h1>Journal all group %s</h1>' % gid)
