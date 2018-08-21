from flask import Blueprint,jsonify
from app.libs.redprint import Redprint
from app.libs.token_auth import auth
from app.models.user import User

#blueprint
# user = Blueprint('user',__name__)user

api = Redprint('user')


@api.route('/<int:uid>',methods=['GET'])
@auth.login_required
def get_user(uid):
    #token 是否合法 是否过期
    user = User.query.get_or_404(uid)
    return jsonify(user)

@api.route('/create')
def create_user():
    pass

