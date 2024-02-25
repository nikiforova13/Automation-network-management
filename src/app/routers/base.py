from flask import Blueprint, request, render_template

# from flask_restx import Api, namespace, Namespace, Resource
from config.driver import BaseNetworkDriverSettings
from scrapli import Scrapli
from config.driver import driver

router = Blueprint("configurations", __name__, "templates")


# @router.before_request
# def connect_to_device():
@router.get("/")
def index():
    return render_template("index.html")


@router.get("/get_config")
def get_current_device_configuration():
    print('request')
    print(request)
    print(request.data)
    if request:
        with Scrapli(
                **driver.get_settings
        ) as ssh:
            a = ssh.send_command("show run")
            return a.result
    return render_template("index.html")


from pydantic import BaseModel


class Interface(BaseModel):
    interface: str
    ip_address: str
    method: str
    ok: str
    protocol: str
    status: str


class InterfacesInfo(BaseModel):
    interfaces: list[Interface]


@router.get("/interfaces")
def get_all_available_interfaces():
    if request:
        with Scrapli(
                **driver.get_settings
        ) as ssh:
            import pathlib
            APP_GLOBAL_PATH = pathlib.Path(__file__).absolute().parent.parent.joinpath('templates').joinpath('ex1')
            print(APP_GLOBAL_PATH)

            a = ssh.send_command("show ip interface brief")
            print(a.result)

            # print(b1)
            b = a.ttp_parse_output(str(APP_GLOBAL_PATH))
            print(b)
            print(InterfacesInfo(**b[0]).interfaces)
            return render_template("interfaces.html", int=InterfacesInfo(**b[0]).interfaces)
    return render_template("index.html")
