# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "marimo==0.14.13",
#     "numpy==1.26.4",
#     "pandas>=2.0.3",
#     "pyarrow==21.0.0",
#     "altair==5.5.0",
#     "hvplot==0.11.3",
#     "polars==1.30.0",
# ]
# ///

import marimo

__generated_with = "0.14.13"
app = marimo.App(width="columns")


@app.cell(column=0)
def _():
    import marimo as mo
    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## 2. Displaying a Well Plot with Matplotlib""")
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


    ---
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    This notebook is layout in "vertical/column" mode.

    Each "column" will be treated like "chapter" or "sub-chapter" I would say. Enjoy!!
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Wait up, it takes some times to fully load


    >
    > Note 💡
    >
    > you can always show the code of the notebook by clicking the `three dots` button on the top-right corner of this page.
    """).callout("danger")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        """
    ### Modifications:

    - Using `marimo notebook` instead of `jupyter notebook`

    - Using `polars` instead of `pandas` to read the csv

    - Visualize things using `altair` instead of `matplotlib`

    - Costumizing logplot!
    """
    )
    return


@app.cell(hide_code=True)
def _():
    import polars as pl
    import altair as alt
    return alt, pl


@app.cell
def _(mo):
    mo.md(r"""> ### The following tutorial illustrates displaying well data from a CSV on a custom `altair` (instead of matplotlib) plot.""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""The following cells load data in from a CSV file and replace the null values (-999.25) with Not a Number (NaN) values. More detail can be found in 1. Loading and Displaying Well Data From CSV.""")
    return


@app.cell
def _(mo, pl):
    _s = dict()
    raw_well = pl.read_csv(str(mo.notebook_location() / "public" / "data/L0509WellData.csv"))
    for col in raw_well.columns:
        _s[col] = raw_well[col].replace([-999.00, -999.25], [float("nan"), float("nan")])
    well = pl.DataFrame(_s)
    return (well,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""### Loading Well Data from CSV""")
    return


@app.cell
def _(well):
    well.describe()
    return


@app.cell(column=1, hide_code=True)
def _(mo):
    mo.md(r"""### Setting up the logplot""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    We can quickly make a log plot using altair charts.

    There is a same concept like "subplots" of matplotlib.pyplot in Altari.

    This allows us to space out multiple plots (tracks) in an easy to understand way. <br><br>

    We will separate, and combine altair chart in a several manner to produce a convinient log plot.
    """
    )
    return


@app.cell
def _(mo, well):
    selection = well.columns
    select_log = mo.ui.radio(selection[1:], value="GR", label="## Log to plot", inline=True)
    select_log_scale = mo.ui.switch(label="Logarithmic scale?", value=False)
    return (select_log_scale,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    #### Customising the Log Plot
    We can further customise the plot to look more like a familiar log plot, with the curve names and scales at the top and two curves (density & neutron) in the one track.
    """
    )
    return


@app.cell(hide_code=True)
def _(alt, mo, select_log_scale, well):
    _xlim = (well["GR"].max()+0.001, well["GR"].min() - 0.001)
    _ylim = (well["DEPTH"].max()+10, well["DEPTH"].min() - 10)

    _base = alt.Chart(well)

    _SHARE_Z = (
        alt
            .Y('DEPTH', sort = 'descending',scale=alt.Scale(domain=_ylim))
            .scale(zero=False, type="linear")
            .axis(disable=True)
    )
    _height = 1000
    _width  = 220 


    # ---
    # .configure_axisBottom(disable = False, position = 0, bandPosition= 10, labelBaseline="line-top")
    # ---


    _chrt = (
        _base
            .mark_line(color='green', point=False,)
            .encode(
                (
                    alt
                        .X("GR", scale=alt.Scale(domain=_xlim))
                        .scale(zero=False, type="log" if select_log_scale.value else "linear")
                        .axis(bandPosition= 100, orient="top", labelColor="green", titleColor="green",
                             grid=True, gridColor="green", gridOpacity=0.25)
                ),
                _SHARE_Z,
                order = 'DEPTH')
        .properties(width=_width, height=_height,)
        
    )

    _chrt_density = (
        _base
            .mark_line(color='red', point=False,)
            .encode(
                (
                    alt
                        .X("RHOB", scale=alt.Scale(domain=(1.95, 2.95)), title="Density", titleColor="red")
                        .scale(zero=False, type="log" if select_log_scale.value else "linear")
                        .axis(offset=0, orient="top", labelColor="red", titleColor="red",
                             grid=True, gridColor="red", gridOpacity=0.25)
                ),
                _SHARE_Z.axis(title="", domain=False, tickSize=0, labels=False),
                order = 'DEPTH')
        .properties(width=_width, height=_height,)
        
    )

    _chrt_neutron = (
        _base
            .mark_line(color='blue', point=False,)
            .encode(
                (
                    alt
                        .X("NPHI", scale=alt.Scale(domain=(0.45, -0.15)), title="Neutron")
                        .scale(zero=False, type="log" if select_log_scale.value else "linear")
                        .axis(offset=50, orient="top", labelColor="blue", titleColor="blue",
                              grid=True, gridColor="blue", gridOpacity=0.25)
                ),
                _SHARE_Z.axis(title="", domain=False, tickSize=0, labels=False),
                order = 'DEPTH')
        .properties(width=_width, height=_height,)
        
    )

    _chrt_sonic = (
        _base
            .mark_line(color='purple', point=False,)
            .encode(
                (
                    alt
                        .X("DT", scale=alt.Scale(domain=(140, 40)), title="Sonic")
                        .scale(zero=False, type="log" if select_log_scale.value else "linear")
                        .axis(offset=0, orient="top", labelColor="purple", titleColor="purple",
                              grid=True, gridColor="purple", gridOpacity=0.25)
                ),
                _SHARE_Z.axis(title="", domain=False, tickSize=0, labels=False),
                order = 'DEPTH')
        .properties(width=_width, height=_height,)
        
    )

    # mo.vstack(
    #     [
    #         # mo.hstack([select_log, select_log_scale], justify="space-around"),
    #         mo.hstack([_chrt, _chrt2])
    #     ],
    # )
    mo.ui.altair_chart(
        alt.hconcat(
            _chrt, 
            (_chrt_neutron + _chrt_density).resolve_scale(x="independent"),
            _chrt_sonic
        )
    ).center()
    return


if __name__ == "__main__":
    app.run()
