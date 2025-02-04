from clickup_cli.api import make_request
from clickup_cli.config import get_config
from clickup_cli.utils import format_date, hex_to_ansi, convert_ms_to_hm
from colorama import Fore, Style
from clickup_cli.types import Task
from typing import List


def fetch_user_tasks(status_filter=None) -> List[Task]:
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
            f"\n{Fore.MAGENTA}Found {len(all_tasks)} tasks assigned to you:{Style.RESET_ALL}\n"
        )
        for task in all_tasks:
            status_color = (
                Fore.BLUE
                if task["status"]["status"].lower() == "planned"
                else Fore.GREEN
            )
            print(
                f"{status_color}[{task['status']['status']}] {Style.RESET_ALL}{task['name']} (ID: {task['id']})"
            )
            print(f"{Fore.MAGENTA}URL: {Style.RESET_ALL}{task['url']}")
            print(
                f"{Fore.MAGENTA}Due Date: {Style.RESET_ALL}{format_date(task.get('due_date'))}\n"
            )
    else:
        print(f"{Fore.RED}No tasks found with the specified criteria.{Style.RESET_ALL}")

    return all_tasks


def fetch_task_details(task_id):
    """
    Fetch and display details for the specified task id.
    """
    config = get_config()

    response = make_request(
        f"task/{task_id}",
        params={
            "include_custom_fields": True,
            "subtasks": True,
        },
    )

    if not response:
        print(
            f"{Fore.RED}No task found or error fetching task # {task_id}.{Style.RESET_ALL}"
        )
        print(response)
        return

    print(f"\n{Fore.YELLOW}Task details for ID: {Style.RESET_ALL}{response['id']}\n")

    # print(f"  {Fore.YELLOW}ID: {Style.RESET_ALL}{response['id']}")
    print(f"{Fore.YELLOW}Status: {Style.RESET_ALL}{response['status']['status']}")
    print(f"{Fore.YELLOW}Priority: {Style.RESET_ALL}{response['priority']}")
    print(
        f"{Fore.YELLOW}Start Date: {Style.RESET_ALL}{format_date(response['start_date'])}"
    )
    print(
        f"{Fore.YELLOW}Due Date: {Style.RESET_ALL}{format_date(response['due_date'])}"
    )
    print(
        f"{Fore.YELLOW}Estimate: {Style.RESET_ALL}{convert_ms_to_hm(response['time_estimate'])}"
    )
    print(
        f"{Fore.YELLOW}Type Spent: {Style.RESET_ALL}{convert_ms_to_hm(response['time_spent'])}"
    )
    print(f"{Fore.YELLOW}Name: {Style.RESET_ALL}{response['name']}")
    print(f"{Fore.YELLOW}URL: {Style.RESET_ALL}{response['url']}")
    print(f"{Fore.YELLOW}Description: {Style.RESET_ALL}{response['description']}")

    return response
