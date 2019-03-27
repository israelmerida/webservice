import config

class Insert:

    def __init__(self):
        pass

    def GET(self):
        clientes = config.form_cliente()
        return config.render.insert(clientes)

    def POST(self):
        clientes = config.form_cliente()
        if clientes.validates():
            config.model.insert_cliente(**clientes.d)
            raise config.web.seeother('/')
        else:
            return config.render.insert(clientes)
