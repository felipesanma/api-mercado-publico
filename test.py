from mercapy import Mercapy

ticket = "F8537A18-6766-4DEF-9E59-426B4FEE2844"
mercapi = Mercapy(ticket=ticket)

"""
fecha = "05062023"
print(mercapi.tenders.get_by_date(date=fecha))
"""

today_tenders = mercapi.tenders.get_today_states()
tender_sample = today_tenders.json["Listado"][0]
tender_code_sample = tender_sample["CodigoExterno"]
# tender_web_url = mercapi.tenders.get_url_by_code(tender_code=tender_code_sample)

print(tender_sample)
