from utils import ModelBase


class Bill(ModelBase):
    def __init__(self):
        table="bills"
        columns="(document, email, amount, date, reference)"
        super().__init__(table, columns)
