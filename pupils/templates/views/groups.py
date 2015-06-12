# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse


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
