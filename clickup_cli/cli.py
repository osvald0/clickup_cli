import click
from clickup_cli.tasks import fetch_user_tasks, fetch_task_details


@click.group()
def cli():
    """ClickUp CLI Tool."""
    pass


@cli.group()
def tasks():
    """Manage tasks."""
    pass


@tasks.command()
@click.argument("task_id", required=False)
@click.option(
    "--status",
    default=None,
    help="Filter tasks by a comma-separated list of statuses (e.g., 'in progress,planned').",
)
def view(task_id, status) -> None:
    """View tasks assigned to you or specific task details by id."""

    if task_id:
        try:
            task_details = fetch_task_details(task_id)

        except Exception as e:
            raise
    else:
        try:
            status_filter = [s.strip() for s in status.split(",")] if status else None
            tasks = fetch_user_tasks(status_filter=status_filter)

        except Exception as e:
            print(f"Error fetching tasks: {e}")
            raise click.ClickException("Failed to fetch tasks.")


if __name__ == "__main__":
    cli()
