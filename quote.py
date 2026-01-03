import datetime


class Quote:
    def __init__(self) -> None:
        self.data = {
            "GB00BLD4ZM24": {
                datetime.datetime(year=2026, month=1, day=2, hour=16, minute=15): {
                    "ETP": {
                        "bid_eur": None,
                        "ask_eur": None,
                    },
                    "ETH": {
                        "bid_eur": 2610,
                        "ask_eur": 2613,
                        "local_high_eur": 4000,
                    }
                }
            }
        }
