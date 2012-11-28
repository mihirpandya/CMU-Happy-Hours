# Create your views here.

from datetime import datetime
from django.http import HttpResponse
from django.template import loader, Context


def hello_view(request):
    """ Simple Hello World View """
    t = loader.get_template('helloworld.html')
    c = Context({
        'current_time': datetime.now(),
    })
    return HttpResponse(t.render(c))

def get_timings(request):
	return HttpResponse("Gotta write these methods, dammit!", mimetype="application/json")