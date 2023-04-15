from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.http import HttpResponse

# relative import of forms
from .models import ProjectsModel, TasksModel
from .forms import ProjectsForm, TasksForm

def home(request):
    if request.method == "POST":
        # projects
        if "LIST" in request.POST:
            return HttpResponseRedirect("/list/")
        if "VIEW" in request.POST:
            return HttpResponseRedirect("/view/")
        if "CREATE" in request.POST:
            return HttpResponseRedirect("/create/")
        if "MODIFY" in request.POST:
            return HttpResponseRedirect("/update/")
        if "DELETE" in request.POST:
            return HttpResponseRedirect("/delete/")
        # tasks
        if "BULLET" in request.POST:
            return HttpResponseRedirect("/bullet/")
        if "NEW" in request.POST:
            return HttpResponseRedirect("/new/")
        if "EDIT" in request.POST:
            return HttpResponseRedirect("/edit/")
        if "REMOVE" in request.POST:
            return HttpResponseRedirect("/remove/")

    return render(request, "home.html")

def create_view(request):
    # dictionary for initial data with field names as keys
    context = {}
    # add the dictionary during initialisation
    form = ProjectsForm(request.POST or None)
    if form.is_valid():
        form.save()
    
    context['form'] = form

    if request.method == "POST":
        return HttpResponseRedirect('/success/')

    return render(request, "create_view.html", context)

def new_view(request):
    # dictionary for initial data with field names as keys
    context = {}
    # add the dictionary during initialisation
    form = TasksForm(request.POST or None)
    if form.is_valid():
        form.save()
    
    context['form'] = form

    if request.method == "POST":
        return render(request, "success.html")

    return render(request, "create_view.html", context)

def list_view(request):
    # dictionary for initial data with field names as keys
    context = {}
    # add dictionary during initialisation
    context['dataset'] = ProjectsModel.objects.all()

    return render(request, "list_view.html", context)

def bullet_view(request):
    # dictionary for initial data with field names as keys
    context = {}
    # add dictionary during initialisation
    context['dataset'] = TasksModel.objects.all()

    return render(request, "bullet_view.html", context)

def project_selection(request):
    context = {}
    # context['names'] = ProjectsModel.objects.values_list('name', flat=True)
    context['ids'] = ProjectsModel.objects.values_list('id', flat=True)
    # data = {}
    # for id in context['ids']:
        # data[id] = ProjectsModel.objects.get(id=id).name
    if request.method == "POST":
        project_id = request.POST.get('project')
        context['data'] = ProjectsModel.objects.get(id=project_id)
        return HttpResponseRedirect(str(project_id) + "/")

    return  render(request, "project_selection.html", context)

def task_selection(request):
    context = {}
    # context['names'] = ProjectsModel.objects.values_list('name', flat=True)
    context['ids'] = TasksModel.objects.values_list('id', flat=True)
    # data = {}
    # for id in context['ids']:
        # data[id] = TasksModel.objects.get(id=id).name
    if request.method == "POST":
        task_id = request.POST.get('task')
        context['data'] = TasksModel.objects.get(id=task_id)
        return HttpResponseRedirect(str(task_id) + "/")

    return  render(request, "task_selection.html", context)

def detail_view(request, id):
    # dictionary for initial data with field names as keys
    context = {}
    # add the dictionary during initialisation
    project_object = ProjectsModel.objects.get(id=id)
    context['data'] = project_object
    context['tasks'] = list(TasksModel.objects.filter(project__name=project_object.name).values_list('name', flat=True))
    context['stylesheet'] = "./static/style.css"
    
    return render(request, "detail_view.html", context)

# update view for details
def update_view(request, id):
    # dictionary for initial data with field names as keys
    context = {}
    # fetch the object related to passed id
    obj = get_object_or_404(ProjectsModel, id=id)
    # pass the object as instance in form
    form = ProjectsForm(request.POST or None, instance=obj)
    # save the data from the form and redirect to detail_view
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/success/')
    
    # add form dictionary to context
    context['form'] = form

    if request.method == "POST":
        return HttpResponseRedirect('/success/')

    return render(request, "update_view.html", context)

def success_view(request):
    return render(request, "success.html")

def edit_view(request, id):
    # dictionary for initial data with field names as keys
    context = {}
    # fetch the object related to passed id
    obj = get_object_or_404(TasksModel, id=id)
    # pass the object as instance in form
    form = TasksForm(request.POST or None, instance=obj)
    # save the data from the form and redirect to detail_view
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/success/')
    
    # add form dictionary to context
    context['form'] = form

    if request.method == "POST":
        return HttpResponseRedirect('/success/')

    return render(request, "update_view.html", context)

# delete view for details
def delete_view(request, id):
    # dictionary for initial data with field names as keys
    context = {}
    # fetch the object related to the passed id
    obj = get_object_or_404(ProjectsModel, id=id)

    if request.method == "POST":
        # delete object
        obj.delete()
        # OR redirect to success page
        return HttpResponseRedirect('/success/')
    
    return render(request, "delete_view.html", context)

def remove_view(request, id):
    # dictionary for initial data with field names as keys
    context = {}
    # fetch the object related to the passed id
    obj = get_object_or_404(TasksModel, id=id)

    if request.method == "POST":
        # delete object
        obj.delete()
        # OR redirect to success page
        return HttpResponseRedirect('/success/')
    
    return render(request, "delete_view.html", context)