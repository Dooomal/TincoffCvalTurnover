# pip install tinkoff-investments

from tinkoff.invest import Client
import creds


with Client(token=creds.token) as client:
    def cast_money(v):
        d = v.units + v.nano / 1e9
        return d

