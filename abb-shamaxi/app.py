from flask import Flask
from flask_admin import Admin

app = Flask(__name__)
admin = Admin(app)

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:@localhost:3306/abb_bank"
app.config['SECRET_KEY'] = "abbbank"

from controllers import *
from extensions import *
from models import *

if __name__ == "__main__":
    app.run(port=5000, debug=True)
    db.init_app(migrate)
    db.init_app(app)