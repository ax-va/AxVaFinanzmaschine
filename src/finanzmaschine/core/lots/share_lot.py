import datetime
from typing import List

from finanzmaschine.core.lots.asset_lot import AssetLot
from finanzmaschine.core.lots.position_lot import PositionLot
from finanzmaschine.core.market.instruments import Share


class ShareLot(PositionLot):
    def __init__(self, share: Share):
        super().__init__()
        self.share: Share = share
        self.asset_lot = AssetLot(self.share.require_asset())
        self.entitlement_in: float | None = None  # asset per share
        self.entitlement_out_list: List[float] = []  # asset per share

    def extended_record_in(
        self,
        units_in: float,  # units bought
        price_in: float,
        datetime_in: datetime.datetime,
        entitlement_in: float,  # asset units per a share unit when buying
    ) -> float:
        assert entitlement_in > 0

        super().record_in(
            units_in=units_in,
            price_in=price_in,
            datetime_in=datetime_in,
        )
        self.entitlement_in: float = entitlement_in
        cash_in: float = units_in * price_in
        return cash_in

    def extended_record_out(
        self,
        units_out: float,  # units sold
        entitlement_out: float,  # asset units per a share unit when selling
        price_out: float,
        datetime_out: datetime.datetime,
    ) -> float:
        assert entitlement_out > 0

        super().record_out(
            units_out=units_out,
            price_out=price_out,
            datetime_out=datetime_out,
        )
        self.entitlement_out_list.append(entitlement_out)
        cash_out: float = units_out * price_out
        return cash_out


def record_share_lot_in(
    share_lot: ShareLot,
    share_units_in: float,  # share units to buy
    share_price_in: float,
    datetime_in: datetime.datetime,
    entitlement_in: float,  # asset units per a share unit when buying
) -> float:
    share_lot.asset_lot.record_in(
        units_in=share_units_in * entitlement_in,  # implied units
        price_in=share_price_in / entitlement_in,  # implied price
        datetime_in=datetime_in,
    )
    cash_in: float = share_lot.extended_record_in(
        units_in=share_units_in,
        price_in=share_price_in,
        datetime_in=datetime_in,
        entitlement_in=entitlement_in,
    )
    return cash_in


def record_share_lot_out(
    share_lot: ShareLot,
    share_units_out: float,  # share units to sell
    share_price_out: float,
    datetime_out: datetime.datetime,
    entitlement_out: float,  # asset units per a share unit when selling
) -> float:
    share_lot.asset_lot.record_out(
        units_out=share_units_out * entitlement_out,  # implied units
        price_out=share_price_out / entitlement_out,  # implied price
        datetime_out=datetime_out,
    )
    cash_out: float = share_lot.extended_record_out(
        units_out=share_units_out,
        price_out=share_price_out,
        datetime_out=datetime_out,
        entitlement_out=entitlement_out,
    )
    return cash_out
