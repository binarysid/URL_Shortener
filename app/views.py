from flask import  Blueprint, request
import app.controller as controller
from flask_restx import Resource, Api

view_blue_print = Blueprint('controller', __name__)
api = Api(view_blue_print)

@api.route('/geturl/')
class FetchOriginalURL(Resource):
    @api.doc(parser=controller.get_req_parser)
    def get(self):
        args = controller.get_req_parser.parse_args()
        url = args['url']
        return controller.get_original_url(short_url=url,base_url=request.url_root)

@api.route('/generate-short-url/')
class GenerateShortURL(Resource):
    @api.doc(parser=controller.post_req_parser)
    def post(self):
        args = controller.post_req_parser.parse_args()
        url = args['url']
        return controller.create_short_url(url=url,base_url=request.url_root)
