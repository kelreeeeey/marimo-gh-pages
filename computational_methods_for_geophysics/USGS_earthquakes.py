# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "marimo==0.14.15",
#     "numpy==1.26.4",
#     "pandas>=2.0.3",
#     "pyarrow==21.0.0",
#     "altair==5.5.0",
#     "polars==1.30.0",
#     "plotly==6.2.0",
#     "urllib3==2.5.0",
# ]
# ///

import marimo

__generated_with = "0.14.15"
app = marimo.App(width="full")


@app.cell
def _():
    import marimo as mo
    # import requests
    import json
    import datetime as dt
    from io import BytesIO
    return BytesIO, dt, mo


@app.cell
def _():
    # import polars as pl
    import pandas as pd
    import plotly.express as px
    import altair as alt
    import plotly.graph_objects as go
    return alt, go, pd, px


@app.cell
def _():
    ACCEPTABLE_ORDER = ["time", "time-asc", "magnitude", "magnitude-asc"]
    ACCEPTABLE_FORMAT = ["csv",]# "geojson"]
    return ACCEPTABLE_FORMAT, ACCEPTABLE_ORDER


@app.cell
def _():
    import urllib3
    return (urllib3,)


@app.cell
def _():
    FORMAT: str = "csv"
    BASE_URL: str = "http://earthquake.usgs.gov/fdsnws/event/1/query?format={format}"
    START_DATE: str = "2015-12-09%2000:00:00"
    END_DATE: str = "2020-12-16%2023:59:59"
    ORDERBY: str = "magnitude"
    MINMAGNITUDE: float = 5.0
    MAXMAGNITUDE: float = 8.0
    LIMIT: int = 20000
    return (
        BASE_URL,
        END_DATE,
        FORMAT,
        LIMIT,
        MAXMAGNITUDE,
        MINMAGNITUDE,
        ORDERBY,
        START_DATE,
    )


@app.cell
def _(
    ACCEPTABLE_FORMAT,
    ACCEPTABLE_ORDER,
    END_DATE: str,
    FORMAT: str,
    LIMIT: int,
    MAXMAGNITUDE: float,
    MINMAGNITUDE: float,
    ORDERBY: str,
    START_DATE: str,
    mo,
    str2datetime,
):
    form_query = mo.md("""

    ## Query for Data Request of Earthquake events to `earthquake.usgs.gov`

    ---

    Query format: {format}

    Range date of events: {event_date}

    Minimum Magnitude: {minmagnitude}

    Maximum Magnitude: {maxmagnitude}

    Order by: {orderby}

    Limit: {limit} (maximum 20,000 records)

    ---
    """).batch(
        format = mo.ui.radio(options=ACCEPTABLE_FORMAT, value=FORMAT, inline=True),
        event_date=mo.ui.date_range(start=str2datetime(START_DATE).date(), stop=str2datetime(END_DATE).date()),
        minmagnitude=mo.ui.number(start=0.1, step=0.01, stop=10.0, value=MINMAGNITUDE),
        maxmagnitude=mo.ui.number(start=0.1, step=0.01, stop=10.0, value=MAXMAGNITUDE),
        limit=mo.ui.number(start=1, step=1, stop=LIMIT, value=LIMIT-5000),
        orderby=mo.ui.radio(options=ACCEPTABLE_ORDER, value=ORDERBY, inline=True)
    ).form(bordered=False, submit_button_label="Submit query form", loading=False)
    mo.vstack([form_query.center().callout(kind="warn"), mo.md("THIS NOTEBOOK IS IMPLEMENTING `http.request` to fetch data from `earthquake.esgs.gov`.<br>The implementation can always be seen in this notebook by the button on the top right corner of this page<br>And if you would, you may also need to allow something in your browser in order for this website to run.").callout(kind="danger")], align="center", gap=0)#.callout()
    return (form_query,)


@app.cell
def _():
    return


@app.cell
def _(form_query, mo):
    mo.stop(form_query.value is None, mo.md("**Submit the form to continue.**").center())
    return


@app.cell
def _(BASE_URL: str, form_query):
    if form_query.value:
        input_start_date, input_end_date = list(map(str, form_query.value["event_date"]))
        query_url  = f'{BASE_URL.format(format=form_query.value["format"])}'
        query_url += f'&starttime={input_start_date}&endtime={input_end_date}'
        query_url += f'&minmagnitude={form_query.value["minmagnitude"]}'
        query_url += f'&orderby={form_query.value["orderby"]}'
        query_url += f'&limit{form_query.value["limit"]}'
        query_url += f'&maxmagnitude{form_query.value["maxmagnitude"]}'

    return (query_url,)


