import pandas as pd


class DFPlus(pd.DataFrame):
    @property
    def _constructor(self):
        return DFPlus

    @classmethod
    def from_csv(cls, filepath, **kwargs):
        df = pd.read_csv(filepath, **kwargs)
        return cls(df)

    def print_with_headers(self):
        """
        Print the DataFrame in chunks of `chunk_size` rows,
        re-printing the column headers at the top of each block.
        """
        total_rows = len(self)
        for start in range(0, total_rows, 10):
            end = start + 10
            block = super().iloc[start:end]
            print(block.to_string(index=True))


dfp = DFPlus.from_csv("../csv/products.csv")
dfp.print_with_headers()
