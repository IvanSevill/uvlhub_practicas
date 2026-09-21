"""HTTP integration tests for the notepad feature.

Drive the application through the Flask test client. The module-scoped
``test_client`` fixture initializes a clean database once for this module.
"""
import pytest

pytestmark = pytest.mark.integration


def test_notepad_index_responds(test_client):
    test_client.post("/login", data=dict(email="test@example.com", password="test1234"), follow_redirects=True)

    response = test_client.get("/notepad")

    assert response.status_code == 200, "/notepad did not return 200"
    test_client.get("/logout", follow_redirects=True)
