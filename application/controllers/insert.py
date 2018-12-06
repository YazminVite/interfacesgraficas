import web
import application.models.model_datos as model_datos

render = web.template.render('application/views/', base='master')

class Insert:
    def __init__(self):
        pass

    def GET(self):  
        return render.insert()
    
    def POST(self):
        formulario = web.input()
        email = formulario['email']
        nombre = formulario['nombre']
        apellidos = formulario['apellidos']
        telefono = formulario['telefono']
        password = formulario['password']
        model_datos.insert_datos(email, nombre, apellidos, telefono, password)
        raise web.seeother('/')