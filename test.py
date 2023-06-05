from mercapy import Mercapy

ticket = "F8537A18-6766-4DEF-9E59-426B4FEE2844"
mercapi = Mercapy(ticket=ticket)

fecha = "05062023"

# print(mercapi.tenders.get_by_date(date=fecha))
print(mercapi.tenders.get_today_states())
print("END")
