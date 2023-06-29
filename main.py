# pip install tinkoff-investments

from tinkoff.invest import Client
import creds


with Client(token=creds.token) as client:
    def cast_money(v):
        d = v.units + v.nano / 1e9
        return d

    f = open('turnover.txt')
    turnover = int(f.read())
    while turnover < 6000000:
        r = client.market_data.get_last_prices(
            figi=["BBG333333333"])
        price_by = client.market_data.get_order_book(
            figi="BBG333333333",
            instrument_id='figi',
            depth=4
        ).bids[0].price
        quantity = int(
            (client.operations.get_withdraw_limits(account_id=creds.account_id).money[1].units // cast_money(
            price_by)) - 1)











