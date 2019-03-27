import web

print"conectando"
db = web.database(
    dbn='mysql', # motor de base de datos
    host='cig4l2op6r0fxymw.cbetxkdyhwsb.us-east-1.rds.amazonaws.com', # ruta del servidor
    db='x5mr0c1om4knotua', # nombre de la base de datos
    user='zpj10ffxpxk38w9b', # usuario dela base de datos
    pw='zm314m31xnd3pzua', # password del usuario
    port = 3306 # puerto de mariadb
    )
print"conectado"