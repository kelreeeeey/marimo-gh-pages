# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "marimo==0.14.12",
#     "numpy==1.26.4",
#     "pandas>=2.0.3",
#     "pyarrow==21.0.0",
#     "altair==5.5.0",
#     "hvplot==0.11.3",
#     "polars==1.30.0",
#     "wigglystuff",
# ]
# ///

import marimo

__generated_with = "0.14.12"
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def _():
    import marimo as mo
    import polars as pl
    import altair as alt
    return alt, mo, pl


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## 2. Displaying a Well Plot with _`Altair`_ instead of _`Matplotlib`_""")
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
def _(mo):
    mo.md(r"""> ## The following tutorial illustrates displaying well data from a CSV on a custom `altair` (instead of matplotlib) plot.""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## Loading Well Data from CSV""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""The following cells load data in from a CSV file and replace the null values (-999.25) with Not a Number (NaN) values. More detail can be found in 1. Loading and Displaying Well Data From CSV.""")
    return


@app.cell
def _(pl):
    _s = dict()
    raw_well = pl.read_csv("https://raw.githubusercontent.com/kelreeeeey/petrophysics-python-and-odin/master/Data/L0509WellData.csv")
    for col in raw_well.columns:
        _s[col] = raw_well[col].replace([-999.00, -999.25], [float("nan"), float("nan")])
    well = pl.DataFrame(_s)
    return (well,)


@app.cell
def _(mo):
    show_df_stat = mo.ui.switch(label="Show Dataframe Statistics?", value=True)
    show_df = mo.ui.switch(label="Show Dataframe", value=False)
    return show_df, show_df_stat


