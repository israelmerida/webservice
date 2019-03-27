import web
from web import form
import application.models.model_cliente

render = web.template.render('application/views/clientes/', base='master')
model = application.models.model_cliente

vemail = form.regexp(r".*@.*", "Must be a valid email address")
'''
Here we define the form fields for use in all the views
'''
form_cliente = form.Form(
            form.Hidden('id_cliente',description="", value="0", class_="form-control", required=True),
            form.Textbox('nombre',description="nombre", class_="form-control", required=True),
            form.Textbox('apellido_paterno',description="apellido_paterno", class_="form-control", required=True),
            form.Textbox('apellido_materno',description="apellido_materno", class_="form-control", required=True),
            form.Textbox('telefono',description="telefono", class_="form-control", required=True),
            form.Textbox('email', vemail, description="Email", class_="form-control", required=True),
        )
        