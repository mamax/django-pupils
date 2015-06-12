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

def groups_list(request):
    groups = (
                {'id': 1,
                'leader': u'Яченюк Олег',
                'name': u'8-A'},
                {'id': 2,
               'leader': u'Подоба Віталій',
                'name': u'5-A'},
                {'id': 3,
               'leader': u'Іванюк Андрій',
                'name': u'8-Б'},
                )
    return render(request, 'pupils/groups_list.html', {'groups': groups})

def groups_add(request):
    return HttpResponse('<h1>Group Add Form</h1>')

def groups_edit(request, gid):
    return HttpResponse('<h1>Edit Group %s</h1>' % gid)

def groups_delete(request, gid):
    return HttpResponse('<h1>Delete Group %s</h1>' % gid)

def journal_list(request):
    return render(request, 'pupils/visiting.html', {})

def journal_pupil(request, gid):
    return HttpResponse('<h1>Journal pupil %s</h1>' % gid)

def journal_group(request, gid):
    return HttpResponse('<h1>Journal all group %s</h1>' % gid)
