from clickup_cli.tasks import fetch_user_tasks


def test_fetch_user_tasks(mocker):
    mock_response = {
        "tasks": [
            {
                "id": "123",
                "name": "Mock Task 1",
                "status": {"status": "in progress"},
                "url": "https://app.clickup.com/t/123",
                "due_date": "1738317600000",
            },
            {
                "id": "456",
                "name": "Mock Task 2",
                "status": {"status": "planned"},
                "url": "https://app.clickup.com/t/456",
                "due_date": "1738417600000",
            },
        ],
        "last_page": True,
    }

    mocker.patch("clickup_cli.tasks.make_request", return_value=mock_response)

    tasks = fetch_user_tasks()
    assert len(tasks) == 2
    assert tasks[0]["name"] == "Mock Task 1"
    assert tasks[1]["name"] == "Mock Task 2"
