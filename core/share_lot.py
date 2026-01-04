import datetime

from asset_lot import AssetLot
from lot import Lot


class ShareLot(Lot):
    def __init__(
        self,
        share_isin: str,
        share_name: str = None,
        asset_name: str = None,
    ):
        self.isin: str = share_isin
        self.name: str = share_name
        self.asset_lot = AssetLot(asset_name)
        super().__init__()


def buy_share_lot(
    share_lot: ShareLot,
    cash: float,
    share_price: float,
    asset_per_share: float,
    price_dt: datetime.datetime,
) -> None:
    share_lot.buy(cash, share_price, price_dt)
    implied_asset_price: float = share_price / asset_per_share
    share_lot.asset_lot.buy(cash, implied_asset_price, price_dt)


def sell_share_lot(
    share_lot: ShareLot,
    share_price: float,
    asset_per_share: float,
    price_dt: datetime.datetime,
) -> float:
    cash: float = share_lot.sell(share_price, price_dt)
    implied_asset_price: float = share_price / asset_per_share
    share_lot.asset_lot.sell(implied_asset_price, price_dt)
    return cash
