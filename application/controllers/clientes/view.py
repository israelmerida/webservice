import config

class View:

    def __init__(self):
        pass

    def GET(self, id_cliente):
        result = config.model.get_cliente(id_cliente)
        return config.render.view(result)
