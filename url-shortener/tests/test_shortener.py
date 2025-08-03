def test_health(client):
    resp = client.get("/")
    assert resp.status_code == 200

def test_shorten_and_redirect(client):
    # Shorten URL
    resp = client.post("/api/shorten", json={"url": "https://example.com"})
    assert resp.status_code == 201
    data = resp.get_json()
    code = data["short_code"]

    # Get stats
    stats_resp = client.get(f"/api/stats/{code}")
    assert stats_resp.status_code == 200
