import requests
from ..objects.obj_computer import Computer
from ..endpoint_parent import Endpoint

class ClassicComputers(Endpoint):
    """TO DO""" # // TODO
    def get_all(self) -> (requests.Response, list):
        """Gets all computers from parent API obj"""
        suffix = "/computers/subset/basic"
        url = self._api.url() + suffix
        headers = self._api.header("basic")
        req = requests.Request("GET", url=url, headers=headers)
        call = self._api.do(req)
        if call.ok:
            out = []
            for comp in call.json()["computers"]:
                out.append(Computer(
                    self._api.tenant,
                    comp["serial_number"],
                    comp["id"],
                    comp
                ))

            return (call, out)

        return (call, None)
