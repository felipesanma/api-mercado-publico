from mercapy import Mercapy

ticket = "2C9F8A33-10E9-4F37-9ED8-E282FB355A39"
mercapi = Mercapy(ticket=ticket)

fecha = "05062023"

# print(mercapi.tenders.get_by_date(date=fecha))
print(mercapi.tenders.get_today_states())
print("END")
