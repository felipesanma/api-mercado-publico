import logging
from collections import namedtuple

Result = namedtuple("result", ["json", "status_code"])

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)


class BaseApi:
    """
    Clase base para todos los demás módulos de subdomains
    """

    def __init__(self, config):
        self.session = config.session
        self.ticket = config.ticket
        self.timeout = config.timeout
        self.base_url = f"https://api.mercadopublico.cl/servicios/v1/publico"

    def call_api(self, endpoint):
        url = self._build_url(endpoint)
        return self.get_result(url)

    def build_url(self, endpoint):
        raise NotImplementedError

    def get_result(self, url: str, params: dict = dict()) -> Result:
        """
        Dada una URL, obtiene el resultado json y su código de estado
        :param url: vtex endpoint
        :return: a namedtuple
        """
        params["ticket"] = self.ticket
        response = self.session.get(url, params=params, timeout=self.timeout)
        if response.status_code == 200:
            if "application/json" in response.headers.get("Content-Type"):
                json_response = response.json()
            else:
                print("text")
                json_response = response.text
        else:
            json_response = response.content
        output = Result(json_response, response.status_code)
        logger.debug("## GET RESPONSE FROM API ChileCompra ")
        logger.debug(output)
        return output
