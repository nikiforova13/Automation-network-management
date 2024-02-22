from flask import Blueprint, request, render_template

# from flask_restx import Api, namespace, Namespace, Resource
from config.driver import BaseNetworkDriverSettings

router = Blueprint("configurations", __name__, "templates")


# @router.before_request
# def connect_to_device():
@router.get("/")
def index():
    print(request)
    # if request.form['submit1']=="Получить конфигурацию устройства":
    # redirect('get_current_device_configuration')
    # print(request.form)        print(';sdlkfjdkf')
    return render_template("index.html")


@router.get("/get_config")
def get_current_device_configuration():
    print(request.form)
    print(request)
    if request:
        with BaseNetworkDriverSettings(
            host="192.168.226.132",
            auth_username="cisco",
            auth_password="cisco",
            auth_secondary="cisco",
            auth_strict_key=False,
            transport="paramiko",
            platform="cisco_iosxe",
        ) as ssh:
            a = ssh.send_command("show run")
            return a.result
    return render_template("index.html")


@router.get("/interfaces")
def get_all_available_interfaces():
    print(request.form)
    print(request)
    if request:
        # a = func()
        return True
    return render_template("index.html")
