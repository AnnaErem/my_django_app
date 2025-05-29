from django.shortcuts import render
import datetime, math
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.db.models import Count, Avg, Min, Max, StdDev, Sum
from .models import Educational_ProgrammModel
from .forms import Educational_ProgrammModelFrom, ProgrammForm

def index(request):
    return render(request, "StelmakApp/index.html")

def programm_model_form(request):
    print("request.method: ", request.method)
    if request.method == "POST":
        form = Educational_ProgrammModelFrom(request.POST)
        if form.is_valid():
            print("\nform_is_valid:\n", form)
            form.save()
            return redirect("StelmakApp:programm_result")
    else:
        form = Educational_ProgrammModelFrom()
        print("\nform_else:\n", form)
    context = {"form": form}
    print("\ncontext:\n", context)
    return render(request, "StelmakApp/programm_model_form.html", context)

def solution(courses):
    result = 4-courses
    return result


def programm_result(request):
    object_list = Educational_ProgrammModel.objects.all().order_by("-id")
    print("\n\nobject_list: ", object_list)

    last_object = object_list.values("name", "date_of_birth", "year", "courses", "last_year", "result")[0]
    print("\n\nlast_object: ", last_object)
    name_formulation = object_list.values("name")[0]
    name_id = object_list.values("id")[0]["id"]
    print("task_id task_formulation: ", name_id, name_formulation)


    result = solution(last_object['courses'])
    print("\nresult: ", result)
  
    
    
    update_obj = Educational_ProgrammModel.objects.filter(id=name_id)
    update_result = result
    update_obj.update(result = update_result )

    # list
    values_list = object_list.values_list()[0]
    print("\nvalues_list: ", values_list)
    name_formulation = values_list[1]
    print("\ntask_formulation: ", name_formulation)
    last_values = [values_list[1], values_list[2], values_list[3], values_list[4], values_list[5], values_list[6]]
    print("\nlast_values:", last_values)


    context = {
        "last_object": last_object,
        "name_formulation": name_formulation,
        "last_values": last_values,
        "result": result,
    }
    return render(request, "StelmakApp/programm_result.html", context)

def table(request):
    objects_values = Educational_ProgrammModel.objects.values()
    print("\nobjects_values:", objects_values)
    objects_values_list = (
        Educational_ProgrammModel.objects.values_list().filter(courses=3).order_by("name")
    ) 
    print("\nobjects_values_list:", objects_values_list)
    cur_objects = objects_values_list
    statics_val = [
        cur_objects.aggregate(Avg("courses")),
        cur_objects.aggregate(Min("courses")),
        cur_objects.aggregate(Max("courses")),
        cur_objects.aggregate(Sum("result")),
    ]
    print("\nstatics_val:", statics_val)
    statics = {"statics_val": statics_val}
    # fields_name
    fields = Educational_ProgrammModel._meta.get_fields()
    print("\nfields", fields)
    verbose_name_list = []
    name_list = []
    for e in fields:
        verbose_name_list.append(e.verbose_name)
        name_list.append(e.name)
    print("\nverbose_name_list:", verbose_name_list)
    print("\nname_list", name_list)
    field_names = verbose_name_list
    context = {
        "objects_values": objects_values,
        "name_list": name_list,
        "objects_values_list": objects_values_list,
        "verbose_name_list": verbose_name_list,
        "statics": statics,
        "field_names": field_names,
    }
    return render(request, "StelmakApp/table.html", context)

def datetimenow (request):
    datetime_now: datetime = datetime.datetime.now()
    context = {'key': datetime_now}
    return render (request, 'StelmakApp/datetime_now.html', context)

def programm_form(request):
    programm_form = ProgrammForm()
    return render(request, "programm_form.html", {"programm_form": programm_form})

def programm_get(request):
    print(request.GET)
    name_value = (request.GET.get("name"))
    date_of_birth_value = int(request.GET.get("date_of_birt"))
    year_value =int(request.GET.get("year")) 
    courses_value = int(request.GET.get("courses")) 
    last_year_value = int(request.GET.get('last_year'))
    new_object = Educational_ProgrammModel(name=name_value, date_of_birth=date_of_birth_value, year=year_value, courses = courses_value, last_year=last_year_value)
    new_object.save()
    return redirect("StelmakApp:programm_result")