import datetime


class Lot:
    def __init__(self):
        self.price_bought: float | None = None
        self.price_bought_dt: datetime.datetime | None = None
        self.price_sold: float | None = None
        self.price_sold_dt: datetime.datetime | None = None
