# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "marimo==0.14.15",
#     "matplotlib==3.10.3",
#     "plotly==6.2.0",
# ]
# ///

import marimo

__generated_with = "0.14.15"
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def _():
    import marimo as mo
    import array as ar
    import matplotlib.pylab as plt
    import math
    from collections import namedtuple, UserList
    import plotly.graph_objects as go
    from plotly.subplots import make_subplots
    return UserList, ar, go, math, mo, namedtuple, plt


@app.cell(hide_code=True)
def _(mo):
    mo.hstack([

        mo.vstack([
            mo.md(
        rf"""
    # Gravitational Responses of 2 "imaginary" perfect sphere objects below surface

    A ball with density of \(\rho\) located at \(x,y,z\) below the surface will induce a vector field
    """
            ),
            mo.md(r"""# $\vec{g}(F_1) = -\gamma \frac{\frac{4}{3} \pi a^2 \rho}{R^2} \hat{r}$""").center(),
            mo.md(r"""**Where:**
        
            - \(\vec{g}(F_1)\) = Gravitational field at point \(F_1\) due to a mass distribution  
            - \(\gamma\) = Gravitational constant (also written as \(G\))  
            - \(a\) = Radius of the ball  
            - \(\rho\) = Mass density of the object (mass per unit volume or surface area depending on context)  
            - \(R\) = Distance from the center of the mass distribution to the point \(F_1\)  
            - \(\hat{r}\) = Unit vector pointing from the mass distribution to the point \(F_1\) (direction of the field)  
            - \(\frac{4}{3} \pi a^2\) = Volume of a ball
            """)], align="center"),
        mo.image(
            src=str(mo.notebook_location() / "public/gravity.jpeg"),
            width="800px", height="320px", rounded=True
        ).center(),
        mo.md("\n---")
    ], justify="start", align="center").center()


    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ---

    # The Exciting Part
    """
    )
    return


@app.cell(hide_code=True)
def _(math):
    GAMMA = 6.6E-11
    SI2MG = 1.0E5
    PI = math.pi
    KM2M = 1e3 # konversi satuan
    IERROR = 0
    NX = 200
    NY = 200

    LEFT = -50
    BOTTOM = -50
    RIGTH = 50
    TOP = 50
    return BOTTOM, GAMMA, KM2M, LEFT, NX, NY, PI, RIGTH, SI2MG, TOP


@app.cell(hide_code=True)
def _(namedtuple):
    Ball = namedtuple("Ball", ["r", "rho", "x", "y", "z"], defaults=[10.0, 90.0, 0, 0, 0])
    return (Ball,)


@app.cell
def _(BOTTOM, LEFT, NX, NY, RIGTH, TOP, linspace, meshgrid):
    x = linspace(LEFT, RIGTH, NX)
    y = linspace(BOTTOM, TOP, NY)
    xx, yy = meshgrid(x, y)
    return xx, yy


@app.cell
def _(
    Ball,
    NX,
    NY,
    density_ball_a,
    density_ball_b,
    myArr,
    radius_ball_a,
    radius_ball_b,
    slider_posx_ball_a,
    slider_posx_ball_b,
    slider_posy_ball_a,
    slider_posy_ball_b,
    slider_posz_ball_a,
    slider_posz_ball_b,
    zeros,
):
    ball_a = Ball(r=radius_ball_a.value, rho=density_ball_a.value, x=slider_posx_ball_a.value, y=slider_posy_ball_a.value, z=slider_posz_ball_a.value)
    ball_b = Ball(r=radius_ball_b.value, rho=density_ball_b.value, x=slider_posx_ball_b.value, y=slider_posy_ball_b.value, z=slider_posz_ball_b.value)
    G1  =myArr(zeros((NX,NY)))
    G1_a=myArr(zeros((NX,NY)))
    G1_b=myArr(zeros((NX,NY)))
    return G1, G1_a, G1_b, ball_a, ball_b


@app.cell(hide_code=True)
def _(UserList):
    class myArr(UserList):
        ndim = 2
    return (myArr,)


@app.cell(hide_code=True)
def _(G1, G1_a, G1_b, NX, NY, ball_a, ball_b, bola, math, xx, yy):
    MIN = math.inf
    MAX = -math.inf

    MIN_a = math.inf
    MAX_a = -math.inf

    MIN_b = math.inf
    MAX_b = -math.inf

    for i in range(NX):
        for j in range(NY):
            gx1, gy1, gz1 = bola(ball_a, xx[i][j], yy[i][j], -2)
            gx2, gy2, gz2 = bola(ball_b, xx[i][j], yy[i][j], -2)
            G1[i][j]=gz1+gz2
            G1_a[i][j]=gz1
            G1_b[i][j]=gz2

            if MIN > G1[i][j]:
                MIN = G1[i][j]
            if MAX < G1[i][j]:
                MAX = G1[i][j]

            if MIN_a > G1_a[i][j]:
                MIN_a = G1_a[i][j]
            if MAX_a < G1_a[i][j]:
                MAX_a = G1_a[i][j]

            if MIN_b > G1_b[i][j]:
                MIN_b = G1_b[i][j]
            if MAX_b < G1_b[i][j]:
                MAX_b = G1_b[i][j]

    return MAX, MAX_a, MAX_b, MIN, MIN_a, MIN_b


@app.cell(hide_code=True)
def _(input_ball_a, input_ball_b, mo):
    mo.hstack([input_ball_a, input_ball_b])
    return


@app.cell(hide_code=True)
def _(G1, G1_a, G1_b, MAX, MAX_a, MAX_b, MIN, MIN_a, MIN_b, mo, plt, xx, yy):
    fig, axes = plt.subplot_mosaic([["a", "a+b", "b"]], figsize=(15,5), sharey=True, layout="tight")
    fig.suptitle("Gravitational Field", fontsize=15)

    contour_a_b = axes["a+b"].contourf(xx, yy, G1, cmap="jet", vmin=MIN, vmax=MAX)
    axes["a+b"].set_title("Combine", fontsize=13, loc="left")
    axes["a+b"].grid(alpha=0.25)
    cbar_a_b = fig.colorbar(contour_a_b, ax=axes["a+b"])
    cbar_a_b.set_label('Gravity Response')

    contour_a = axes["a"].contourf(xx, yy, G1_a, cmap="coolwarm", vmin=MIN_a, vmax=MAX_a)
    axes["a"].set_title("Ball A", fontsize=13, loc="left")
    axes["a"].grid(alpha=0.25)
    cbar_a = fig.colorbar(contour_a, ax=axes["a"])
    cbar_a.set_label('Gravity Response')


    contour_b = axes["b"].contourf(xx, yy, G1_b, cmap="coolwarm", vmin=MIN_b, vmax=MAX_b)
    axes["b"].set_title("Ball B", fontsize=13, loc="left")
    axes["b"].grid(alpha=0.25)
    cbar_b = fig.colorbar(contour_b, ax=axes["b"])
    cbar_b.set_label('Gravity Response')

    for _, _ax in axes.items():
        _ax.set(ylabel="Y", xlabel="X")

    mo.as_html(plt.gca()).center()
    return


@app.cell(hide_code=True)
def _(
    density_ball_a,
    mo,
    radius_ball_a,
    slider_posx_ball_a,
    slider_posy_ball_a,
    slider_posz_ball_a,
):
    input_ball_a = mo.vstack(
        [
            mo.md(f"""## Ball A"""),
            mo.md(f"""
    - the larger Z the deeper the ball below the surface
    """),
            mo.hstack([slider_posx_ball_a, slider_posy_ball_a, slider_posz_ball_a], justify="start"),
            mo.hstack([radius_ball_a, density_ball_a], justify="start"),
        ]
    )#.callout()
    return (input_ball_a,)


