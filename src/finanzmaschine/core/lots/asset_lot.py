import datetime

from finanzmaschine.core.lots.base_lot import BaseLot
from finanzmaschine.core.market.asset import Asset


class AssetLot(BaseLot):
    def __init__(self, asset: Asset):
        super().__init__()
        self.asset: Asset = asset

    def record_in(
        self,
        share_units_in: float,  # share units to buy
        entitlement_in: float,  # asset units per a share unit when buying
        price_in: float,  # implied price
        datetime_in: datetime.datetime,
    ) -> None:
        assert self.units_in == 0
        assert share_units_in > 0
        assert entitlement_in > 0
        assert price_in > 0

        self.units_in: float = share_units_in * entitlement_in
        self.price_in: float = price_in
        self.datetime_in: datetime.datetime = datetime_in

    def record_out(
        self,
        share_units_out: float,  # share units to sell
        entitlement_out: float,  # asset units per a share unit when selling
        price_out: float,  # implied price
        datetime_out: datetime.datetime,
    ) -> None:
        assert self.units_in > 0
        assert share_units_out > 0
        assert entitlement_out > 0
        assert price_out > 0

        self.units_out_list.append(share_units_out * entitlement_out)
        self.price_out_list.append(price_out)
        self.datetime_out_list.append(datetime_out)
