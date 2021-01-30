import flask
from Database import Database
from Product import Product

app = flask.Flask(__name__)
db = Database()

"""
Possible requests:
GET     /product/<product_id>
POST    /product/
PUT     /product/<product_id>
PATCH   /product/<product_id>
DELETE  /product/<product_id>

Automatic:
OPTIONS /product
OPTIONS /product/<product_id>

Not fully implemented:
HEAD
"""


@app.route("/product/<product_id>", methods=["GET"])
def get_product(product_id):
    # returns product by id
    index = int(product_id)
    product = db.get(index)
    if product is not None:
        return flask.jsonify(product.serialize())
    else:
        return flask.Response(status=404)


@app.route("/product", methods=["POST"])
def post_product():
    # adds new product, returns product id
    name = flask.request.form["name"]
    manufacturer = flask.request.form["manufacturer"]
    price = flask.request.form["price"]
    product = Product(name, price, manufacturer)
    product_id = db.add(product)
    return flask.Response('{"product_id":' + str(product_id) + '}', status=201, mimetype='application/json')


@app.route("/product/<product_id>", methods=["PUT"])
def put_product(product_id):
    # create or replace product by id
    name = flask.request.form["name"]
    manufacturer = flask.request.form["manufacturer"]
    price = flask.request.form["price"]
    index = int(product_id)
    product = Product(name, price, manufacturer)
    new_index = db.create_or_replace(product, index)
    return flask.Response('{"product_id":' + str(new_index) + '}', status=201, mimetype='application/json')


@app.route("/product/<product_id>", methods=["PATCH"])
def patch_product(product_id):
    # modifies product by id
    name = flask.request.form.get("name", None)
    manufacturer = flask.request.form.get("manufacturer", None)
    price = flask.request.form.get("price", None)
    index = int(product_id)

    if db.modify(name, price, manufacturer, index):
        return flask.Response(status=200)
    else:
        return flask.Response(status=404)


@app.route("/product/<product_id>", methods=["DELETE"])
def delete_product(product_id):
    # delete product by id
    index = int(product_id)
    if db.remove(index):
        return flask.Response(status=200)
    else:
        return flask.Response(status=404)


if __name__ == "__main__":
    app.run(host='0.0.0.0')
