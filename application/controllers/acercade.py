import web
        
render = web.template.render ('application/views/', base='master')
class Acercade:        
    def __init__(self):
        pass
        
    def GET(self):
        datos =['Vite', '00259491@red.unid.mx']
        return render.acercade(datos)
