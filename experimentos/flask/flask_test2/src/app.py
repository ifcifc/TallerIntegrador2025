from core.app_core import app, wireup_cotainer
import core.database as database
import core.route as route


database.init(app)
route.init(app)
database.create_all(app)

wireup_cotainer.init(app)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)