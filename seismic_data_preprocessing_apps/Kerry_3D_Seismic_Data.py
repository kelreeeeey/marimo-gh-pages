# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "marimo==0.14.13",
#     "pandas>=2.0.3",
#     "pyarrow==21.0.0",
#     "altair==5.5.0",
#     "hvplot==0.11.3",
#     "polars==1.30.0",
#     "numpy>=1.26.4",
# ]
# ///

import marimo

__generated_with = "0.14.13"
app = marimo.App(width="columns")

@app.cell(column=0, hide_code=True)
def _(mo):
    mo.md(r"""## Kerry 3D Seismic Data""")
    return


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    Created By: [AN YU](https://github.com/anyuzoey)

    Original Repo: [SEGY2NUMPY](https://github.com/anyuzoey/SEGY2NUMPY.git)

    Through: [Wiki SEG - Kerry 3D](https://wiki.seg.org/wiki/Kerry-3D)

    ---

    Modified By: [T. S. Kelrey](https://github.com/kelreeeeey)

    As one of main process for my Undergrad Thesis project. (Thank God it's just finished.)

    ---
    """
    )
    return

@app.cell
def _():
    import segyio
    return (mo,)


if __name__ == "__main__":
    app.run()
