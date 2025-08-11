import marimo

__generated_with = "0.14.16"
app = marimo.App(width="medium", sql_output="polars")

with app.setup:
    # Initialization code that runs before all other cells
    import marimo as mo


@app.cell
def _():
    return


@app.cell
def _():
    from pathlib import Path
    return (Path,)


@app.cell
def _():
    import random
    import asyncio
    return asyncio, random


@app.cell
def _():
    mo.vstack(
        [
            mo.md(
                rf"""
    # What is marimo

    Well, marimo is a brand new Python notebook which is the re-invention of Jupyter notebook.

    """
            ),
        ],
        align="stretch",
    )
    return


@app.cell(hide_code=True)
def _():
    mo.accordion(
        {
            "_More to read_": mo.iframe(
                "https://kelreeeeey.github.io/yap/Marimo-Notebooks#ok-the-things-that-make-me-rethink-why-i-still-use-jupyter-notebook"
            )
        },
    )
    return


@app.cell
def _():
    mo.md(
        r"""
    # Ways of getting started
    /// details | <b style="color:black">1. In your local</b>
        type: info

    1. `pip install marimo`
    2. marimo edit notebooks.py

    ///

    /// details | <b style="color:red">2. In our server (prefered!)</b>
        type: info

    > <a href="https://kelreeeeey.github.io/marimo-gh-pages/notebooks/marimo_notebook.html">https://kelreeeeey.github.io/marimo-gh-pages/notebooks/marimo_notebook.html</a>


    ///

    /// details | <b style="color:grey">3. In my personal WASM Github Page</b>
        type: info

    > <a href="https://kelreeeeey.github.io/marimo-gh-pages/notebooks/marimo_notebook.html">https://kelreeeeey.github.io/marimo-gh-pages/notebooks/marimo_notebook.html</a>


    ///
    """
    )
    return


@app.cell
def _():
    mo.md(r"""# Actually getting started""")
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""## Those basic UIs""")
    return


@app.cell
def _():
    show_code = mo.ui.switch(label="Show code")
    show_code
    return (show_code,)


@app.cell
def _():
    number = mo.ui.number(label="Number", value=10)
    slider = mo.ui.slider(
        label="Slider", value=10, start=1, stop=100, include_input=True
    )
    dropdown = mo.ui.dropdown(
        options=["Apples", "Oranges", "Pears"], label="choose fruit"
    )
    dropdown_dict = mo.ui.dropdown(
        options={"Apples": 1, "Oranges": 2, "Pears": 3},
        value="Apples",  # initial value
        label="choose fruit with dict options",
    )
    wish = mo.ui.text(placeholder="Wish")
    wishes = mo.ui.array([wish] * 3, label="Three wishes")
    button_incerement = mo.ui.button(
        value=0, on_click=lambda value: value + 1, label="increment", kind="warn"
    )
    checkbox = mo.ui.checkbox(label="check me")
    date = mo.ui.date(label="Start Date")

    _first_name = mo.ui.text(placeholder="First name")
    _last_name = mo.ui.text(placeholder="Last name")
    _email = mo.ui.text(placeholder="Email", kind="email")

    dictionary = mo.ui.dictionary(
        {
            "First name": _first_name,
            "Last name": _last_name,
            "Email": _email,
        },
        label="dictionary",
    )
    _options = ["Apples", "Oranges", "Pears"]
    multiselect = mo.ui.multiselect(label="Multiselect", options=_options)
    radio_normal = mo.ui.radio(label="Radio normal", options=_options)
    radio_inline = mo.ui.radio(label="Radio inline", options=_options, inline=True)
    range_slider = mo.ui.range_slider(
        label="Range Slider",
        start=1,
        stop=10,
        step=2,
        value=[2, 6],
        full_width=True,
    )
    switch = mo.ui.switch(label="Siwtch do not disturb")
    tabs = mo.ui.tabs(
        {
            "Bob says": mo.md("Hello, Alice! 👋"),
            "Alice says": mo.md("Hello, Bob! 👋"),
        }
    )

    mo.show_code()
    return (
        button_incerement,
        checkbox,
        date,
        dictionary,
        dropdown,
        dropdown_dict,
        multiselect,
        number,
        radio_inline,
        radio_normal,
        range_slider,
        slider,
        switch,
        tabs,
        wishes,
    )


