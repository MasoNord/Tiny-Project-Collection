import json
import click


def get_data_from_json(path):
    file_date = None
    with open(path, "r") as file:
        file_date = json.load(file)

    return file_date

def write_data_to_json(path, file_data):
    with open(path, "w") as file:
        file.seek(0)
        json.dump(file_data, file, indent=4)

def print_task(task):
    click.echo(click.style("id: ", bold=True) + " " + task["id"] + "\n")
    click.echo(click.style("description: ", bold=True) + " " + task["description"] + "\n")
    click.echo(click.style("status: ", bold=True) + " " + task["status"] + "\n")
    click.echo(click.style("createdAt: ", bold=True) + " " + task["createdAt"] + "\n")
    click.echo(click.style("updatedAt: ", bold=True) + " " + task["updatedAt"] + "\n\n")