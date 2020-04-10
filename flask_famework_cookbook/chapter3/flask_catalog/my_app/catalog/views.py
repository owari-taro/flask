from flask import request, jsonify, Blueprint
from my_app.catalog.models import Product, Category
from my_app import db

catalog = Blueprint("catalog", __name__)


@catalog.route("/")
@catalog.route("/home")
def home():
    return "welcome to the catalog home"


@catalog.route("/product/<id>")
def product(id):
    product = Product.query.get_or_404(id)
    return f"Product{product.name} {product.price}"


@catalog.route("/products")
def products():
    products = Product.query.all()
    res = {}
    for product in products:
        res[product.id] = {"name": product.name,
                           "price": str(product.price),
                           "category": products.category.name
                           }
    return jsonify(res)


@catalog.route("/product-create", methods=["POST"])
def create_product():
    # extract data from post request
    name = request.form.get("name")
    price = request.form.get("price")
    categ_name = request.form.get("category")
    category = Category.query.filter_by(name=categ_name).first()
    if not category:
        category = Category(categ_name)
    product = Product(name, price, category)
    db.session.add(product)
    db.session.commit()
    return "product created"


@catalog.route("/category-create", methods=["POST"])
def create_category():
    name = request.form.get("namer")
    category = Category(name)
    db.session.add(category)
    db.session.commit()
    return "category created"


@catalog.route("/categories")
def categories():
    categories = Category.query.all()
    res = {}
    for category in categories:
        res[category.id] = {"name": category.name}
        for product in category.products:
            #TODO:is this bug?,value must be list of dictionary?
            res[category.id]["products"] = {
                "id": product.id, "name": product.name, "price": product.price}
    return jsonify(res)
