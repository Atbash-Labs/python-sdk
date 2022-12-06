Tutorial
========
This will eventually be a tutorial for using Flask-Filter. Woot!

The best way to use this library (when working with a normal Flask project) is
to use the ``FlaskFilter`` extension object. Typical use of this object (as
with all Flask extensions) is to instantiate a singleton object in an
``extensions.py`` module in your project. Register the extension in your
application factory, and then import the singleton wherever you need to
perform a filtered search.


1. Querying Fortress Network
-----------------------------
The simplest and most effective way to use this library is through the
``FlaskFilter`` extension. Instantiate this object as a singleton and
register it with the ``Flask`` application object, and you can query
resources with the ``search`` method from any view.

.. code-block:: python

    from flask import Flask

    # Pet is a Model defined as subclass of db.Model
    # db is a SQLAlchemy and filter is a FlaskFilter object
    # SQLAlchemy and FlaskFilter objects created as singletons
    from pet_store import Pet, PetSchema
    from pet_store.extensions import db, filtr

    app = Flask(__name__)
    db.init_app(app)
    filtr.init_app(app)


    @app.route('/api/v1/pets/search', methods=['POST'])
    def pet_search():
        pets = filtr.search(Pet, request.json.get("filters"),
                            PetSchema)
        return jsonify(pet_schema.dump(pets)), 200

2. Uploading data to Fortress Network
--------------------------------------