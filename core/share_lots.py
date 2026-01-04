from core.instrument import Instrument
from core.share_lot import ShareLot


class GB00BLD4ZM24(ShareLot):
    def __init__(self):
        super().__init__(
            share_isin="GB00BLD4ZM24",
            share_name="CoinShares Physical Staked Ethereum",
            share_instrument=Instrument.ETP,
            asset_name="ETH",
        )
