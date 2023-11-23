from test.unit.webapp import client

def test_landing(client):
    landing = client.get("/")
    html = landing.data.decode()
    assert "<title>Words and Paragraphs Counter</title>" in html
    assert "Words and Paragraphs" in html
    assert landing.status_code == 200

def test_landing_aliases(client):
    landing = client.get("/")
    assert client.get("/count/").data != landing.data
