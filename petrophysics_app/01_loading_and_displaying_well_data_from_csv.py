# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "marimo==0.14.12",
#     "altair==4.2.0",
#     "matplotlib",
#     "hvplot",
#     "scipy",
#     "numpy>=1.26.4",
#     "polars>=0.20.31"
# ]
# ///

import marimo

__generated_with = "0.14.13"
app = marimo.App(width="columns")


@app.cell(column=0, hide_code=True)
def _(mo):
    mo.md(r"""## 1. Loading and Displaying Well Data From CSV""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    Created By: [Andy McDonald (Original Author)](https://github.com/andymcdgeo/)

    Original Repo: [Petrophysics-Python-Series](https://github.com/andymcdgeo/Petrophysics-Python-Series)

    ---

    Modified By: [T. S. Kelrey](https://github.com/kelreeeeey)

    All Credits to McDonald, A., tho! I'm just chillin with [marimo](https://marimo.io/) here!
    """
    )
    return


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""The following tutorial illustrates loading basic well log data from a csv file by using pandas, and displaying the data using the plotting option available in pandas.""")
    return


@app.cell
def _():
    import polars as pl
    import pandas as pd
    import numpy as np
    import altair as alt
    import plotly as ply
    import hvplot as hv
    import matplotlib.pyplot as plt
    # pd.options.plotting.backend = "plotly"
    return hv, np, pd, plt


@app.cell
def _(mo, pd):
    well = pd.read_csv(mo.notebook_location() / "public" / "data/L0509WellData.csv", header=0)
    return (well,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""To check that the data has been loaded in correctly, we can use the .head() function in pandas to view the first 5 rows and the header.""")
    return


@app.cell
def _(well):
    well.head()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""We can also view some statistics on the curves by using the describe() function.""")
    return


@app.cell
def _(well):
    well.describe()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Before carrying out any displaying of data or calculations, we carry out some data cleansing. The first is the conversion of null values, represented by -999.25, to a Not a Number (NaN). We can achieve this using the replace function.""")
    return


@app.cell
def _(well):
    well
    return


@app.cell
def _(np, well):
    well.replace(-999.0, np.nan, inplace=True)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""If we now call the describe and head functions on the well dataframe, we can see that the nulls have been been replaced.""")
    return


@app.cell
def _(well):
    well.describe()
    return


@app.cell
def _(well):
    well.head()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""By default, the well.head() function produces the first 5 rows of data. We can extend this by passing in a value to the head function.""")
    return


@app.cell
def _(well):
    well.head(20)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Now we have some data appearing in the GR column.""")
    return


@app.cell(column=1, hide_code=True)
def _(mo):
    mo.md(r"""### Viewing Data on a Log Plot""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""With polars, we can quickly bring up a plot of our well data by using the `.plot()` function on our well dataframe. <br><br>If we just specify the x and y axis, we can generate a simple line plot.""")
    return


@app.cell
def _(mo, plt, well):
    plt.figure(figsize=(4.5, 16))
    plt.plot(well["GR"], well["DEPTH"], label="Gamma Ray")
    plt.xlabel("GR"); plt.ylabel("DEPTH")
    plt.legend()
    plt.grid(True, "both")
    mo.as_html(plt.gca()).center()
    return


@app.cell(column=2, hide_code=True)
def _(mo):
    mo.md(r"""### Cross Plot""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""We can change the type of plot by using the keyword kind and passing in the word scatter. In this example we have a familiar density neutron crossplot. <b>Note</b> that we can change the y-axis scales so that they are flipped and show increasing porosity as you move up the axis.""")
    return


@app.cell
def _(mo, plt, well):
    # well.plot(kind = 'scatter', x = 'NPHI', y = 'RHOB')
    plt.scatter(well['NPHI'], well['RHOB'])
    plt.xlabel("NPHI"); plt.ylabel("RHOB")
    mo.as_html(plt.gca()).center()
    return


@app.cell
def _(mo, well):
    selection = well.columns
    select_x = mo.ui.radio(selection, value="NPHI", inline=True)
    select_y = mo.ui.radio(selection, value="RHOB", inline=True)
    select_c = mo.ui.radio(selection, value="GR", inline=True)
    return select_c, select_x, select_y


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        f"""
    ### We can also add some colour to our plot using the gamma ray as a third axis. This is done by including the c argument and specifying the column name. <br><br>

    > This helps us identify the cleaner intervals from shalier intervals
    """
    )
    return


@app.cell(hide_code=True)
def _(mo, select_c, select_x, select_y):
    mo.md(f"""
    | Config |     | Options    |
    | :----: | --- | :-------- |
    | X Axis |     | {select_x} |
    | Y Axis |     | {select_y} |
    | Color  |     | {select_c} |
    """).center().callout()
    return


@app.cell
def _(hv, select_c, select_x, select_y, well):
    hv.plot(well, kind = 'scatter',
            x = select_x.value, y = select_y.value, color=select_c.value,
            cmap="jet", width=600, height=500, grid=True)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Data can also be easily displayed as a histogram in the form of bars:""")
    return


@app.cell
def _(mo, plt, well):
    _ = plt.hist(well['GR'], bins=30)
    plt.ylabel("Frequency")
    mo.as_html(plt.gca()).center()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""That is all for this short tutorial. In the next one we will take our plotting to the next level and construct the familiar log plot using matplotlib.""")
    return


if __name__ == "__main__":
    app.run()
