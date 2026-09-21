import pytest

pytestmark = pytest.mark.integration


def test_notepad_index_responds(test_client):
    test_client.post(
        "/signup/",
        data={
            "email": "notepad-test@example.com",
            "password": "1234",
            "name": "Notepad",
            "surname": "Test",
        },
        follow_redirects=True,
    )

    response = test_client.get("/notepad")

    assert response.status_code == 200, "/notepad did not return 200"
