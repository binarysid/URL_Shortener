import app.engine as engine
from app.model import URLShortner
from database import database as db_instance
from sqlalchemy.exc import IntegrityError
import app.error_message as error_message
from app.request_parser import RequestParser

get_req_parser = RequestParser(arg='url',type=str,location='args').getParser()
post_req_parser = RequestParser(arg='url',type=str,location='form').getParser()

def create_short_url(url,base_url):
    url_model = URLShortner(original_url=url)
    try:
        db_instance.commit(url_model)
        short_url = engine.convert_to_shortURL(base_url=base_url,id=url_model.id)
        return {'short_url': short_url}
    except IntegrityError as error:
        return {'message':error_message.DUPLICATE_VALUE}

def get_original_url(short_url,base_url):
    try:
        id = engine.restore_id_from_URL(base_url=base_url,shortenedURL=short_url)
        services = URLShortner.query.filter_by(id=id).first()
        return {'url': services.original_url}
    except IntegrityError as error:
        return {'message': error}
    except:
        return {'message': error_message.GENERIC_MSSG}