
"""
Integration tests for the /version route.
"""
# pylint: disable=redefined-outer-name,unused-argument


def test_unset_version_route(client):
    """
    Test that the default version is unknown.
    """
    with client:
        client.application.config["APP_VERSION"] = "unknown"

        response = client.get("/version")

        assert response.status_code == 200
        assert response.data == b"unknown"


def test_real_version_route(client):
    """
    Test that the route returns the configured version.
    """
    with client:
        client.application.config["APP_VERSION"] = "11.0.0"

        response = client.get("/version")

        assert response.status_code == 200
        assert response.data == b"11.0.0"
