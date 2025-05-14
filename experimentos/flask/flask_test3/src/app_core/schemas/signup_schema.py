from marshmallow import Schema, fields, validate

class SignupSchema(Schema):
    email = fields.String(required=True, validate=validate.Email(error="Invalid email format"))
    password = fields.String(required=True, 
        validate=[
            validate.Length(min=8, max=128, error="La contraseña debe tener entre 8 y 128 caracteres."),
            validate.Regexp(
                r"(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}",
                error="Debe contener al menos una mayúscula, una minúscula, un número y un carácter especial."
            )
        ])
    nick = fields.String(required=True, validate=validate.Length(min=6, max=30))