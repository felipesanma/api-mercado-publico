from .base_api import BaseApi


class PurchaseOrders(BaseApi):
    """
    https://api.mercadopublico.cl/modules/ejemplo_10.aspx

    Listar Órdenes de Compra diarias
    Listar Órdenes de Compra por código
    Listar Órdenes de Compra diarias por estado
    Listar Órdenes de Compra por día
    Listar Órdenes de Compra por estado y día
    Listar Órdenes de Compra por código de organismo público o proveedor
    """

    def _build_url(self):
        catalog_endpoint = "/ordenesdecompra.json?"
        return self.base_url + catalog_endpoint
