# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "marimo==0.14.15",
# ]
# ///

import marimo

__generated_with = "0.14.15"
app = marimo.App()


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""# Basic""")
    return


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _():
    a = 10
    return (a,)


@app.cell
def _():
    b = 100
    return (b,)


@app.cell(hide_code=True)
def _(a, b):
    print(f"""
    We have {a = }

    and

    {b = }
    """)
    return


@app.cell
def _():
    # we cannot re-assign a again cz it will cause confusion of the order of execution
    # uncomment below line and see yourself

    # a = 15
    return


@app.cell
def _(a, b, c, mo):
    mo.md(
        f"""
    We have {a = }

    and

    {b = }

    and where is {c = }, tho?

    c is devined it the cell located at bottom of this notebook!
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""# `marimo.ui`""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    What is realy interesing about marimo is its reactivity

    We will use `marimo.ui.slider` and `marimo.md` to demonstrate this


    ---

    We can ma construct an f-string and pass it to `marimo.md` and marimo will give us back an html that nicely rendered
    """
    )
    return


@app.cell
def _(mo):
    slider_a = mo.ui.slider(label="Slider a", value=10, step=1, start=1, stop=20)
    number_b = mo.ui.number(label="Numebr b", value=10)

    slider_a, number_b
    return (slider_a,)


@app.cell(hide_code=True)
def _(mo, slider_a):
    mo.md(
        f"""
    As you can see above, that is a nice slider and an input field.

    the cool part is we can acces its value by using dot notation to access its `value` property

    {slider_a.value = }

    > try slide the slider or change the number and see the immidiate change


    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    And you can do things like following, too

    Crying ({slider_a.value} + {number_b.value}) times

    {"😭" * (slider_a.value + number_b.value)}
    """
    )
    return


@app.cell(hide_code=True)
def _():
    c = 90
    return (c,)


if __name__ == "__main__":
    app.run()