@app.cell(hide_code=True)
def _(
    density_ball_b,
    mo,
    radius_ball_b,
    slider_posx_ball_b,
    slider_posy_ball_b,
    slider_posz_ball_b,
):
    input_ball_b = mo.vstack(
        [
            mo.md(f"""## Ball B"""),
            mo.md(f"""
    - the larger Z the deeper the ball below the surface
    """),
            mo.hstack([slider_posx_ball_b, slider_posy_ball_b, slider_posz_ball_b], justify="start"),
            mo.hstack([radius_ball_b, density_ball_b], justify="start"),
        ]
    )#.callout()
    return (input_ball_b,)


@app.cell(hide_code=True)
def _(ball_a, ball_b, mo):
    stats = mo.hstack([
            mo.stat(label="Ball A", value=str(ball_a), bordered=True),
            mo.stat(label="Ball B", value=str(ball_b), bordered=True)
        ], justify="center")

    stats.center()
    return


@app.cell(hide_code=True)
def _(BOTTOM, LEFT, RIGTH, TOP, mo):
    slider_posx_ball_a = mo.ui.slider(label="`X`", value= 20, start=LEFT, stop=RIGTH, step=1)
    slider_posy_ball_a = mo.ui.slider(label="`Y`", value=-20,start=BOTTOM, stop=TOP, step=1)
    slider_posz_ball_a = mo.ui.slider(label="`Z`", value=  2,start=0.5, stop=10_000, step=0.5)
    radius_ball_a = mo.ui.number(label="Radius", start = 1, stop = 50, step=0.5, value=12)
    density_ball_a = mo.ui.number(label=r"($\rho$)", start = 1, stop = 50_000, step=0.5, value=10000.10)


    slider_posx_ball_b = mo.ui.slider(label="`X`", value=-20, start=LEFT, stop=RIGTH, step=1)
    slider_posy_ball_b = mo.ui.slider(label="`Y`", value=20,start=BOTTOM, stop=TOP, step=1)
    slider_posz_ball_b = mo.ui.slider(label="`Z`", value=  2,start=0.5, stop=10_000, step=0.5)
    radius_ball_b = mo.ui.number(label="Radius", start = 1, stop = 50, step=0.5, value=20)
    density_ball_b = mo.ui.number(label=r"($\rho$)", start = 1, stop = 50_000, step=0.5, value=12000.10)
    return (
        density_ball_a,
        density_ball_b,
        radius_ball_a,
        radius_ball_b,
        slider_posx_ball_a,
        slider_posx_ball_b,
        slider_posy_ball_a,
        slider_posy_ball_b,
        slider_posz_ball_a,
        slider_posz_ball_b,
    )


