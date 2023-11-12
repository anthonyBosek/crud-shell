# server/app.py

from flask import Flask
from flask_migrate import Migrate

from models import db

# create a Flask application instance
app = Flask(__name__)

# configure the database connection to the local file app.db
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"

# configure flag to disable modification tracking and use less memory
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# create a Migrate object to manage schema modifications
migrate = Migrate(app, db)

# initialize the Flask application to use the database
db.init_app(app)


if __name__ == "__main__":
    app.run(port=5555, debug=True)

# Flask Shell Methods
# The Flask shell provides a few methods to interact with the database:
#
# Method	                      Description
# db.create_all()	        Creates all tables in the database
# db.drop_all()	            Drops all tables in the database
# db.session.commit()  	    Commits the current transaction
# db.session.rollback()	    Rolls back the current transaction
# db.session.add(obj)	    Adds a new object to the database
# db.session.delete(obj)	Deletes an object from the database
# db.session.merge(obj)	    Merges changes made to an object with the database
# db.session.expunge(obj)	Removes an object from the current session
# db.session.flush()	    Flushes the current session
# db.session.refresh(obj)	Refreshes the attributes of an object
# db.session.expire(obj)	Expires the attributes of an object
# db.session.scalar(query)	Returns a scalar value from a query
#
# Methods to use with Model.query
# Method	                            Description
# Model.query.all()	            Returns all objects from the database
# Model.query.first()	        Returns the first object from the database
# Model.query.get(id)	        Returns an object with the specified id
# Model.query.filter_by(attr=value)	Returns objects filtered by the specified attribute
# Model.query.order_by(attr)	Returns objects ordered by the specified attribute
# Model.query.limit(num)	    Returns a specified number of objects
# Model.query.offset(num)	    Returns objects after a specified offset
# Model.query.join(Model2)	    Returns a query with a join between two models
# Model.query.group_by(attr)	Returns a query with a group by clause
# Model.query.having(condition)	Returns a query with a having clause
# Model.query.distinct()	    Returns a query with a distinct clause
# Model.query.count()	        Returns the number of rows returned by a query
# Model.query.delete()	        Deletes rows returned by a query
