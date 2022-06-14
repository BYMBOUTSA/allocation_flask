from flask import Flask, request
from allocation.domain_model import Product

from allocation.repository import Repository
from . import services

app = Flask(__name__)

repository = Repository(products=[])

@app.route('/', methods=['GET'])
def hello_world():
    return '<h1>Hello, World!</h1>'

@app.route('/products', methods=['GET'])
def list_products():
    return {
        'products': [
            {
                'sku': p.sku,
                 'batches': [
                    {
                        'reference': batch.reference,
                        'purchased_quantity': batch.purchased_quantity,
                        'available_quantity': batch.available_quantity
                    } for batch in p.batches
                ],
            } for p in services.list_products(repository)
        ]
    }

@app.route('/products/add_batch', methods=['POST'])
def add_batch():
    try:
        reference = request.json['reference']
        sku = request.json['sku']
        quantity = int(request.json['quantity'])
        eta = request.json.get('eta')
        services.add_batch(
            reference=reference,
            sku=sku,
            quantity=quantity,
            eta=eta,
            repository=repository
        )
        return 'OK', 201
    except (KeyError, ValueError):
        return 'Missing parameter', 400







