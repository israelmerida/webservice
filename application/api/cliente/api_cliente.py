import web
import config
import json

class Api_cliente:

    def __init__(self):
        pass
        
    def get(self, id_cliente):
        try:
            # http://0.0.0.0:8080/api_persons?user_hash=12345&action=get
            if id_cliente == None:
                result = config.model.get_all_cliente()
                clientes_json = []
                for row in result:
                    tmp = dict(row)
                    clientes_json.append(tmp)
                web.header('Content-Type', 'application/json')
                return json.dumps(clientes_json)
            else:
                # http://0.0.0.0:8080/api_persons?user_hash=12345&action=get&id_person=1
                result = config.model.get_cliente(int(id_cliente))
                clientes_json = []
                clientes_json.append(dict(result))
                web.header('Content-Type', 'application/json')
                return json.dumps(clientes_json)
        except Exception as e:
            print "GET Error {}".format(e.args)
            clientes_json = '[]'
            web.header('Content-Type', 'application/json')
            return json.dumps(clientes_json)

# https://0.0.0.0:8080/api_persons?user_hash=12345&action=put&id_person=1&name=new&telephone=12345&email=new@email.com
    def put(self, nombre,apellido_paterno,apellido_materno,telefono,email):
        try:
            config.model.insert_cliente(nombre,apellido_paterno,apellido_materno,telefono,email)
            clientes_json = '[{200}]'
            web.header('Content-Type', 'application/json')
            return json.dumps(clientes_json)
        except Exception as e:
            print "PUT Error {}".format(e.args)
            return None

# http://0.0.0.0:8080/api_persons?user_hash=12345&action=get&id_person=1
    def delete(self, id_cliente):
        try:
            config.model.delete_cliente(id_cliente)
            clientes_json = '[{200}]'
            web.header('Content-Type', 'application/json')
            return json.dumps(clientes_json)
        except Exception as e:
            
            print "DELETE Error {}".format(e.args)
            return None

# https://0.0.0.0:8080/api_persons?user_hash=12345&action=update&id_person=1&name=new&telephone=12345&email=new@email.com
    def update(self,  id_cliente,nombre, apellido_paterno,apellido_materno,telefono,email):
        try:
            config.model.update_cliente(id_cliente,nombre,apellido_paterno,apellido_materno,telefono,email)
            clientes_json = '[{200}]'
            web.header('Content-Type', 'application/json')
            return json.dumps(clientes_json)
        except Exception as e:
            print "GET Error {}".format(e.args)
            clientes_json = '[]'
            web.header('Content-Type', 'application/json')
            return json.dumps(clientes_json)

    def GET(self):
        user_data = web.input(
            user_hash=None,
            action=None,
            id_cliente=None,
            nombre=None,
            apellido_paterno=None,
            apellido_materno=None,
            telefono=None,
            email=None,
        )
        try:
            user_hash = user_data.user_hash  # user validation
            action = user_data.action  # action GET, PUT, DELETE, UPDATE
            id_cliente=user_data.id_cliente
            nombre=user_data.nombre
            apellido_paterno=user_data.apellido_paterno
            apellido_materno=user_data.apellido_materno
            telefono=user_data.telefono
            email=user_data.email
            
            #change de user_hash 
            if user_hash == '12345':  # user_hash
                if action == None:
                    raise web.seeother('/404')
                elif action == 'get':
                    return self.get(id_cliente)
                elif action == 'put':
                    return self.put(nombre,apellido_paterno,apellido_materno,telefono,email)
                elif action == 'delete':
                    return self.delete(id_cliente)
                elif action == 'update':
                    return self.update(id_cliente,nombre,apellido_paterno,apellido_materno,telefono,email)
            else:
                raise web.seeother('/404')
        except Exception as e:
            print "WEBSERVICE Error {}".format(e.args)
            raise web.seeother('/404')
