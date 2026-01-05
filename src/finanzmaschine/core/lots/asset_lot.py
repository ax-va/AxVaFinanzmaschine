import datetime

from finanzmaschine.core.lots.base_lot import BaseLot
from finanzmaschine.core.market.asset import Asset


class AssetLot(BaseLot):
    def __init__(self, asset: Asset):
        super().__init__()
        self.asset: Asset = asset
