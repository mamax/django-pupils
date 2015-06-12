# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse

def pupils_list(request):
    pupils = (
                {'id': 1,
                'first_name': u'Віталій',
                'last_name': u'Подоба',
                'ticket': 235,
                'image': 'img/me.jpeg'},
                {'id': 2,
                'first_name': u'Андрій',
                'last_name': u'Корост',
                'ticket': 2123,
                'image': 'img/piv.png'},
                )
    return render(request, 'pupils/pupils_list.html', {'pupils': pupils})

def pupils_add(request):
    return HttpResponse('<h1>Student Add Form</h1>')

def pupils_edit(request, sid):
    return HttpResponse('<h1>Edit Student %s</h1>' % sid)

def pupils_delete(request, sid):
    return HttpResponse('<h1>Delete Student %s</h1>' % sid)

