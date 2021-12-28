import os

def start_project():
    path: str = input("Please Enter the path of your project : ")
    is_path = os.path.exists(path)
    while is_path == False:
        path: str = input("Invalid Path. Please Enter the path of your project : ")
        is_path = os.path.exists(path)
    project_name = input("What the name of the project : ")
    django_project_app = input(
        "Please Enter the name of your Django project, and Django app name (separated by comma): "
    )
    django_project_name = django_project_app.split(",")[0]
    django_app_name = django_project_app.split(",")[1]

    react_project_app_name = input(
        "Please Enter the name of frontend side project and React app name (separated by comma) : "
    )
    react_project_name = react_project_app_name.split(",")[0]
    react_app_name = react_project_app_name.split(",")[1]

    venv_name = input("Please Enter the name of your virtual environment : ")
    python_command = f"cd {path} &&  mkdir {project_name} && cd {path}\\{project_name} && django-admin startproject {django_project_name} && cd {path}\\{project_name}\\{django_project_name} && python -m venv {venv_name} && django-admin startapp {django_app_name} &&  {venv_name}\\Scripts\\activate && python -m pip install django && python -m pip install djangorestframework && python -m pip install django-cors-headers && python -m pip install django-extensions"
    js_command = f"cd {path}\\{project_name} && mkdir {react_project_name} && cd {path}\\{project_name}\\{react_project_name} && npx create-react-app {react_app_name} && npm install axios && npm install react-router-dom"
    os.system(python_command)
    os.system(js_command)
    print("Project Created Successfully")


