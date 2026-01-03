from enum import Enum

class Mode(Enum):
    VACUUM = "VACUUM"
    ACC = "ACC"  # accumulator
    HUNTER = "HUNTER"


def detect_mode(price, vacuum_upper, acc_upper) -> Mode:
    if price <= vacuum_upper:
        return Mode.VACUUM
    elif price <= acc_upper:
        return Mode.ACC
    else:
        return Mode.HUNTER


if __name__ == "__main__":
    local_high = 4000
    profit_p = 0.2  # take profit percent
    loss_p = profit_p * 2  # acceptable loss percent
    vacuum_upper = local_high * (1 - loss_p)
    print("vacuum_upper:", vacuum_upper)

    etp_price_bid = 2610  # sell
    etp_price_ask = 2613  # buy
    etp_price_spread = etp_price_ask - etp_price_bid
    print("etp_price_spread:", etp_price_spread)

    acc_upper = vacuum_upper / (1 - profit_p)
    print("acc_upper:", acc_upper)

    mode = detect_mode(etp_price_ask, vacuum_upper, acc_upper)
    print("mode:", mode)

    limit_order = etp_price_ask * (1 + profit_p)
    print("limit_order:", limit_order)

    stop_loss_raw = etp_price_ask * (1 - loss_p)
    print("stop_loss_raw:", stop_loss_raw)
    stop_loss = max(vacuum_upper, stop_loss_raw)
    print("stop_loss:", stop_loss)

    cash_input = 0
    etp_amount_bought = cash_input / etp_price_ask
    print("etp_amount_bought:", etp_amount_bought)
