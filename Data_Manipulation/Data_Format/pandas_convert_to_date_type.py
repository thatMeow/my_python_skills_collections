import pandas as pd
from pandas import DataFrame, Series
from pandas.tseries.offsets import MonthEnd

from datetime import datetime
import datetime

df['col'] = pd.to_datetime(df['col']) + MonthEnd(1) # change vintage to month end
df['col'] = df['col'].dt.date

