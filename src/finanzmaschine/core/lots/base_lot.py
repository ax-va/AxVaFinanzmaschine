import datetime as dt
import math
from typing import List, Type, TypeVar, Generic

from finanzmaschine.core.lots.base_lot_record import BaseLotRecord

TLotRecord = TypeVar("TLotRecord", bound=BaseLotRecord)


class BaseLot(Generic[TLotRecord]):
    """
    Generic lot managing immutable lot records.

    Subclasses must define `record_cls`, a dataclass subclass of `BaseLotRecord`.
    """

    record_cls: Type[TLotRecord]

    def __init__(self):
        if not hasattr(self, "record_cls"):
            raise TypeError(f"{type(self).__name__} must define class attribute `record_cls`")

        self.lot_record_in: TLotRecord | None = None
        self.lot_records_out: List[TLotRecord] = []

    @property
    def units_out_total(self):
        return math.fsum(lr.units for lr in self.lot_records_out)

    def record_in(
        self,
        *,
        units: float,
        price: float,
        datetime: dt.datetime,
        **kwargs,
    ) -> None:
        assert units > 0
        assert price > 0

        self.lot_record_in = self.record_cls(
            units=units,
            price=price,
            datetime=datetime,
            **kwargs,
        )

    def record_out(
        self,
        *,
        units: float,
        price: float,
        datetime: dt.datetime,
        **kwargs,
    ) -> None:
        assert self.lot_record_in.units > 0
        assert units > 0
        assert price > 0

        lot_record_out = self.record_cls(
            units=units,
            price=price,
            datetime=datetime,
            **kwargs,
        )
        self.lot_records_out.append(lot_record_out)
