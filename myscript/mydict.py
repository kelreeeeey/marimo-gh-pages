import marimo

__generated_with = "0.14.12"
app = marimo.App(width="columns")


@app.cell(column=0)
def _():
    import marimo as mo
    return (mo)

@app.function
def hello():
    print("Hello from mydict")
    return None

if __name__ == "__main__":
    app.run()

