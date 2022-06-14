def test_add_batch_returns_201(client):
    response = client.post(
        '/products/add_batch',
        json={
            'reference': 'batch_1',
            'sku': 'TABLE',
            'quantity': 100,
        },
    )
    assert 201 == response.status_code

    products = client.get('/products').json['products']
    assert 'TABLE' in [d['sku'] for d in products]

def test_add_batch_returns_400(client):
    response = client.post(
        '/products/add_batch',
        json={
            'reference': 'batch_1',
            'quantity': 100,
        },
    )
    assert 400 == response.status_code

    response = client.post(
        '/products/add_batch',
        json={
            'reference': 'batch_1',
            'sku': 'CHAIR',
            'quantity': 'str',
        },
    )
    assert 400 == response.status_code


def test_products(client):
    client.post(
        '/products/add_batch',
        json={
            'reference': 'batch_1',
            'sku': 'CHAIR',
            'quantity': 100,
        },
    )
    client.post(
        '/products/add_batch',
        json={
            'reference': 'batch_2',
            'sku': 'CHAIR',
            'quantity': 100,
        },
    )

    response = client.get("/products")
    assert response.status_code == 200
    assert "products" in response.json
    assert 2 == len(response.json["products"])
    assert "TABLE" in [d["sku"] for d in response.json["products"]]
    assert "CHAIR" in [d["sku"] for d in response.json["products"]]