@app.cell
def _(mo):
    button_start_query = mo.ui.run_button(label=fr"Start Query", kind="danger")
    button_start_query.center()
    return (button_start_query,)


@app.cell
def _(mo):
    mo.md("""---""")
    return


@app.cell
def _():
    return


@app.cell
def _(
    BytesIO,
    agregate_items,
    button_start_query,
    form_query,
    mo,
    pd,
    query_url,
    urllib3,
):
    button_start_query
    http = urllib3.PoolManager()
    if form_query.value and button_start_query.value:
        with mo.status.spinner(title="Loading...", remove_on_exit=True) as _spinner:
            _spinner.update("Fetching the data", subtitle=f"from {query_url}")
            # _response = requests.get(query_url)
            _response = http.request('GET', query_url)
            _spinner.update("Almost done")
            # print(_response.status, _response.info())
            # if _response.status_code == 200:
            if _response.status == 200:
                _spinner.update("Success")
                query_msg = mo.as_html("Success")
                if "csv" == form_query.value["format"]:
                    fetched_data = pd.read_csv(BytesIO(_response.data))#, infer_schema_length=10_000)
                    # fetched_data = pd.read_csv(BytesIO(_response.content))#, infer_schema_length=10_000)
                else:
                    raw_fetched_data = _response.json()  # For JSON data
                    fetched_data = pd.DataFrame(map(agregate_items, raw_fetched_data.pop('features')))#, infer_schema_length=10_000)
            else:
                _spinner.update("Failed")
                query_msg = mo.as_html(_response.status)
                # query_msg = mo.as_html(_response.content)
                fetched_data = pd.DataFrame()

    else:
        query_msg = mo.md("").center()
        fetched_data = pd.DataFrame()

    http.clear()
    query_msg
    return (fetched_data,)


@app.cell
def _(fetched_data, form_query, mo):
    if 0 != form_query.value and len(fetched_data):
        _md = mo.md(f"""
    # Earthquakes across the globe from `{form_query.value['event_date'][0]}` to `{form_query.value['event_date'][1]}` with  `({form_query.value['minmagnitude']} <= magnitude < {form_query.value['maxmagnitude']})`
    """)
    else:
        _md = mo.as_html("")

    _md.center()
    return


@app.cell
def _(fetched_data, mo):
    if 0 == len(fetched_data):
        _md = mo.md("**Your query is an empty data, change the query configs to continue!**").center()
    else:
        _md = fetched_data
    _md
    return


@app.cell
def _(button_start_query, fetched_data, form_query, mo):
    if 0 == len(fetched_data) and button_start_query.value:
        _h = mo.md(f"""_you were asking for_ `{form_query.value}`""")
    else:
        _h = mo.as_html("").center()
    _h
    return


@app.cell
def _(MAP_STYLES, fetched_data, form_query, mo):
    if form_query.value and 0 != len(fetched_data):
        fetched_data_columns = fetched_data.columns
        hover_name_selection = mo.ui.dropdown(
            options=fetched_data_columns,
            value="place",
            label="Choose hover type",
            searchable=True,
        )
        map_style_selection = mo.ui.dropdown(
            options=MAP_STYLES,
            value="basic",
            label="Choose a map style",
            searchable=True,
        )
        filter_dataset_by = 0
        _md = mo.vstack([
            mo.hstack([hover_name_selection, map_style_selection, mo], justify="center",),
            mo.md("## Select a region on the map")
        ], align="center")
    else:
        _md = mo.as_html("")
    _md.center()
    return fetched_data_columns, hover_name_selection, map_style_selection


@app.cell(hide_code=True)
def _():
    MAP_STYLES = [
        "basic",
        "carto-darkmatter",
        "carto-darkmatter-nolabels",
        "carto-positron",
        "carto-positron-nolabels",
        "carto-voyager",
        "carto-voyager-nolabels",
        "dark",
        "light",
        "open-street-map",
        "outdoors",
        "satellite",
        "satellite-streets",
        "streets",
        "white-bg"
    ]
    return (MAP_STYLES,)


@app.cell
def _(fetched_data):
    filtered_fetched_data = fetched_data
    return (filtered_fetched_data,)


