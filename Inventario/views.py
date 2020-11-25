from django.http import HttpResponse
from django.template import Template,Context
from django.template import loader
from django.shortcuts import redirect
from django.shortcuts import render
from django.contrib.auth import authenticate

template_path = "/Users/Familia/OneDrive/Escritorio/DjangoAlmacen1/DjangoAlmacen/Inventario/Inventario/templates"



def privado(request):
	if not request.user.is_authenticated:
		return redirect('/admin')

	template_file = open(template_path+"/website.html")
	template = Template(template_file.read())
	template_file.close()
	context=Context({"pagina": "Autenticado", "Contenido": "Informacion para usuarios Autenticados"})
	response= HttpResponse(template.render(context))
	return response	
#class Persona(object):

#	def __init__(self, nombre, contrasena):

#	             self.nombre=nombre
#	             self.contrasena=contrasena

def home_view(request):

	template_file = open(template_path+"/website.html")
	template = Template(template_file.read())
	template_file.close()
	context=Context({"pagina": ""})
	response= HttpResponse(template.render(context))
	return response

#	p1= Persona("admin","1234")

#	temasDelcurso=[]

#	ctx=Context({"nombre":p1.nombre,"contrasena":p1.contrasena, "temas": temasDelcurso})

#	return render (request,"website.html",{"nombre":p1.nombre,"contrasena":p1.contrasena, "temas": temasDelcurso})

def inicio(request):

	template_file = open(template_path+"/Inicio.html")
	template = Template(template_file.read())
	template_file.close()
	context=Context({"pagina": "Inicio"})
	response= HttpResponse(template.render(context))
	return response


def formulario(request):

	template_file = open(template_path+"/Formulario.html")
	template = Template(template_file.read())
	template_file.close()
	context=Context({"pagina": "Formulario"})
	response= HttpResponse(template.render(context))
	return response

	#saludo= "Bienvenidos Al Sistema, <a href=\"/admin\"> ir a la administracion del sistema</a>"
    #home_view="Inicio"
    #template_file = open(template_path+"/Website.html")
    #template = Template(templates_file.read())
    #template_file.close()
    #context = Context({"pagina_actual": "Inicio"})
	#response = HttpResponse(templates.render(context))
        
def lista(request):

	template_file = open(template_path+"/Lista.html")
	template = Template(template_file.read())
	template_file.close()
	context=Context({"pagina": "Lista"})
	response= HttpResponse(template.render(context))
	return response	
	#return HttpResponse(saludo)

#def Formulario(resquest):

	#template_file = open(template_path+"/Website.html")
    #template = Template(template_file.read())
    #template_file.close()
    #context = Context({"pagina_actual": "Formulario"})
	#response = HttpResponse(template.render(context))

		
	#return response

#def Lista(resquest):

	#template_file = open(template_path+"/Website.html")
    #template = Template(template_file.read())
    #template_file.close()
    #context = Context({"pagina_actual": "Lista"})
	#response = HttpResponse(template.render(context))

		
	#return response

	