import app as svc

def test_healthz():
    c = svc.app.test_client()
    r = c.get("/healthz")
    assert r.status_code == 200