@app.cell
def _(
    fetched_data,
    fetched_data_columns,
    filtered_fetched_data,
    form_query,
    go,
    hover_name_selection,
    map_style_selection,
    mo,
    px,
):
    if form_query.value and 0 != len(fetched_data):
        fig = go.Figure(px.scatter_map(filtered_fetched_data, lat="latitude", lon="longitude",
                                       hover_name=hover_name_selection.value, hover_data=fetched_data_columns,
                                       color="mag", color_continuous_scale="jet", zoom=1, height=650, width=1450, template=None))
        fig.update_geos(resolution=50, projection_type="natural earth", lataxis_showgrid=True, lonaxis_showgrid=True)
        fig.update_layout(map_style=map_style_selection.value)
        fig.update_layout(dragmode='select', activeselection=dict(fillcolor='yellow'))
        fig.update_layout(margin={"r":0,"t":0,"l":350,"b":0})
        mo_plot = mo.ui.plotly(fig)
    else:
        fig = mo.ui.checkbox(value=False) # mo.as_html("").center()
        mo_plot = mo.as_html(fig)
    mo_plot.center()
    return (mo_plot,)


@app.cell
def _(alt, form_query, mo, pd, selected_df):
    if not (form_query.value and 0 != len(selected_df)):
        final_chart = mo.as_html("")
    else:
            # Convert 'time' to datetime and extract year
        selected_df['time'] = pd.to_datetime(selected_df['time'])
        selected_df['year'] = selected_df['time'].dt.year

        # Aggregate by year (count and mean magnitude)
        summary = selected_df.groupby('year').agg(
            earthquake_count=('mag', 'count'),
            avg_magnitude=('mag', 'mean'),
            avg_depth=('depth', 'mean')
        ).reset_index()

        # Plot 1: Number of Earthquakes per Year
        count_chart = alt.Chart(summary).mark_bar().encode(
            x='year:O',  # 'O' for ordinal (discrete)
            y='earthquake_count:Q',
            tooltip=['year', 'earthquake_count']
        ).properties(
            title='Earthquakes per Year',
            width=450,
            # heigth=1000
        )

        # Plot 2: Average Magnitude per Year
        mag_chart = alt.Chart(summary).mark_bar(color='red').encode(
            x='year:O',
            y='avg_magnitude:Q',
            tooltip=['year', 'avg_magnitude']
        ).properties(
            title='Average Magnitude by Year',
            width=450,
            # heigth=1000
        )
        depth_chart = alt.Chart(summary).mark_bar(color='green').encode(
            x='year:O',
            y='avg_depth:Q',
            tooltip=['year', 'avg_depth']
        ).properties(
            title='Average Depth by Year',
            width=450,
            # heigth=1000
        )

        # Combine both charts vertically
        final_chart = mo.ui.altair_chart(alt.hconcat(count_chart, mag_chart, depth_chart))
    final_chart.center()
    return


@app.cell
def _(fetched_data, form_query, mo, mo_plot, pd):
    if form_query.value and 0 != len(fetched_data):
        selected_df = pd.DataFrame(mo_plot.value)
    else:
        selected_df = mo.as_html("").center()

    # mo.ui.table(data=mo_plot.value)
    selected_df
    return (selected_df,)


@app.cell
def _(dt):
    def str2datetime(date_str) -> dt.datetime:
        if "%20" in date_str:
            return dt.datetime.strptime(date_str.replace("%20", " "), "%Y-%m-%d %H:%M:%S")
        else:
            return dt.datetime.strptime(date_str, "%Y-%m-%d")

    def datetime2str(dt_obj, had_time=False) -> str:
        if had_time:
            return dt_obj.strftime("%Y-%m-%d%20H:%M:%S").replace(" ", "%20")
        else:
            return dt_obj.strftime("%Y-%m-%d")
    return (str2datetime,)


@app.cell
def _():
    # TEMPLATE_COORD_IDX = ['lat', 'lon', 'depth']
    # get_coords = lambda x: dict(zip(TEMPLATE_COORD_IDX, x.get("coordinates", [0, 0, 0])))
    # def agregate_items(raw_json: dict) -> dict:
    #     _properties  = {"event-id":raw_json.get("id", "")}
    #     _properties |= {"type":raw_json.get("type", "")}
    #     _properties |= get_coords(raw_json.get("geometry", dict()))
    #     _properties |= raw_json.get("properties", dict())
    #     return _properties
    return


if __name__ == "__main__":
    app.run()
