import os
import platform
from flask import jsonify
from flask_jwt_extended import jwt_required
from services.api import route_info
from core.database import db
import uuid

from services.api.models.api_model import ApiModel, ApiModelSchema

api_models_schema = ApiModelSchema(many=True)


@route_info.bp.route('/')
@jwt_required()
def index():

    db.session.add(ApiModel(name=str(uuid.uuid4()), description='test'))
    db.session.commit()

    query = db.session.query(ApiModel).all()

    return jsonify(api_models_schema.dump(query))

@route_info.bp.route('/hw')
@jwt_required()
def hw():
    return jsonify({
        "sistema_operativo": platform.system(),
        "version_os": platform.version(),
        "nombre_maquina": platform.node(),
        "arquitectura": platform.architecture()[0],
        "procesador": platform.processor(),
        "cpu_cores": os.cpu_count()
    })
