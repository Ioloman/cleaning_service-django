from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import ServiceType, Service, UserService
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import ServiceForm

# Create your views here.


def home(request):
    return render(request, 'html/index.html')


def service_list(request):
    services = Service.objects.all().order_by('-date')
    types = ServiceType.objects.all()
    return render(request, 'html/list.html', {'services': services, 'types': types})


@login_required
def service(request, pk_service):
    service_ = get_object_or_404(Service, service_pk=pk_service)
    return render(request, 'html/service.html', {'service': service_})


@login_required
def service_edit(request, pk_service):
    service_ = get_object_or_404(Service, service_pk=pk_service)
    types = ServiceType.objects.all()
    if request.user.id != service_.user_service_pk.user.id:
        return HttpResponse(403)
    elif request.method == 'GET':
        return render(request, 'html/service_edit.html', {'service': service_, 'types': types})
    elif request.method == 'POST':
        form = ServiceForm(request.POST, instance=service_)
        if form.is_valid():
            service_ = form.save()
            type_name = request.POST.get('type-name')
            if service_.service_type_pk.name != type_name:
                type_ = get_object_or_404(ServiceType, name=type_name)
                service_.service_type_pk = type_
                service_.save()
        return redirect('service', pk_service)


@login_required
def service_create(request):
    if request.method == 'GET':
        types = ServiceType.objects.all()
        user = UserService.objects.get(user=request.user)
        return render(request, 'html/service_create.html', {'types': types, 'service_user': user})
    elif request.method == 'POST':
        form_data = ServiceForm(request.POST)
        if form_data.is_valid():
            service_ = form_data.save(commit=False)
            type_ = get_object_or_404(ServiceType, name=request.POST.get('type-name'))
            service_.service_type_pk = type_
            service_.user_service_pk = UserService.objects.get(user=request.user)
            service_.save()
            return redirect('service', service_.service_pk)
        else:
            return redirect('profile')


@login_required
def service_delete(request, pk_service):
    service_ = get_object_or_404(Service, service_pk=pk_service)
    if request.user.id != service_.user_service_pk.user.id:
        return HttpResponse(403)
    elif request.method == 'POST':
        service_.delete()
        return redirect('profile')


def login_user(request):
    if request.method == 'GET':
        return render(request, 'html/login.html', {'form': AuthenticationForm()})
    elif request.method == 'POST':
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'html/login.html', {'form': AuthenticationForm(), 'error': 'Неверные данные'})
        else:
            login(request, user)
            next_ = request.POST.get('next', '/')
            return HttpResponseRedirect(next_)


@login_required
def logout_user(request):
    if request.method == 'GET':
        logout(request)
        return redirect('home')


@login_required
def profile(request):
    user = UserService.objects.get(user=request.user)
    services = Service.objects.filter(user_service_pk=user)
    return render(request, 'html/profile.html', {'user_service': user, 'services': services})
