import pandas as pd

iter_csv = pd.read_csv('SampleLog.log', iterator=True, chunksize=1000)
print(iter_csv)