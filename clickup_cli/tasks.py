from clickup_cli.api import make_request
from clickup_cli.config import get_config
from clickup_cli.utils import format_date
from colorama import Fore, Style

from colorama import Fore, Style


def fetch_user_tasks(status_filter=None):
    """
    Fetch and display tasks assigned to the authorized user with a detailed format.
    By default, show only 'in progress' and 'planned' tasks unless specific statuses are provided.
    """
    config = get_config()

    page = 0
    all_tasks = []
    while True:
        response = make_request(
            f"team/{config['CLICKUP_TEAM_ID']}/task",
            params={
                "assignees[]": [config["CLICKUP_USER_ID"]],
                "include_closed": False,
                "subtasks": True,
                "page": page,
            },
        )

        if not response or "tasks" not in response:
            print(f"{Fore.RED}No tasks found or error fetching tasks.{Style.RESET_ALL}")
            break

        tasks = response["tasks"]

        if status_filter:
            filtered_tasks = [
                task
                for task in tasks
                if task["status"]["status"].lower()
                in [s.lower() for s in status_filter]
            ]
        else:
            filtered_tasks = [
                task
                for task in tasks
                if task["status"]["status"].lower() in ["in progress", "planned"]
            ]

        all_tasks.extend(filtered_tasks)

        if response.get("last_page", True):
            break

        page += 1

    if all_tasks:
        print(
            f"\n{Fore.GREEN}Found {len(all_tasks)} tasks assigned to you:{Style.RESET_ALL}\n"
        )
        for task in all_tasks:
            status_color = (
                Fore.BLUE
                if task["status"]["status"].lower() == "planned"
                else Fore.GREEN
            )
            print(
                f"- {status_color}[{task['status']['status']}] {Fore.YELLOW}{task['name']} (ID: {task['id']}){Style.RESET_ALL}"
            )
            print(f"  {Fore.MAGENTA}URL: {task['url']}{Style.RESET_ALL}")
            print(
                f"  {Fore.CYAN}Due Date: {format_date(task.get('due_date'))}{Style.RESET_ALL}\n"
            )
    else:
        print(f"{Fore.RED}No tasks found with the specified criteria.{Style.RESET_ALL}")

    return all_tasks
