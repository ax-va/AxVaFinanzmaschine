from lot import Lot


class AssetLot(Lot):
    def __init__(self, asset_name: str):
        self.name: str = asset_name
        self.amount_bought: float = 0
        self.amount_sold: float | None = None
        super().__init__()

    def buy(
        self,
        share_amount: float,
        entitlement: float,  # asset per share
        price_implied: float,
        price_dt: datetime.datetime,
    ) -> None:
        assert share_amount > 0
        assert entitlement > 0
        assert self.amount_bought == 0

        self.amount_bought: float = share_amount * entitlement
        self.price_bought: float = price_implied
        self.price_bought_dt: datetime.datetime = price_dt

    def sell(
        self,
        share_amount: float,
        entitlement: float,  # asset per share
        price_implied: float,
        price_dt: datetime.datetime,
    ) -> None:
        assert share_amount > 0
        assert entitlement > 0
        assert self.amount_bought > 0

        self.amount_sold: float = share_amount * entitlement
        self.price_sold: float = price_implied
        self.price_sold_dt: datetime.datetime = price_dt
