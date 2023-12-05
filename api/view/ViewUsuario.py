from flask import Flask, request
from flask_cors import CORS
from flask_swagger_ui import get_swaggerui_blueprint
from controller.UsuarioController import UsuarioController
from model.Usuario import Usuario


app = Flask(__name__)
CORS(app)

SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'
SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "API usuario"
    }
)

app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)

@app.route("/")
def api_usuario_saudavel():
    return "API-Usuario saudavel"

@app.route("/api/v1/criar-usuario", methods = ["POST"])
def criar_usuario():
    usuario_request = request.json

    usuario_a_ser_criado = Usuario(usuario_request["nome"], usuario_request["sobrenome"], usuario_request["email"], usuario_request["senha"], usuario_request["data_de_nascimento"], usuario_request["cpf"], None)

    usuario_criado = UsuarioController.criar_usuario(usuario_a_ser_criado)

    if usuario_criado:

        return "Usuario criado com sucesso", 201

    else:

        return 500


@app.route("/api/v1/alterar-senha-usuario", methods = ["PUT"])
def alterar_senha_usuario():
    usuario_request = request.json

    senha_usuario_atualizado = UsuarioController.alterar_senha_usuario(usuario_request["senha"], request.args.get("cpf"))

    if senha_usuario_atualizado:
        return "Senha do usuário alterada com sucesso", 202
    else:
        return 500
    
@app.route("/api/v1/detalhar-usuario")
def detalhar_usuario():

    usuario_detalhado = UsuarioController.detalhar_usuario(request.args.get("email"))

    if usuario_detalhado is not None:
        return usuario_detalhado, 200
    else:
        return 500

@app.route("/api/v1/editar-usuario", methods = ["PUT"])
def editar_usuario():
    usuario_request = request.json

    usuario_a_ser_editado = Usuario(usuario_request["nome"], usuario_request["sobrenome"], usuario_request["email"], None, usuario_request["data_de_nascimento"], usuario_request["cpf"], None)

    usuario_editado = UsuarioController.editar_usuario(usuario_a_ser_editado)

    if usuario_editado:
        return "Usuario alterado com sucesso", 202

    else:
        return 500


@app.route("/api/v1/listar-usuarios")
def listar_usuarios():

    usuarios_listados = UsuarioController.listar_usuarios()

    return usuarios_listados, 200


def view_usuario():
    app.run(host="0.0.0.0", port=5000)
