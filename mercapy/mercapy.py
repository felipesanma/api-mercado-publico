from collections import namedtuple

import requests

from .modules import Tenders

DEFAULT_TIMEOUT = 5


class Mercapy:
    """
    Cliente de la API de Mercado público
    Reference: https://api.mercadopublico.cl/
    """

    def __init__(self, *, ticket: str = None, session=None, timeout=None):
        self.ticket = ticket
        session = self._init_session(session)
        timeout = timeout or DEFAULT_TIMEOUT
        config = namedtuple("config", ["ticket", "session", "timeout"])

        cfg = config(ticket, session, timeout)
        self.tenders = Tenders(cfg)
        # self.purchase = PurchaseOrders(cfg)

    def _init_session(self, session):
        """
        Inicializa la sesión
        :param session:
        :return: a requests Session object
        """
        if not session:
            session = requests.Session()

        return session
