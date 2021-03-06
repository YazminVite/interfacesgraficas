import web
'''
Parametros de configuracion para conectarse a una base de datos
MySQL o MariaDB
'''
db_host = 'localhost' #nombre del servidor
db_name = 'base_yaz' #nombre de la base de datos
db_user = 'unid' #usuario
db_pw = 'unid.2018' # contrasena del usuario
db_port = 3306 #puerto

db = web.database(
    dbn='mysql',
    host=db_host,
    db=db_name,
    user=db_user,
    pw=db_pw,
    port = db_port
    )

'''
Metodo para seleccionar todos los registros de la tabla datos
'''
def select_datos():
    try:
        return db.select('datos')
    except Exception as e:
        print "Model select_datos Error {}".format(e.args)
        print "Model select_datos Message {}".format(e.message)
        return None

'''
Metodo para seleccionar un registro que coincida con el email dato
'''
def select_email(email):
    try:
        return db.select('datos',where='email=$email', vars=locals())[0]
    except Exception as e:
        print "Model select_email Error {}".format(e.args)
        print "Model select_email Message {}".format(e.message)
        return None

'''
Metodo para insertar un nuevo registro usando email y password
'''
def insert_datos(email, nombre, apellidos, telefono, password):
    try:
        return db.insert('datos', email=email,nombre=nombre,apellidos=apellidos,telefono=telefono,password=password)
    except Exception as e:
        print "Model insert_datos Error {}".format(e.args)
        print "Model insert_datos Message {}".format(e.message)
        return None

'''
Metodo para eliminar un registro que coincida con el email dato
'''
def delete_datos(email):
    try:
        return db.delete('datos', where='email=$email',vars=locals())
    except Exception as e:
        print "Model delete_datos Error {}".format(e.args)
        print "Model delete_datos Message {}".format(e.message)
        return None

'''
Metodo para actualizar el email y el password
'''
def update_datos(email, nombre, apellidos, telefono, password):
    try:
        return db.update('datos', 
            email=email,
            nombre=nombre,
            apellidos=apellidos,
            telefono=telefono,
            password=password, 
            where='email=$email',
            vars=locals())
    except Exception as e:
        print "Model update_datos Error {}".format(e.args)
        print "Model update_datos Message {}".format(e.message)
        return None
