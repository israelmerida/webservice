import web

print"conectando"
db = web.database(
    dbn='mysql', # motor de base de datos
    host='localhost', # ruta del servidor
    db='ferreteria_iml', # nombre de la base de datos
    user='root', # usuario dela base de datos
    pw='1234', # password del usuario
    port = 3306 # puerto de mariadb
    )
print"conectado"