from flask import jsonify
from flask_jwt_extended import jwt_required
from routes.api import route_info
from database import db
import uuid

from routes.api.models.api_model import ApiModel, ApiModelSchema

api_models_schema = ApiModelSchema(many=True)


@route_info.bp.route('/')
@jwt_required()
def index():

    db.session.add(ApiModel(name=str(uuid.uuid4()), description='test'))
    db.session.commit()

    query = db.session.query(ApiModel).all()

    return jsonify(api_models_schema.dump(query))