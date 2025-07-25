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


@app.cell(column=0, hide_code=True)
def _(mo):
    mo.md(r"""## 1. Loading and Displaying Well Data From CSV""")
    return


@app.cell
def _():
    import marimo as mo
    return (mo,)


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

    - Not using `numpy`,

    - Visualize things using `altair` instead of `matplotlib`
    """
    )
    return


@app.cell(column=1, hide_code=True)
def _(mo):
    mo.md(r"""## Lock in the CSV and clean them!!""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""The following tutorial illustrates loading basic well log data from a csv file by using polars, and displaying the data using altair.""")
    return


@app.cell
def _():
    import polars as pl
    # import hvplot as hv
    import altair as alt
    return alt, pl


@app.cell
def _():
    return


@app.cell
def _(mo, pl):
    raw_well = pl.read_csv(str(mo.notebook_location() / "public" / "data/L0509WellData.csv"))
    return (raw_well,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    To check that the data has been loaded in correctly, we can use
    the `.head()` function in pandas to view the first 5 rows and the
    header.

    > polars has the same method as pandas has
    """
    )
    return


@app.cell
def _(raw_well):
    raw_well.head()
    return


@app.cell(hide_code=True)
def _(mo, raw_well):
    mo.vstack(
        [
            mo.md(
                r"""Here inside marimo, you can directly interact with your dataframe, how convinient is that?."""
            ).callout(kind="info"),

            raw_well,

            mo.md(
                r"""You can dowload this file, too, do you see the `download` button on the bottom-right corner of following tabel? yeah, try it out."""
            ).callout(kind="warn"),

        ]
    ).callout()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Just like `pandas` did, We can also view some statistics on the curves by using the `describe()` function.""")
    return


@app.cell
def _(raw_well):
    raw_well.describe()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    Before carrying out any displaying of data or calculations, we
    carry out some data cleansing. The first is the conversion of null values,
    represented by `-999.25`, to a Not a Number (`NaN`). We can achieve this using
    the replace function.

    ### Using `pandas`

    ```python
    well_dataframe.replace(-999.0, np.nan, inplace=True)
    ```

    or

    ```python
    well_dataframe.replace(-999.0, float('nan'), inplace=True)
    ```


    ### Using `polars`

    ```python
    _s = dict() # make an empty map as container

    for col in well_dataframe.columns: # iterate through the column name

        # take the column name, and replace the desired value
        # whilst assign it to the empty map as we iterating through
        _s[col] = well_dataframe[col].replace(-999, float("nan")) 

    # then we make a new polars.DataFrame just by
    # passing the container we've had and processed before
    new_well = pl.DataFrame(_s)
    ```
    """
    )
    return


@app.cell
def _(pl, raw_well):
    _s = dict()
    for col in raw_well.columns:
        _s[col] = raw_well[col].replace(-999, float("nan"))
    well = pl.DataFrame(_s)
    return (well,)


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
    mo.md(
        r"""
    By default, the `well.head()` function produces the first 5 rows of data. We can extend this by passing in a value to the head function.


    ```python
    well_dataframe.head(5)
    ```
    """
    )
    return


@app.cell
def _(well):
    well.head(20)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    Now we have some data appearing in the GR column.


    >
    > Note 💡
    >
    > you can always show the code of the notebook by clicking the `three dots` button on the top-right corner of this page.
    """
    )
    return


@app.cell(column=2, hide_code=True)
def _(mo):
    mo.md(r"""## Viewing Data on a Log Plot""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    With pandas, we can quickly bring up a plot of our well data by using the `.plot()` function on our well dataframe. <br><br>If we just specify the x and y axis, we can generate a simple line plot.


    ```python
    well_dataframe.plot(x="GR", y="DEPTH")
    ```

    ---

    However, we are using `polar` rn, since this is a WASM notebook, thx to marimo and uv, btw.
    We are going to use `altair` since that is the very the most marimo's supported visualization tool


    with that being said, for my `pandas x matplotlib` folks, i hear you guys!, y'all will be going to encounter a lot of alien plottin API from this point, just remember, you can always toggle wether to show or hide the code by the `[...]` button at the top-right corner.
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    However, while using marimo, we can escalate things to a whole another level.

    we can use `marimo.ui` API to access plenty of widgets that serve us a handy tool to take user input

    ```python
    selection_demo = well_daframe.columns
    select_log_demo = mo.ui.radio(selection_demo[1:], # we filter out "DEPTH" entry
                             value="GR", inline=True)
    select_log_scale_demo = mo.ui.switch(label="Logarithmic scale?", value=False)
    ```

    we will get something like below
    """
    )
    return


