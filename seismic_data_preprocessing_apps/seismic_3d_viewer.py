# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "marimo",
#     "threey==0.0.12","
#     "polars","
# ]
# ///

import marimo

__generated_with = "0.18.4"
app = marimo.App(width="medium", sql_output="polars")


@app.cell
def _(area):
    area
    return


@app.cell
def _(mo):
    # load the data
    import polars as pl
    # _dir = mo.notebook_location() / "public/data"

    # the data's axis are configured to be in this order
    # axis 0: vertical slice / z / xy-plane
    # axis 1 and 2: could be any of the vertical planes, xz-plane or yz-plane
    # z axis is perpendicular to earth surface, not the computer screen :D
    _seis_csv = pl.read_csv(("https://raw.githubusercontent.com/kelreeeeey/threey/main/example-data/seismic_cube_shape_128_128_128.csv"))['data']
    _fault_csv = pl.read_csv(("https://raw.githubusercontent.com/kelreeeeey/threey/main/example-data/fault_cube_shape_128_128_128.csv"))['data']


    synthetic_data = _seis_csv.to_numpy().reshape((128, 128, 128))
    synthetic_fault_data = _fault_csv.to_numpy().reshape((128,128,128))
    return synthetic_data, synthetic_fault_data


@app.cell
def _(Seismic3DViewer, mo, synthetic_data, synthetic_fault_data):
    vmin, vmax = synthetic_data.min(), synthetic_data.max()

    # the widget takes memoryview of both the seismic data & the label
    sample_cube = memoryview(synthetic_data)
    sample_label = memoryview(synthetic_fault_data)

    labels = {"fault":sample_label}
    kwargs_labels = {"fault":dict(cmap="inferno", alpha=0.5)} # store the colormap and alpha for the label here!

    _dimensions = dict(
        inline=sample_cube.shape[1],
        crossline=sample_cube.shape[2],
        depth=sample_cube.shape[0]
    )

    area = mo.ui.anywidget(
        Seismic3DViewer(
            data_source = sample_cube,
            cmap_data = "seismic", # default to "seismic"
            dark_mode=False if mo.app_meta().theme != "dark" else True,
            labels=labels,
            kwargs_labels=kwargs_labels,
            show_label= False,
            vmin = vmin,
            vmax = vmax,
            is_2d_view = False, # default to True
            dimensions=_dimensions,
            height=500
        )
    )
    return (area,)


@app.cell
async def _():
    import marimo as mo
    import numpy as np
    import micropip
    await micropip.install("threey")
    from threey import Seismic3DViewer
    return Seismic3DViewer, mo


if __name__ == "__main__":
    app.run()
