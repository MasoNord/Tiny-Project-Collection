# Git Hub User Activity
A simple implementation of a command line interface to fetch the recent activity of a GitHub user and display it in the terminal

# Dependencies
- Click
- Python
- Json
- Request

# Features
- Fetch the recent activity of the specified GitHub user (push events, pull request events, watch events)
- Display the fetched activity in the terminal
- Error handling

# How to Run
1. Clone the main repostory
```
git clone https://github.com/MasoNord/Tiny-Project-Collection/tree/main
```
2. Navigate to the project folder
```
cd GitHubUserActivity
```
3. Create a virtual environment
```
python -m venv venv
```
4. Activate the environment
```
./venv/Scripts/activate
```
5. Pack entry point
```
pip install -e .
```
6. Create a task.json file to keep your tasks
7. Run the app
```
task-cli
```

# Why is this project useful
- Gain some experience of working with click library for creating iteractive command line interfaces
- Try to use a python request library for working with http  
- Practice working with json files 
- Practice doing exception handling in an application using python programming language

# Source of Inspiration
- [roadmap.sh](https://roadmap.sh/projects/github-user-activity)