@app.cell
def _(mo, show_df, show_df_stat, well):
    if show_df_stat.value and not show_df.value:
        _h = mo.vstack([mo.hstack([show_df_stat, show_df]), well.describe()], align="end")
    elif show_df_stat.value and show_df.value:
        _h = mo.vstack([mo.hstack([show_df_stat, show_df]), well.describe(), well], align="end")
    elif not show_df_stat.value and show_df.value:
        _h = mo.vstack([mo.hstack([show_df_stat, show_df]), well], align="end")
    else:
        _h = mo.vstack([mo.hstack([show_df_stat, show_df])], align="end")
    _h
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ---





    ---
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## Setting up the logplot""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    <!-- We can quickly make a log plot using altair charts.

    There is a same concept like "subplots" of matplotlib.pyplot in Altari.

    This allows us to space out multiple plots (tracks) in an easy to understand way. <br><br>

    We will separate, and combine altair chart in a several manner to produce a convinient log plot. -->
    """
    )
    return


@app.cell
def _():
    # tab1 = mo.accordion(
    #         {
    #             "### 1.a. Chart": mo.md("Nothing!"),
    #             "### 1.b. Shared Depth Axis": mo.md("Nothing!"),
    #             "### 1.c. Putting those together": mo.md(
    #                 "![goat](https://images.unsplash.com/photo-1524024973431-2ad916746881)"
    #             ),
    #         },
    #         lazy=True
    #     )
    return


@app.cell
def _():
    # tab2 = mo.accordion(
    #         {

    #         },
    #         lazy=True
    #     )
    return


@app.cell
def _():
    # setup_log_plot_tabs = mo.ui.tabs({
    #     "## 1. Setup `Altair` Chart": tab1,
    #     "## 2. `Altair` Encoding": tab2
    # }, lazy=False, value="## 1. Setup `Altair` Chart", label="TL;DR")
    # # setup_log_plot_tabs
    return


@app.cell
def _(well):
    selection = well.columns
    return (selection,)


@app.cell
def _(mo):
    update_table_button = mo.ui.run_button(label="Update Plot Log Config", kind="warn")
    return (update_table_button,)


@app.cell
def _(mo, selection):
    n_log_charts = mo.ui.number(value=len(selection)-1, label="### Set Number of Log Charts")
    return (n_log_charts,)


@app.cell
def _(cycle, mo, n_log_charts, selection):
    import random
    _c = selection[1:]
    random.shuffle(_c)
    _log_cycle = cycle(_c)
    log_charts_selections = mo.ui.array(
        [mo.ui.multiselect(
            _c,
            label="",
            value=[_log],
            full_width=True
        ) for _i, _log in zip(range(n_log_charts.value), cycle(_c))],
        label="Chart")
    return (log_charts_selections,)


@app.cell
def _(mo, well):
    from itertools import cycle
    _color_cycle = cycle(["green", "purple", "red", "orange", "blue"])
    logs_input = [
        {
            "Log":_log,
            "Name":mo.ui.text(value=_log, label="Log Name"),
            "Color":mo.ui.text(value=_col),
            "Scale":mo.ui.dropdown(["linear", "log"], value="linear"),
            "Min-Max":mo.ui.dropdown(["auto", "manual"], value="auto"),
            "Min":mo.ui.number(step=0.01, value=-10),
            "Max":mo.ui.number(step=0.01, value=10),

        } for _log, _col in zip(well.columns[1:], _color_cycle)
    ]
    return cycle, logs_input


@app.cell
def _(logs_input, mo, well):
    tb = mo.ui.table(logs_input, selection="multi", label="### Plot Log Config",
                     initial_selection=list(range(len(well.columns[1:]))),
                     show_download=False,
                    )
    return (tb,)


@app.cell
def _(alt, get_lims, well):

    chart_height = 1000
    chart_width = 220

    _min_d, _max_d = get_lims("DEPTH")
    DEPTH_LIMIT = (_min_d + 400, _max_d -400)
    base_chart = alt.Chart(well, )

    ORDER = "DEPTH"
    DEPTH_ENCODING = (alt
        .Y('DEPTH', sort = 'descending',scale=alt.Scale(domain=get_lims("DEPTH")), )
        .scale(zero=False, type="linear")
        .axis(tickColor="black", domainWidth=2)
    )
    DEPTH_ENCODING_SHARED = DEPTH_ENCODING.axis(title="", domain=True, tickSize=0, labels=False, domainWidth=2)


    return (
        DEPTH_ENCODING,
        DEPTH_ENCODING_SHARED,
        ORDER,
        base_chart,
        chart_height,
        chart_width,
    )


@app.cell
def _(
    DEPTH_ENCODING,
    DEPTH_ENCODING_SHARED,
    ORDER,
    alt,
    base_chart,
    chart_height,
    chart_width,
    log_charts_selections,
    tb_val,
):
    log_charts = []
    for _i, _logs in enumerate(log_charts_selections.value):

        if 0 == _i:
            _z = DEPTH_ENCODING
        else:
            _z = DEPTH_ENCODING_SHARED
        log_charts.append([])
        _offset = 0

        if 0 == len(_logs):
            log_charts[_i].append(
                base_chart
                    .mark_line(color="black", point=False, strokeWidth=1)
                    .encode(_z, order = ORDER)
                .properties(width=chart_width, height=chart_height,)
            )
        for _selected_log in _logs:
            _log = tb_val[_selected_log].copy()
            log_charts[_i].append(
                base_chart
                    .mark_line(color=_log["Color"], point=False, strokeWidth=1)
                    .encode(
                        (
                            alt
                                .X(_log["Log"], scale=alt.Scale(domain=_log["Min-Max"]))
                                .scale(zero=False, type=_log["Scale"])
                                .axis(offset=_offset, bandPosition= 100, orient="top", labelColor=_log["Color"],
                                      title=_log["Name"], titleColor=_log["Color"],
                                     grid=True, gridColor=_log["Color"], gridOpacity=0.25, domainWidth=2)
                        ),
                        _z, order = ORDER)
                .properties(width=chart_width, height=chart_height,)
            )
            _offset += 50
    return (log_charts,)


@app.cell
def _(log_charts):
    len(log_charts)
    return


@app.cell
def _(alt, log_charts):
    hchart = alt.HConcatChart(
        spacing=0.0,
        background="white",
        bounds="full"
    )

    for _chrt in log_charts:
        if 1 == len(_chrt):
            hchart |= _chrt[0].resolve_scale(x="independent")#.add_params(brush)
        else:
            _h = _chrt[0].resolve_scale(x="independent")
            for _ in _chrt[1:]:
                _h += _.resolve_scale(x="independent")
            hchart |= _h.resolve_scale(x="independent")
    return (hchart,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        """
    ---

    ## The Plot

    - Double click on the chart to reset the view

    - You can click+drag to move the curve around its chart

    - Try to scroll up/down or pinch your touchpad the chart!
    """
    )
    return


@app.cell(hide_code=True)
def _(mo, tb, update_table_button):
    mo.vstack([mo.md("""
    - If you select/unselect the table' items, chart will be automatically updated

    - If you change the values for each row, you have to click the yellow button to update

    """),
               mo.vstack([tb, update_table_button], align="end")], align="start").center().callout(kind="info")
    return


@app.cell
def _(mo, n_log_charts):
    mo.vstack([n_log_charts, mo.md("Changing above number will reset the chart entirely")]).callout("danger")
    return


@app.cell
def _(log_charts_selections):
    log_charts_selections.hstack(align="start", justify="space-around", gap=5)
    return


@app.cell
def _(hchart, mo):
    mo_chart = mo.ui.altair_chart(hchart.interactive())
    mo_chart.center()
    # hchart.interactive()
    return


@app.cell
def _(mo, selection):
    select_x = mo.ui.radio(selection[1:], value="NPHI", inline=True)
    select_y = mo.ui.radio(selection[1:], value="RHOB", inline=True)
    select_xlog_scale = mo.ui.switch(label="Log scale?", value=False)
    select_ylog_scale = mo.ui.switch(label="Log scale?", value=False)
    select_c = mo.ui.radio(selection, value="GR", inline=True)
    return select_c, select_x, select_xlog_scale, select_y, select_ylog_scale


@app.cell
def _(
    alt,
    mo,
    select_c,
    select_x,
    select_xlog_scale,
    select_y,
    select_ylog_scale,
    well,
):
    cross_plot_chrt = mo.ui.altair_chart(
        alt.Chart(well)
            .mark_point(filled=True)
            .encode(
                alt.X(select_x.value).scale(
                    zero=False, type="log" if select_xlog_scale.value else "linear"),
                alt.Y(select_y.value).scale(
                    zero=False, type="log" if select_ylog_scale.value else "linear"),
                color=alt.Color(
                    select_c.value
                ).scale(scheme="rainbow").legend(True)
            )
            .properties(width=500, height=500, grid=True, title=f"CROSS PLOT {select_x.value} x {select_y.value}")
            .interactive()
    )
    return (cross_plot_chrt,)


@app.cell
def _(
    cross_plot_chrt,
    mo,
    select_c,
    select_x,
    select_xlog_scale,
    select_y,
    select_ylog_scale,
):
    mo.vstack([mo.md(""""""), mo.vstack([cross_plot_chrt, mo.md(f"""

    | Config |     | Options    | Log      |
    | :----: | --- | :--------  | :------ |
    | X Axis |     | {select_x} | {select_xlog_scale} |
    | Y Axis |     | {select_y} | {select_ylog_scale} |
    | Color  |     | {select_c} |   |

    """), ])], align="center").center()
    return


@app.cell
def _():
    return


@app.cell
def _(get_values_from_table, tb, update_table_button):
    if update_table_button.value:
        pass
    tb_val = {x["Log"]:get_values_from_table(x) for x in tb.value}
    return (tb_val,)


@app.cell(hide_code=True)
def _(get_lims):
    def get_values_from_table(selected_row: dict) -> dict:
        out = {}
        for param, value in selected_row.items():
            try:
                    out[param] = value.value
            except:
                    out[param] = value

        _min = out.pop("Min")
        _max = out.pop("Max")
        min_max = out.pop("Min-Max")

        if "auto" == min_max:
            _min, _max = get_lims(out["Log"])
        out["Min-Max"] = (_min, _max)
        return out

    return (get_values_from_table,)


@app.cell
def _(well):
    from operator import abs
    def get_lims(log: str) -> tuple[int|float, int|float]:
        """Get value bounds for `log`"""
        _max = well[log].max()
        _min = well[log].min()
        _pad = abs(_max - _min) // 8
        return (_max+_pad, _min - _pad)
    return (get_lims,)


if __name__ == "__main__":
    app.run()
