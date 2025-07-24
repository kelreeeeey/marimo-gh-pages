# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "marimo==0.14.13",
#     "altair==4.2.0",
#     "matplotlib==3.10.3",
#     "hvplot==0.11.3",
#     "numpy==1.26.4",
#     "pandas==2.0.3",
#     "pyarrow==21.0.0",
#     "pyarr==5.2.0",
#     "polars==0.20.23",
# ]
# ///

import marimo

__generated_with = "0.14.13"
app = marimo.App(width="full")


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _(mo):
    mo.md("""# Hello World""")
    return


@app.cell(hide_code=True)
def _():
    import pandas as pd
    import numpy as np
    import hvplot as hv
    import matplotlib.pyplot as plt
    import polars as pl

    return pd, pl


@app.cell(hide_code=True)
def _(mo, pd):
    well = pd.read_csv(
        mo.notebook_location() / "public" / "data/L0509WellData.csv", header=0
    )

    well
    return


@app.cell
def _(mo, pl):
    well_2 = pl.read_csv(
        mo.notebook_location() / "public" / "data/L0509WellData.csv"
    ).to_pandas()
    well_2
    return


if __name__ == "__main__":
    app.run()
