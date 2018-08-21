from flask import Blueprint
from app.libs.redprint import Redprint

#blueprint
#redprint
# book = Blueprint('book',__name__)

api = Redprint('book')

@api.route('/get',methods=['POST','GET'])
def get_book():
    return 'get book'