@app.cell(hide_code=True)
def _(mo, well):
    selection_demo = well.columns
    select_log_demo = mo.ui.radio(selection_demo[1:], # we filter out "DEPTH" entry
                             value="GR", inline=True)
    select_log_scale_demo = mo.ui.switch(label="Logarithmic scale?", value=False)
    return select_log_demo, select_log_scale_demo


@app.cell(hide_code=True)
def _(mo, select_log_demo, select_log_scale_demo):
    mo.md(
        f"""
    {mo.vstack([select_log_demo, select_log_scale_demo]).callout(kind="warn")}

    You can try select things from above and see their value change

    `select_log_demo` has value >> `{select_log_demo.value}`

    `select_log_scale_demo` has value >> `{select_log_scale_demo.value}`


    --

    we can access their value using `.` dot notation to their `value` property
    like this

    ```python
    select_log_scale_demo.value
    ```
    """
    )
    return


@app.cell(hide_code=True)
def _(mo, well):
    selection = well.columns
    select_log = mo.ui.radio(selection[1:], value="GR", inline=True)
    select_log_scale = mo.ui.switch(label="Logarithmic scale?", value=False)
    return select_log, select_log_scale, selection


@app.cell
def _():
    return


@app.cell
def _(alt, mo, select_log, select_log_scale, well):
    _xlim = (well[select_log.value].max()+0.001, well[select_log.value].min() - 0.001)
    _ylim = (well["DEPTH"].max()+10, well["DEPTH"].min() - 10)

    _chrt = (
        alt.Chart(well)
            .mark_line(color='blue', point=False,)
            .encode(
                alt.X(select_log.value, scale=alt.Scale(domain=_xlim)).scale(
                    zero=False, type="log" if select_log_scale.value else "linear"),
                alt.Y('DEPTH', sort = 'descending',scale=alt.Scale(domain=_ylim)),
                order = 'DEPTH')
            # .configure_mark(color = 'red', size=0.15, fillOpacity=0.5)
            .properties(width=300, height=800,)
            .interactive()
    )

    _md1 = mo.md(f"""
    ### Now we use that to make our interactive plot
    """)

    _md2 = mo.md(f"""
    Select a log to plot:

    {select_log}

    {select_log_scale}

    logarithmic scale: {select_log_scale.value}
    """)

    mo.vstack([
        _md1.center(),
        mo.hstack([
            _md2.center(),
            mo.ui.altair_chart(_chrt)
        ], widths=[0.2, 0.8])
    ])
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    >
    > Note 💡
    >
    > you can always show the code of the notebook by clicking the `three dots` button on the top-right corner of this page.
    """
    )
    return


@app.cell(column=3, hide_code=True)
def _(mo):
    mo.md(r"""## Cross Plot""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    We can change the type of plot by using the keyword kind and
    passing in the word scatter. In this example we have a familiar density
    neutron crossplot. <b>Note</b> that we can change the `y-axis` scales so that
    they are flipped and show increasing porosity as you move up the axis.

    >
    > Note 💡
    >
    > you can always show the code of the notebook by clicking the `three dots` button on the top-right corner of this page.
    """
    )
    return


@app.cell
def _(alt, mo, well):
    _chrt = mo.ui.altair_chart(
        alt.Chart(well)
            .mark_point(color='blue', filled=True)
            .encode(alt.X("NPHI",).scale(zero=False), alt.Y('RHOB',).scale(zero=False),)
            .properties(width=500, height=500,)
            .interactive()
    )
    _chrt.center()
    return


@app.cell
def _(mo, selection):
    select_x = mo.ui.radio(selection[1:], value="NPHI", inline=True)
    select_y = mo.ui.radio(selection[1:], value="RHOB", inline=True)
    select_xlog_scale = mo.ui.switch(label="Log scale?", value=False)
    select_ylog_scale = mo.ui.switch(label="Log scale?", value=False)
    select_c = mo.ui.radio(selection, value="GR", inline=True)
    return select_c, select_x, select_xlog_scale, select_y, select_ylog_scale


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
def _(mo, select_c, select_x, select_xlog_scale, select_y, select_ylog_scale):
    mo.md(f"""Select me, bro!

    | Config |     | Options    | Log      |
    | :----: | --- | :--------  | :------ |
    | X Axis |     | {select_x} | {select_xlog_scale} |
    | Y Axis |     | {select_y} | {select_ylog_scale} |
    | Color  |     | {select_c} |   |

    """).center()#.callout()
    return


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
    _chrt = mo.ui.altair_chart(
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
    _chrt.center()
    return


if __name__ == "__main__":
    app.run()
