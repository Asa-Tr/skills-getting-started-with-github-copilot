import src.app as app_module


def test_get_activities_returns_data(client):
    response = client.get("/activities")

    assert response.status_code == 200
    data = response.json()
    assert "Chess Club" in data
    assert "participants" in data["Chess Club"]


def test_delete_participant_success(client):
    activity = "Chess Club"
    email = "michael@mergington.edu"

    response = client.delete(
        f"/activities/{activity}/participants",
        params={"email": email},
    )

    assert response.status_code == 200
    refreshed = client.get("/activities").json()
    assert email not in refreshed[activity]["participants"]


def test_delete_participant_missing_activity(client):
    response = client.delete(
        "/activities/Unknown Club/participants",
        params={"email": "test@mergington.edu"},
    )

    assert response.status_code == 404


def test_delete_participant_missing_email(client):
    activity = "Chess Club"

    response = client.delete(
        f"/activities/{activity}/participants",
        params={"email": "missing@mergington.edu"},
    )

    assert response.status_code == 404