@app.cell
def _(
    button_incerement,
    checkbox,
    date,
    dictionary,
    dropdown,
    dropdown_dict,
    multiselect,
    number,
    radio_inline,
    radio_normal,
    range_slider,
    slider,
    switch,
    tabs,
    wishes,
):
    uis = [
        number,
        slider,
        dropdown,
        dropdown_dict,
        wishes,
        button_incerement,
        checkbox,
        date,
        dictionary,
        multiselect,
        radio_normal,
        radio_inline,
        range_slider,
        switch,
        tabs,
    ]
    return (uis,)


@app.cell
def _(show_code, uis):
    _table = mo.ui.table(
        data=[{"ui": x, "ui.value": x.value} for x in uis],
        pagination=False,
    )
    if show_code.value:
        _ = mo.show_code(
            mo.md(
                f"""
    We can get the input using its value attribute

    {_table}
    """
            )
        )
    else:
        _ = mo.md(
            f"""
    We can get the input using its value attribute

    {_table}
    """
        )
    _
    return


@app.cell
def _():
    mo.md(r"""## Not that basic UIs""")
    return


@app.cell
def _():
    file = mo.ui.file(filetypes=[".png"], multiple=False)
    mo.show_code()
    return (file,)


@app.cell
def _(Path):
    file_browser = mo.ui.file_browser(initial_path=Path("../"), multiple=True)
    mo.show_code()
    return (file_browser,)


@app.cell
def _(file, file_browser):
    mo.md(
        f"""
    ### `mo.ui.file` and `mo.ui.file_browser()`
    /// details | Info details
        type: info

    We can get the input using its value attribute
    Upload a file <br> {file}

    Upload using selection <br> {file_browser}

    ///
    """
    )
    return


@app.cell(hide_code=True)
def _(file, file_browser):
    _file = (
        file.value,
        [x.name for x in file.value],
    )

    _file_browser = (
        file_browser.value,
        [x.path for x in file_browser.value],
        [x.name for x in file_browser.value],
    )

    (
        mo.md(f"""We can get the input using its value attribute"""),
        _file,
        _file_browser,
    )
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""### `mo.ui.refresh` and `mo.ui.run_button()`""")
    return


@app.cell(hide_code=True)
def _(show_code):
    refresh = mo.ui.refresh(
        label="Refresh to generate random number",
        options=["1s", "5s", "10s", "30s"],
    )
    if show_code.value:
        _ = mo.show()
    else:
        _ = None
    _
    return (refresh,)


@app.cell
def _(refresh):
    refresh
    return


@app.cell
def _(random, refresh):
    refresh.value
    mo.md(f"""generated random number: {random.randint(10, 100)}""")
    return


@app.cell
def _():
    first_button = mo.ui.run_button(label="Button 1", kind="warn")
    second_button = mo.ui.run_button(label="Button 2", kind="success")
    return first_button, second_button


@app.cell(hide_code=True)
def _(first_button, second_button):
    if first_button.value:
        _md = mo.md('<b style="color:orange">You chose option 1!</b>')
    elif second_button.value:
        _md = mo.md("You chose option 2!")
    else:
        _md = mo.md("Click a button!")
    _md.center()
    return


@app.cell
def _(first_button):
    first_button.value
    return


@app.cell
def _(first_button, second_button):
    mo.hstack([first_button, second_button], justify="space-around", gap=-1)
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""## Layouts""")
    return


@app.cell
def _(uis):
    _a = mo.accordion(
        {
            "Door 1": "Nothing!",
            "Door 2": mo.ui.table(
                data=[{"ui": x, "ui.value": x.value} for x in uis],
                pagination=False,
            ).callout(),
            "Door 3": mo.md(
                "![goat](https://images.unsplash.com/photo-1524024973431-2ad916746881)"
            ),
        }
    )

    mo.md(f"""### `mo.accordion()`

    {_a}
    """).callout()
    return


@app.cell
def _():
    mo.md(r"""### `mo.callout()`""")
    return


@app.cell
def _():
    callout_kind = mo.ui.dropdown(
        label="Color",
        options=["info", "neutral", "danger", "warn", "success"],
        value="neutral",
    )
    return (callout_kind,)


