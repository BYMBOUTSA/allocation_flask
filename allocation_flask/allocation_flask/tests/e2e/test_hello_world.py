def test_hello_world(client):
    response = client.get('/')
    assert 200 == response.status_code
    assert 'Hello, World!' == response.data.decode('utf8')