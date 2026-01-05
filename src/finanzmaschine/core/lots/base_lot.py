import datetime
import math
from typing import List


class BaseLot:
    def __init__(self):
        self.units_in: float = 0
        self.price_in: float | None = None
        self.datetime_in: datetime.datetime | None = None
        self.units_out_list: List[float] = []
        self.price_out_list: List[float] = []
        self.datetime_out_list: List[datetime.datetime] = []

    @property
    def units_out_total(self):
        return math.fsum(self.units_out_list)

    @property
    def units_open(self) -> float:
        return self.units_in - self.units_out_total

    def record_in(
        self,
        units_in: float,
        price_in: float,
        datetime_in: datetime.datetime,
    ) -> None:
        assert self.units_in == 0
        assert units_in > 0
        assert price_in > 0

        self.units_in: float = units_in
        self.price_in: float = price_in
        self.datetime_in: datetime.datetime = datetime_in

    def record_out(
        self,
        units_out: float,
        price_out: float,
        datetime_out: datetime.datetime,
    ) -> None:
        assert self.units_in > 0
        assert units_out > 0
        assert price_out > 0

        self.units_out_list.append(units_out)
        self.price_out_list.append(price_out)
        self.datetime_out_list.append(datetime_out)
