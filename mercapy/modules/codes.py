from .base_api import BaseApi


class SearchCodes(BaseApi):
    """
    Ref: https://api.mercadopublico.cl/modules/ejemplo_10.aspx
    """

    def _build_url(self, endpoint):
        catalog_endpoint = "/Empresas"
        return self.base_url + catalog_endpoint + endpoint

    def get_public_org(self):

        url = self._build_url("/BuscarComprador")

        return self.get_result(url)

    def get_provider_code_by_rut(self, *, rut):
        url = self._build_url("/BuscarProveedor")

        params = {"rutempresaproveedor": rut}

        return self.get_result(url, params)
