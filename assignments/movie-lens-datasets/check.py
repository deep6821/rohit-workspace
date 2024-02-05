import pandas as pd
import constants as const
print(const.MOVIES_DAT_FILE)
df = pd.read_csv(const.MOVIES_DAT_FILE, header=None, sep='::', engine='python')
print(df.head(5))
