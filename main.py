import cli
from get_tasks import get_tasks
from create_db import create_db
from update_task import update_task

@cli.app()
def main(action = "show"):
    if action == "show":
        get_tasks()
    elif action == "create":
        create_db()
    elif action == "update":
        update_task()

main.run()