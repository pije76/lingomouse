from config.models import *
from course.models import *

def app_list(context):
    return {
        'app_list' : Course.objects.all(),
    }
