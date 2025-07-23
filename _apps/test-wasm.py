import marimo

__generated_with = "0.14.12"
app = marimo.App(width="columns")


@app.cell(column=0)
def _():
    import marimo as mo
    from mydict import hello
    return hello, mo


@app.cell
def _(mo):
    slider = mo.ui.slider(1, 10, 1, label="")
    return (slider,)


@app.cell
def _(mo):
    number = mo.ui.number(1, 10, 1, label="")
    return (number,)


@app.cell
def _(hello, mo, number, slider):
    mo.md(
        f"""
        marimo is a **reactive** Python notebook.

        Slide me, dude { slider }

        { "##" + "🍃" * slider.value }

        How about {number}

        { "##" + "🥲" * number.value }
        """)
    hello()
    return


@app.cell
def _():
    return


@app.cell(column=1)
def _(mo, number, slider):
    mo.md(
        f"""
    marimo is a **reactive** Python notebook.

    Slide me, dude { slider }

    { "##" + "🍃" * slider.value }

    How about {number}

    { "##" + "🥲" * number.value }
    """
    )
    return


if __name__ == "__main__":
    app.run()
