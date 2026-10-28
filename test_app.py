
from app import app


def test_health_check():
    client = app.test_client()

    response = client.get("/health")

    assert response.status_code == 200
    assert response.get_json()["status"] == "healthy"
    assert response.get_json()["service"] == "task-tracker-api"


def test_get_tasks():
    client = app.test_client()

    response = client.get("/tasks")

    assert response.status_code == 200
    assert response.get_json()["tasks"] == []
    assert response.get_json()["count"] == 0


def test_create_task():
    client = app.test_client()

    response = client.post(
        "/tasks",
        json={"title": "Learn Docker"}
    )

    assert response.status_code == 201
    assert response.get_json()["task"]["title"] == "Learn Docker"
    assert response.get_json()["task"]["completed"] is False