@app.cell(hide_code=True)
def _(G1, G1_a, G1_b, go, mo, xx, yy):
    _xx = [x.tolist() for x in xx]
    _yy = [y.tolist() for y in yy]

    _G1_a = [x.tolist() for x in G1_a]
    _G1 = [x.tolist() for x in G1]
    _G1_b = [x.tolist() for x in G1_b]


    # Create 3D surface plot
    fig3d = go.Figure(data=[go.Surface(
        x=_xx,  # assuming xx is your meshgrid x-coordinates
        y=_yy,  # assuming yy is your meshgrid y-coordinates
        z=_G1,
        colorscale='Jet',
        showscale=True,
        colorbar=dict(
            x=0.85,  # position of colorbar
            len=0.75
        )
    )])

    # Update layout with camera view and labels
    fig3d.update_layout(
        autosize=True,
        width=1200,
        height=800,
        scene=dict(
            xaxis_title='X',
            yaxis_title='Y',
            zaxis_title='Gravity',
            camera=dict(
                center=dict(x=0, y=0, z=0),
                eye=dict(x=1.25, y=1.25, z=1.25),
                up=dict(x=0, y=0, z=1),
            ),
            aspectratio=dict(x=1, y=1, z=1)  # similar to \"auto\" aspect,
        ),
        margin=dict(l=0, r=0, b=0, t=0)
    )

    fig3d.update_scenes(
        xaxis_showbackground=False,
        yaxis_showbackground=False,
        zaxis_showbackground=True
    )

    mo.as_html(fig3d).center()
    return


@app.cell
def _():
    return


@app.cell
def _(input_ball_a, input_ball_b, mo):
    mo.hstack([input_ball_a, input_ball_b])
    return


@app.cell(hide_code=True)
def _(Ball, GAMMA, KM2M, PI, SI2MG, math):
    def bola(ball: Ball, xp, yp, zp):
        rx = xp - ball.x
        ry = yp - ball.y
        rz = zp - ball.z

        # menghitung jarak menggunakan persamaan Pythagoras
        r = math.sqrt(math.pow(rx,2)+math.pow(ry,2)+math.pow(rz,2))

        # apabila jarak=0 maka dibuat fungsi error
        if r == 0:
            raise ValueError("Observer `observer` and Object `ball` should be in the same point")

        #jarak pangkat 3
        r3 = math.pow(r,3)

        # menghitung total mass
        tmass = 4.0 * PI * ball.rho * (math.pow(ball.r,2))/3

        # menghitung nilai percepatan gravitasi pada masing-masing komponen
        gx = -GAMMA * tmass * rx/r3
        gy = -GAMMA * tmass * ry/r3
        gz = -GAMMA * tmass * rz/r3

        # konversi satuan
        gx = gx * SI2MG * KM2M
        gy = gy * SI2MG * KM2M
        gz = gz * SI2MG * KM2M

        return gx, gy, gz
    return (bola,)


@app.cell(hide_code=True)
def _(ar):
    def linspace(lower, upper, n) -> ar.array:
        _step = (upper-lower)/n
        _out = ar.array('d', [lower+(i*_step) for i in range(n)])
        return _out

    def meshgrid(*xi: list|ar.array) -> list[ar.array]:
        """
        Reimplementation of numpy.meshgrid using Python built-in arrays

        Parameters:
        *xi : sequence of 1-D arrays (lists)
            Representing the coordinates of a grid.

        Returns:
        list of array.array
        """
        if not xi:
            return []

        xi = [list(x) for x in xi]
        ndim = len(xi)

        # Initialize output
        output = []
        for i, x in enumerate(xi):

            # Create the broadcasted array
            broadcasted = []
            if ndim == 1:
                broadcasted = [ar.array('d', [val]) for val in x]
            else:
                if i == 0:
                    # For x in xy mode, repeat rows
                    for val in x:
                        broadcasted.append(ar.array('d', [val]*len(xi[1])))
                elif i == 1:
                    # For y in xy mode, repeat columns
                    broadcasted = [ar.array('d', [val for val in x]) for _ in xi[0]]
                else:
                    pass
            output.append(broadcasted)

        return output

    def zeros(dim: tuple[int, int]) -> list[ar.array]:
        x = []
        (nx, ny) = dim
        for _ in range(nx):
            x.append(ar.array('d', [0.0]*ny))
        return x
    return linspace, meshgrid, zeros


if __name__ == "__main__":
    app.run()