@app.cell
def _(callout_kind):
    callout = mo.callout("This is a callout", kind=callout_kind.value)
    return (callout,)


@app.cell
def _(callout, callout_kind):
    mo.vstack([callout_kind, callout], align="stretch", gap=0)
    return


@app.cell
def _():
    mo.md(r"""### `mo.carousel()`""")
    return


@app.cell
def _(uis):
    mo.carousel(
        [
            mo.md("Nothing!").center().callout(),
            mo.md(
                "![goat](https://images.unsplash.com/photo-1524024973431-2ad916746881)"
            ),
            mo.ui.table(
                data=[{"ui": x, "ui.value": x.value} for x in uis],
                pagination=False,
            ),
        ]
    )
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""### `Stacks()` and `mo.tree()`""")
    return


@app.function
def create_box(num=1):
    box_size = 30 + num * 10
    return mo.Html(
        f"<div style='min-width: {box_size}px; min-height: {box_size}px; background-color: orange; text-align: center; line-height: {box_size}px'>{str(num)}</div>"
    )


@app.cell
def _():
    boxes = [create_box(i) for i in range(1, 5)]
    justify = mo.ui.dropdown(
        ["start", "center", "end", "space-between", "space-around"],
        value="space-between",
        label="justify",
    )
    align = mo.ui.dropdown(
        ["start", "center", "end", "stretch"], value="center", label="align"
    )
    gap = mo.ui.number(start=0, step=0.25, stop=2, value=0.25, label="gap")
    wrap = mo.ui.checkbox(label="wrap")
    return align, boxes, gap, justify, wrap


@app.cell
def _(align, boxes, gap, justify, wrap):
    horizontal = mo.hstack(
        boxes,
        align=align.value,
        justify=justify.value,
        gap=gap.value,
        wrap=wrap.value,
    )
    vertical = mo.vstack(
        boxes,
        align=align.value,
        gap=gap.value,
    )

    mo.vstack(
        [
            mo.hstack([justify, align, gap], justify="center"),
            horizontal,
            mo.md("-----------------------------"),
            vertical,
        ],
        align="stretch",
        gap=1,
    )
    return


@app.cell
def _(uis):
    mo.tree(
        uis,
        label="A tree of elements.",
    )
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""## Another things""")
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""### `batch` and `form`""")
    return


@app.cell
def _():
    user_info_1 = mo.md(
        """
        - What's your name?: {name}
        - When were you born?: {birthday}
        """
    ).batch(name=mo.ui.text(), birthday=mo.ui.date())
    mo.show_code(user_info_1)
    return (user_info_1,)


@app.cell
def _(user_info_1):
    print(user_info_1.value)
    return


@app.cell
def _():
    user_info = (
        mo.md(
            """
        - What's your name?: {name}
        - When were you born?: {birthday}
        """
        )
        .batch(name=mo.ui.text(), birthday=mo.ui.date())
        .form()
    )
    mo.show_code(user_info)
    return (user_info,)


@app.cell
def _(user_info):
    print(user_info.value)
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""### Progress""")
    return


@app.cell
def _():
    rerun = mo.ui.button(label="Rerun")
    rerun
    return (rerun,)


@app.cell
async def _(asyncio, rerun):
    rerun
    for _ in mo.status.progress_bar(
        range(10),
        title="Loading",
        subtitle="Please wait",
        show_eta=True,
        show_rate=True,
    ):
        await asyncio.sleep(0.5)
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""### `mo.mermaid()`""")
    return


@app.cell
def _():
    mermaid = mo.mermaid(
        "graph LR\n  A[Christmas] -->|Get money| B(Go shopping)\n  B --> C{Let me think}\n  C -->|One| D[Laptop]\n  C -->|Two| E[iPhone]\n  C -->|Three| F[Car]"
    )
    mo.show_code(mermaid)
    return


@app.cell
def _():
    mo.md(
        r"""
    ## create reusable function, class, and anything


    hit `ctrl+k` or `command+k`,  and type `Add setup cell`
    """
    )
    return


@app.cell
def _():
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""## mo.watch()""")
    return


@app.cell
def _():
    # watch_file = mo.watch.file("./what.txt")
    mo.show_code()
    return


@app.cell
def _():
    # watch_file.read_text()
    mo.show_code()
    return


if __name__ == "__main__":
    app.run()
