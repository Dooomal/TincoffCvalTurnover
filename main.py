# pip install tinkoff-investments

from tinkoff.invest import Client
import creds
import time


with Client(token=creds.token) as client:
    def cast_money(v):
        d = v.units + v.nano / 1e9
        return d

    f = open('turnover.txt')
    turnover = int(f.read())
    while turnover < 6000000:
        r = client.market_data.get_last_prices(
            figi=["BBG333333333"])
        price_by = client.market_data.get_order_book( #получение цены на покупку по стакану
            figi="BBG333333333",
            instrument_id='figi',
            depth=4
        ).bids[0].price
        quantity = int(  # расчет количества лотов которое можно купить
            (client.operations.get_withdraw_limits(account_id=creds.account_id).money[0].units // cast_money(
            price_by)) - 1)
        f = open('status.txt')


        by_etf = client.orders.post_order(
            figi='BBG333333333',
            quantity=quantity,
            price=price_by,
            direction=1,
            account_id=creds.account_id,
            order_type=1
        )
        print(by_etf)
        lots_requests = client.orders.get_order_state(
            account_id=creds.account_id, order_id=by_etf.order_id).lots_requested
        lots_executed = client.orders.get_order_state(
            account_id=creds.account_id, order_id=by_etf.order_id).lots_executed

        while lots_executed != lots_requests:
            lots_executed = client.orders.get_order_state(
                account_id=creds.account_id, order_id=by_etf.order_id).lots_executed

            time.sleep(5)
            print(lots_executed)

        quantity = lots_executed
        price_sell = client.market_data.get_order_book(  # получение цены на покупкупо стакану
            figi="BBG333333333",
            instrument_id='figi',
            depth=4
        ).asks[0].price

        sell_etf = client.orders.post_order(
            figi='BBG333333333',
            quantity=quantity,
            price=price_sell,
            direction=2,
            account_id=creds.account_id,
            order_type=1)
        print(sell_etf)














