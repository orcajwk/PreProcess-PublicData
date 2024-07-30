import pandas as pd

def read_csv(file_path):
    encodings = ["utf-8", "cp949"]
    seps = [",", "|"]
    for encoding in encodings:
        for sep in seps:
            try:
                df = pd.read_csv(
                    file_path, encoding=encoding, sep=sep, low_memory=False, on_bad_lines="skip"
                )
                return (df, encoding, sep)
            except UnicodeDecodeError:
                continue
            except pd.errors.ParserError:
                continue
    return (None, None, None)