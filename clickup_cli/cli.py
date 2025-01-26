import click
from clickup_cli.tasks import fetch_user_tasks


@click.group()
def cli():
    """ClickUp CLI Tool."""
    pass


@cli.group()
def tasks():
    """Manage tasks."""
    pass


@tasks.command()
@click.option(
    "--status",
    default=None,
    help="Filter tasks by a comma-separated list of statuses (e.g., 'in progress,planned').",
)
def view(status):
    """View tasks assigned to you."""
    status_filter = [s.strip() for s in status.split(",")] if status else None
    try:
        tasks = fetch_user_tasks(status_filter=status_filter)

    except Exception as e:
        print(f"Error fetching tasks: {e}")
        raise click.ClickException("Failed to fetch tasks.")


if __name__ == "__main__":
    cli()
