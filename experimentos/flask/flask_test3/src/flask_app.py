from app_core import app, database, module_loader, wireup_cotainer
from app_core import security


database.init(app)
module_loader.init(app)
database.create_all(app)

wireup_cotainer.init(app)

#Si no se ejecuta aqui security interfiere con wireup
security.init()

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)