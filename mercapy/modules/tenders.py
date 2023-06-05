from .base_api import BaseApi


class Tenders(BaseApi):
    """
    Ref: https://api.mercadopublico.cl/modules/ejemplo_10.aspx
    """

    def _build_url(self):
        catalog_endpoint = "/licitaciones.json"
        return self.base_url + catalog_endpoint

    def get_today_states(self):
        url = self._build_url()
        return self.get_result(url)

    def get_states_by_date(self, *, date):
        url = self._build_url()

        params = {"fecha": date}

        return self.get_result(url, params)

    def get_by_code(self, *, tender_code):
        url = self._build_url()

        params = {"codigo": tender_code}

        return self.get_result(url, params)

    def get_actives(self):
        """
        muestra todas las licitaciones publicadas al día de realizada la consulta.
        """
        url = self._build_url()

        params = {"codigo": "activas"}

        return self.get_result(url, params)

    """
    def get(
        self, *, date="", state="", tender_code="", public_org_code="", provider_code=""
    ):
        url = self._build_url()

        params = {
            "fecha": date,
            "estado": state,
            "codigo": tender_code,
            "CodigoOrganismo": public_org_code,
            "CodigoProveedor": provider_code,
        }

        return self.get_result(url, params)
    """
