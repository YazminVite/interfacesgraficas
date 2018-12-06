import web
import application.models.model_datos as model_datos

render = web.template.render('application/views/', base='master')

class Update:
    def __init__(self):
        pass

    def GET(self, email): 
        datos = model_datos.select_email(email) 
        return render.update(datos)
    
    def POST(self, email):
        formulario = web.input()
        email = formulario['email']
        nombre = formulario['nombre']
        apellidos = formulario['apellidos']
        telefono = formulario['telefono']
        password = formulario['password']
        model_datos.update_datos(email, nombre, apellidos, telefono, password)
        raise web.seeother('/')
