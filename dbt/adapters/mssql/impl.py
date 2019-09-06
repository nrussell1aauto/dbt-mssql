import agate

from dbt.adapters.sql import SQLAdapter
from dbt.adapters.mssql import MSSQLConnectionManager


class MSSQLAdapter(SQLAdapter):
    ConnectionManager = MSSQLConnectionManager

    @classmethod
    def date_function(cls):
        return 'get_date()'

    @classmethod
    def convert_text_type(cls, agate_table, col_idx):
        return 'varchar(max)'

    @classmethod
    def convert_number_type(cls, agate_table, col_idx):
        decimals = agate_table.aggregate(agate.MaxPrecision(col_idx))
        return "decimal(18, 2)" if decimals else "integer"

