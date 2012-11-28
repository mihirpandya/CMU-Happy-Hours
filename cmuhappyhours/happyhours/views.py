# Create your views here.

from datetime import datetime
from happyhours.models import *
from django.http import HttpResponse
from django.template import loader, Context


def hello_view(request):
    """ Simple Hello World View """
    t = loader.get_template('helloworld.html')
    c = Context({
        'current_time': datetime.now(),
    })
    return HttpResponse(t.render(c))

def get_course(course_num):
    try:
        c = Courses.objects.get(course_id=course_num)
        return c
    except:
        return None

def get_ta(ta_name):
    if ta_name is "": return None

    name_l = ta_name.split(" ")
    fname = name_l[0]
    lname = name_l[len(name_l)-1]

    try:
        ta = TA.objects.get(fname=fname)
        return ta

    except:
        try:
            ta = TA.objects.get(lname=lname)
            return ta
        except:
            return None

def get_timings(request):
    if request.method == "GET":
        parameter = request.GET.get('parameter')
        ta = get_ta(parameter)

        if ta is not None:
            ta_id = [ta.u_id]

        else:
            course = get_course(parameter)

            if course is None:
                ta_id = []

            else:
                ta_id = []
                ta_id_temp = TA.objects.filter(courseNum=course.course_id)

                if len(ta_id_temp) > 0:
                    for el in ta_id_temp:
                        ta_id.append(el.u_id)

        result_d = []


        for el in ta_id:
            hours = OfficeHours.objects.filter(ta_id_id=el)
            ta = TA.objects.get(u_id=el)
            for h in hours:
                d = dict()
                d['name'] = ("%s %s" % (ta.fname, ta.lname))
                d['obj'] = h
                result_d.append(d)

        t = loader.get_template("results.html")
        c = Context({'db_results': result_d})
        return HttpResponse(t.render(c))
