from functools import reduce


def concat_column(df, name, columns, sep):
    series_with_sep = lambda series: series + sep
    df[name] = reduce(lambda x, y: x + y, (series_with_sep(df[col]) for col in columns))
    df[name] = df[name].apply(lambda x: x.strip(sep))
    return df


"""
Ex)

df["abcde"] = df["a"] + "_" + df["b"] + "_" + df["c"] + "_" + df["d"] + "_" + df["e"]

df = concat_column(df, "abcde", ["a", "b", "c", "d", "e"], "_")

"""
