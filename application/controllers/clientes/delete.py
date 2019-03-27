import config

class Delete:
    
    def __init__(self):
        pass

    def GET(self, id_cliente):
        cliente = config.form_cliente()
        result = config.model.get_cliente(id_cliente)
        cliente.fill(result)
        return config.render.delete(cliente)

    def POST(self, id_cliente):
        config.model.delete_cliente(id_cliente)
        raise config.web.seeother('/')
