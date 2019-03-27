import config

class Update:

    def __init__(self):
        pass

    def GET(self, id_cliente):
        clientes = config.form_cliente()
        result = config.model.get_cliente(id_cliente)
        clientes.fill(result)
        return config.render.update(clientes)

    def POST(self, id_cliente):
        clientes = config.form_cliente()
        if clientes.validates():
            config.model.update_cliente(**clientes.d)
            raise config.web.seeother('/')
        else:
            return config.render.update(clientes)
