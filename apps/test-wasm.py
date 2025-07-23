import marimo

__generated_with = "0.14.12"
app = marimo.App(width="full")


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _(mo):
    slider = mo.ui.slider(1, 10, 1, label="")
    return (slider,)


@app.cell
def _(mo, slider):
    mo.md(
        f"""
        marimo is a **reactive** Python notebook.

        Slide me, dude { slider }

        { "##" + "🍃" * slider.value }
        """)
    return


if __name__ == "__main__":
    app.run()
