import io
import pandas as pd

def conversor(df):
    output = io.BytesIO()
    with pd.ExcelWriter(output,engine='xlsxwriter') as writer:
        df.to_excel(writer, index=False)
        
    processed = output.getvalue()

    return processed
