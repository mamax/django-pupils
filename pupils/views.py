from django.shortcuts import render
from django.http import HttpResponse

def pupils_list(request):
    return render(request, 'pupils/index.html', {})

def pupils_add(request):
    return HttpResponse('<h1>Student Add Form</h1>')

def pupils_edit(request, sid):
    return HttpResponse('<h1>Edit Student %s</h1>' % sid)

def pupils_delete(request, sid):
    return HttpResponse('<h1>Delete Student %s</h1>' % sid)

def groups_list(request):
    return render(request, 'pupils/groups.html', {})

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
