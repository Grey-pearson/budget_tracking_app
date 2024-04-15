import numpy as np
import pandas as pd

# import slight_budgetting.xlsx

delta_frame1 = pd.read_excel(
    "slight_budgetting.xlsx", "Sheet1", index_col=None, na_values=["NA"]
)

print(delta_frame1)
