class StokeError(Exception):
    pass


class OutOfStockError(StokeError):
    pass


class InvalidPromoError(StokeError):
    pass
