import click, json, uuid, datetime
from pathlib import Path
from util import get_data_from_json, write_data_to_json, print_task
from enum import Enum

class ListArguments(Enum):
    DONE = "done"
    IN_PROGRESS = "in-progress"
    TODO = "todo"
    ALL = "all"


@click.group()
@click.version_option()
def cli():
    """Task Tracker
    
    This is a simple implementation of a task tracker.
    It'll help you track and manage your tasks
    """


@cli.command("list")
@click.argument("status", default=ListArguments.ALL, type=ListArguments)
def list(status):
    """List all tasks\n
    Status:\n
        done - list all tasks marked with 'done' status\n
        todo - list all tasks marked with 'todo' status\n
        in-progress - list all tasks marked with 'in-progress' status\n
    """

    file_data = get_data_from_json("tasks.json")

    if status == ListArguments.ALL:
        count = 0
        for task in file_data["tasks"]:
            count += 1
            print_task(task)
        if count == 0:
            click.echo("(empty set)")

    elif status == ListArguments.DONE:
        count = 0
        for task in file_data["tasks"]:
            if task['status'] == 'done':
                count += 1
                print_task(task)
        if count == 0:
            click.echo("(empty set)")
    elif status == ListArguments.IN_PROGRESS:
        count = 0
        for task in file_data["tasks"]:
            if task['status'] == 'in-progress':
                count += 1
                print_task(task)
        if count == 0:
            click.echo("(empty set)")
    elif status == ListArguments.TODO:
        count = 0
        for task in file_data["tasks"]:
            if task['status'] == 'TODO':
                count += 1
                print_task(task)
        if count == 0:
            click.echo("(empty set)")
    else:
        click.echo(click.style("Bad argument has been recieved, try again!", fg="red")) 

@cli.command("add")
@click.argument("name", type=str)
def add(name):
    """Add a new task"""

    task = {
        "id": str(uuid.uuid4()),
        "description": name,
        "status": "todo",
        "createdAt": str(datetime.datetime.now()),
        "updatedAt": str(datetime.datetime.now())
    }


    file_date = get_data_from_json("tasks.json")

    file_date["tasks"].append(task)

    write_data_to_json("tasks.json", file_date)

    click.echo(f"Added a new task {name}")


@cli.command("update")
@click.argument("id", type=str)
@click.argument("name", type=str)
def update(id, name):
    """Update the task by its id"""

    file_date = get_data_from_json("tasks.json")

    for task in file_date["tasks"]:
        if (task["id"] == id):
            task["description"] = name
            task["updatedAt"] = str(datetime.datetime.now())

            write_data_to_json("tasks.json", file_date)

            click.echo(f"The task has been updated successfully!")
            return

    click.echo(f"The task has not been found by id {id}")

@cli.command("delete")
@click.argument("id",  type=str)
def delete(id):
    """Delete the task by its id"""

    
    file_date = get_data_from_json("tasks.json")

    for task in file_date["tasks"]:
        if task["id"] == id:
            file_date["tasks"].remove(task)

            write_data_to_json("tasks.json", file_date)

            click.echo("The task has been deleted successfully")
            return
            
    click.echo(f"The task has not been found by id {id}")

@cli.command("mark-in-progress")
@click.argument("id",  type=str)
def mark_in_progress(id):
    """Set the task's status to 'in progress' by id"""

    file_date = get_data_from_json("tasks.json")

    for task in file_date["tasks"]:
        if (task["id"] == id):
            task["status"] = "in-progress"
            task["updatedAt"] = str(datetime.datetime.now())
            
            write_data_to_json("tasks.json", file_date)

            click.echo(f"The task has been set to 'in-progress'")
            return
    click.echo(f"The task has not been found by id {id}")

@cli.command("mark-done")
@click.argument("id", type=str)
def mark_done(id):
    """Set the task's status to 'done' by id"""

    file_date = get_data_from_json("tasks.json")

    for task in file_date["tasks"]:
        if (task["id"] == id):
            task["status"] = "done"
            task["updatedAt"] = str(datetime.datetime.now())
            
            write_data_to_json("tasks.json", file_date)

            click.echo(f"The task has been set to 'done'")
            return
    click.echo(f"The task has not been found by id {id}")