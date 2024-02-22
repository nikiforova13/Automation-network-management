from scrapli import Scrapli
from pydantic import Field, field_validator, ValidationError
from pydantic_settings import BaseSettings, SettingsConfigDict
from ipaddress import IPv4Address
from typing import Literal, Any
from config.base import get_updated_model_config, BASE_CONFIG


class BaseNetworkDriverSettings(BaseSettings):
    model_config = SettingsConfigDict(
        get_updated_model_config(BASE_CONFIG, SettingsConfigDict(env_prefix="device_"))
    )
    host: str
    platform: str = Literal[
        "cisco_iosxe", "arista_eos", "cisco_iosxr", "cisco_nxos", "juniper_junos"
    ]
    transport: str = Field(default="paramiko")
    auth_username: str
    auth_password: str
    auth_secondary: str
    auth_strict_key: bool

    @field_validator("host")
    @classmethod
    def check_ipaddress(cls, v: Any):
        print(cls)
        try:
            IPv4Address(v)
        except (ValidationError, ValueError):
            raise TypeError("Invalid IP address format")
        return v

    @property
    def get_settings(self):
        return self.model_dump()


a = BaseNetworkDriverSettings()
print(a)
print(a.get_settings)


class BaseNetworkDriver2(Scrapli):
    # settings: a.get_config

    def __init__(self, **kwargs):
        super().__init__(**a.get_config)

    # def get_conf_d(self):
    #     a = self.send_command('show run')
    #     print(a.result)
    #     return a.result


#
#
# with BaseNetworkDriver2(**a.get_config) as ssh2:
#     a1 = ssh2.send_command("show run")
#     print(a1)

#
#         # with Scrapli(**r1_driver) as ssh:
#         #
#         #     a = ssh.send_command('show ip interface brief')
#         #     # a = ssh.send_command('show run')
#         #     print(a)
#         #     print(a.result)
#         #     return a.result
