__author__ = 'msks'
from .settings import PORTAL_URL

def pupils_proc(request):
    return {'PORTAL_URL': PORTAL_URL}