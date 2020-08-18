from flask import Blueprint

bp = Blueprint('user', __name__, url_prefix='/user')

@bp.route('/', methods=['GET'])
def get_user():
    return 'user'