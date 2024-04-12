# [PyCon Africa](https://pycon.africa/)

    This is the source code for the https://pycon.africa/ website.

Sure! To incorporate the use of `virtualenvwrapper` specifically into the installation instructions for Python 3.11.0 and Django 5.0.2, we'll focus on the `mkvirtualenv` command for creating a virtual environment. Here's the updated guide including the `virtualenvwrapper` style for creating a virtual environment:

# Running the site locally

## Requirements


* [Python 3.11.9](https://python.org)
* [Poetry](https://python-poetry.org/)



```
# install dependencies using poetry 

poetry install 

# now open a shell. This is equivalent to activating a virtual environment

poetry shell

# once your shell is active you can use this command to set up your development database

python manage.py migrate 

# then you can use this command to run the application

python manage.py runserver
```

## Installation

1. **Clone or Fork the Repository**: Follow the guide on [GitHub Help - Fork a Repo](https://help.github.com/articles/fork-a-repo) to understand how to clone or fork a repo.

2. **Set Up Virtualenvwrapper**: If you haven't already installed `virtualenvwrapper`, you can do so by following the installation instructions on their [official documentation](https://virtualenvwrapper.readthedocs.io). Ensure it's properly configured to work with your shell.

3. **Create and Activate a Virtual Environment**: Using `virtualenvwrapper`, you will create a new virtual environment specifically for the project. Replace `env1` with a name relevant to your project, like `pyconafrica_env`:

   ```
   mkvirtualenv pyconafrica_env --python=/usr/bin/python3.11
   ```

   This command creates a new virtual environment named `pyconafrica_env` using Python 3.11.0. Once created, `virtualenvwrapper` automatically activates the virtual environment.

4. **Install Dependencies**: Ensure your `requirements.txt` file includes `Django==5.0.2` and any other necessary packages. Install them using `pip`:

   ```
   (pyconafrica_env) $ pip install -r requirements.txt
   ```

5. **Database Setup and Server Launch**: Execute the following Django management commands to set up your database and start the development server:

   ```
   (pyconafrica_env) $ python manage.py migrate
   (pyconafrica_env) $ python manage.py makemigrations
   (pyconafrica_env) $ python manage.py runserver
   ```

6. **Access the Site**: After the server starts, copy the IP address provided (typically something like "Serving at 127.0.0.1:8000") and paste it into your web browser to view the site.

`Note`: It's important to avoid creating your virtual environment in the same directory as your project code. `virtualenvwrapper` stores environments in a separate location by default, which helps avoid this issue.

# Contributing

Interested in contributing? Please read our [Contributing Guide](./CONTRIBUTING.md) for guidelines on how to contribute effectively.

This guide now includes the use of `virtualenvwrapper` for managing your Python virtual environments, providing a clean and efficient workflow for Python development, especially with specific versions like Python 3.11.0 and Django 5.0.2.