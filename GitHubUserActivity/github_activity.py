import click
import requests
import enum
import datetime

class NotFoundUsername(Exception):
    pass

@click.command()
@click.argument("username", type=str)
def cli(username):
    """
    This is a simple command line interface to fetch the recent activity of a GitHub
    """

    url = f"https://api.github.com/users/{username}/events"


    response = None
    count = 10
    try:
        with click.progressbar(label="Fetching your GitHub information",
                           length=10,
                           show_eta=False) as progress_bar:
            with requests.get(url) as response:
                progress_bar.update(count)
                count += 10
        if response.status_code == 404:
            raise NotFoundUsername
    except NotFoundUsername:
        click.echo("Sorry, but I could not find the given username, try another one")
        return


    event = response.json()[0]

    repositories = {}
    for event in response.json():
        repo_name = event["repo"]["name"]
        event_type = event["type"]

        repositories[repo_name] = repositories.setdefault(repo_name, {})

        if event_type == "PushEvent":
            repositories[repo_name][event_type] = repositories[repo_name].setdefault(event_type, 0) + len(event["payload"]["commits"])
        elif event_type == "WatchEvent":
            if event_type in repositories[repo_name]:
                curr = repositories[repo_name][event_type]
                curr.append(event["payload"]["action"])
                repositories[repo_name][event_type] = curr
            else:
                repositories[repo_name][event_type] = [event["payload"]["action"]]
        elif event_type == "PullRequestEvent":
            if event_type in repositories[repo_name]:
                curr = repositories[repo_name][event_type]
                curr.append(event["payload"]["action"])
                repositories[repo_name][event_type] = curr
            else:
                repositories[repo_name][event_type] = [event["payload"]["action"]]
        

    for key, val in repositories.items():
        for v in val.keys():
            if v == "PushEvent":
                click.secho(f"Push Events (fro {key} repository):", bold=True)
                click.echo(f"\t- Pushed {val[v]} commits")
            elif v == "WatchEvent":
                click.secho(f"Watch Events (for {key} repository):", bold=True)
                for we in val[v]:
                    click.echo(f"\t- Watch event was performed with {we} action")
            elif v == "PullRequestEvent":
                click.secho(f"Pull Request Events (for {key} repository):", bold=True)
                for we in val[v]:
                    click.echo(f"\t- Pull request event was performed with {we} action")
