import web
        
urls = (
    '/', 'Index',
    '/acercade', 'Acercade',
)
render = web.template.render ('templates/', base='master')

class Index:        
    def GET(self):
        datos=['Vite', '00259491@red.unid.mx']
        return render.index(datos)
        

class Acercade:
    def GET (self):
        return render.acercade()

if __name__ == "__main__":
    web.config.debug= False     
    app = web.application(urls, globals())
    app.run()
