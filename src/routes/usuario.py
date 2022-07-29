from flask import Blueprint, request, jsonify, make_response

UsuarioRoute = Blueprint('usuario', __name__)

@UsuarioRoute.route('/', methods=['GET', 'POST'])
def usuario():
    if request.method == 'GET':
        return jsonify({'usuario': 'usuario'})
    elif request.method == 'POST':
        return jsonify({'usuario': 'usuario'})
    else:
        return make_response(jsonify({'error': 'Method not allowed'}), 405)

@UsuarioRoute.route('/usuario/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def usuario_id(id):
    if request.method == 'GET':
        return jsonify({'usuario': 'usuario'})
    elif request.method == 'PUT':
        return jsonify({'usuario': 'usuario'})
    elif request.method == 'DELETE':
        return jsonify({'usuario': 'usuario'})
    else:
        return make_response(jsonify({'error': 'Method not allowed'}), 405)

