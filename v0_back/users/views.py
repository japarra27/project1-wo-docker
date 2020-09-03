from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import DetailView, RedirectView, UpdateView
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from .models import *
from rest_framework.permissions import IsAuthenticated

User = get_user_model()


class UserDetailView(LoginRequiredMixin, DetailView):

    model = User
    slug_field = "username"
    slug_url_kwarg = "username"


user_detail_view = UserDetailView.as_view()


class UserUpdateView(LoginRequiredMixin, UpdateView):

    model = User
    fields = ["name"]

    def get_success_url(self):
        return reverse("users:detail", kwargs={"username": self.request.user.username})

    def get_object(self):
        return User.objects.get(username=self.request.user.username)

    def form_valid(self, form):
        messages.add_message(
            self.request, messages.INFO, _("Infos successfully updated")
        )
        return super().form_valid(form)


user_update_view = UserUpdateView.as_view()


class UserRedirectView(LoginRequiredMixin, RedirectView):

    permanent = False

    def get_redirect_url(self):
        return reverse("users:detail", kwargs={"username": self.request.user.username})


user_redirect_view = UserRedirectView.as_view()


##Aquí empieza nuestro código

#Crear Proyecto
@csrf_exempt
def Create_Project(request):
    permission_classes = (IsAuthenticated,)
    authentication_class = (TokenAuthentication,)
    comp = request.company
    projectform = CreateProjectForm()
    if request.method == 'POST':
        form = CreateProjectForm(request.POST)
        project = Project(project_name=form['project_name'].value(), project_description=form['project_description'].value(), project_price=form['project_price'].value(),project_company=comp)
        project.save()
            
        return render(request, 'Project1.html', {'formulario':projectform})

    else:
        projectform = CreateProjectForm()

    return render(request, 'NewProject.html', {'formulario':projectform})

# @csrf_exempt
# def Listado_Eventos(request):
#     user = request.user.id
#     queryset = Evento.objects.filter(event_user=user)
#     serializer_class = EventoSerializer
#     permission_classes = (IsAuthenticated,)
#     authentication_class = (TokenAuthentication,)
#     return render(request, 'P4.html',{'queryset':queryset})

# @csrf_exempt
# def Eliminar_Evento(request, evento_id):
#     user = request.user.id
#     queryset = Evento.objects.filter(event_user=user)
#     try:
#         eventos = Evento.objects.get(id=evento_id)
#     except Evento.DoesNotExist:
#         raise Http404
#     eventos.delete()
#     return redirect("http://172.24.98.170:8080/api/eventos/")  

# @csrf_exempt
# def Modificar_Evento2(request, evento_id):  
#     user = request.user.id
#     usere = request.user
#     eventos = Evento.objects.get(event_user=user, id=evento_id) 
#     form = EventoForm(request.POST, instance = eventos)
#     print(form)
#     print(eventos)
#     print('Voy a entrar al formulario')  
#     if form.is_valid():
#         print('Entre al formulario')  
#         form.save()  
#         return redirect("http://172.24.98.170:8080/api/eventos/")  
#     return render(request, 'actualiza_evento.html', {'eventos': eventos, 'formulario':form}) 
