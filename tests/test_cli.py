from click.testing import CliRunner
from clickup_cli.cli import cli
import re


def test_view_tasks_command(mocker):
    mock_response = {
        "tasks": [
            {
                "id": "123",
                "name": "Mock Task 1",
                "status": {"status": "in progress"},
                "url": "https://app.clickup.com/t/123",
                "due_date": "1738317600000",
            }
        ],
        "last_page": True,
    }

    mocker.patch("clickup_cli.tasks.make_request", return_value=mock_response)

    runner = CliRunner()
    result = runner.invoke(cli, ["tasks", "view"])

    def strip_ansi_codes(text):
        ansi_escape = re.compile(r"\x1b\[([0-9;]*[a-zA-Z])")
        return ansi_escape.sub("", text)

    output = strip_ansi_codes(result.output)

    assert result.exit_code == 0, f"Unexpected exit code: {result.exit_code}"
    assert "Found 1 tasks assigned to you" in output
    assert "Mock Task 1" in output
    assert "https://app.clickup.com/t/123" in output
    assert "[in progress]" in output
