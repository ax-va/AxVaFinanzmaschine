import datetime
from typing import List


class BaseLot:
    def __init__(self):
        self.units_in: float = 0
        self.price_in: float | None = None
        self.price_in_dt: datetime.datetime | None = None
        self.units_out_list: List[float] = []
        self.price_out_list: List[float] = []
        self.price_out_dt_list: List[datetime.datetime] = []
