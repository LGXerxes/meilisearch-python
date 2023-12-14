# pylint: disable=invalid-name

import meilisearch
from tests import BASE_URL, MASTER_KEY


def test_get_client():
    """Tests getting a client instance."""
    client = meilisearch.Client(BASE_URL, MASTER_KEY)
    assert client.config
    response = client.health()
    assert response["status"] == "available"


def test_client_timeout_set():
    timeout = 5
    client = meilisearch.Client(BASE_URL, MASTER_KEY, timeout=timeout)
    response = client.health()
    assert client.config.timeout == timeout
    assert response["status"] == "available"


def test_client_timeout_not_set():
    client = meilisearch.Client(BASE_URL, MASTER_KEY)
    response = client.health()
    assert client.config.timeout is None
    assert response["status"] == "available"
