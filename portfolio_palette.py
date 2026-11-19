"""Reusable color palette based on the portfolio design.

The color constants can be used without third-party dependencies. Matplotlib
and Seaborn are imported only by the helper functions that need them.

Examples:
    import seaborn as sns
    from portfolio_palette import QUALITATIVE_COLORS, set_seaborn_theme

    set_seaborn_theme()
    sns.barplot(data=data, x="category", y="value")

    import matplotlib.pyplot as plt
    from portfolio_palette import apply_matplotlib_style, matplotlib_colormap

    apply_matplotlib_style()
    plt.imshow(values, cmap=matplotlib_colormap())
"""

from typing import List, Optional, Sequence, Tuple


COLORS = {
    "background": "#F3F4EE",
    "surface": "#FFFFFF",
    "surface_alt": "#E8EEE8",
    "teal": "#397F75",
    "sand": "#B99B65",
    "text": "#20312F",
    "muted": "#667570",
    "gold": "#9B7B43",
    "green": "#688A7D",
    "green_light": "#AFC7BD",
    "green_pale": "#D6E3D8",
}

QUALITATIVE_COLORS = (
    COLORS["teal"],
    COLORS["sand"],
    COLORS["green"],
    COLORS["gold"],
    COLORS["text"],
    COLORS["muted"],
)

SEQUENTIAL_COLORS = (
    COLORS["background"],
    COLORS["green_pale"],
    COLORS["green_light"],
    COLORS["green"],
    COLORS["teal"],
    COLORS["text"],
)

DIVERGING_COLORS = (
    COLORS["sand"],
    COLORS["background"],
    COLORS["teal"],
)


def matplotlib_colormap(
    name: str = "portfolio_sequential",
    colors: Sequence[str] = SEQUENTIAL_COLORS,
):
    """Create a continuous Matplotlib colormap from the supplied hex colors."""
    try:
        from matplotlib.colors import LinearSegmentedColormap
    except ImportError as exc:
        raise ImportError(
            "matplotlib_colormap() requires Matplotlib. Install it with "
            "`pip install matplotlib`."
        ) from exc

    return LinearSegmentedColormap.from_list(name, colors)


def apply_matplotlib_style() -> None:
    """Apply portfolio colors to Matplotlib's global plotting defaults."""
    try:
        from cycler import cycler
        from matplotlib import rcParams
    except ImportError as exc:
        raise ImportError(
            "apply_matplotlib_style() requires Matplotlib. Install it with "
            "`pip install matplotlib`."
        ) from exc

    rcParams.update(
        {
            "axes.prop_cycle": cycler(color=QUALITATIVE_COLORS),
            "axes.facecolor": COLORS["surface"],
            "figure.facecolor": COLORS["background"],
            "axes.edgecolor": COLORS["muted"],
            "axes.labelcolor": COLORS["text"],
            "text.color": COLORS["text"],
            "xtick.color": COLORS["muted"],
            "ytick.color": COLORS["muted"],
            "grid.color": COLORS["surface_alt"],
            "savefig.facecolor": COLORS["background"],
        }
    )


def seaborn_palette(
    n_colors: Optional[int] = None,
) -> List[Tuple[float, float, float]]:
    """Return the qualitative palette as Seaborn RGB color tuples."""
    try:
        import seaborn as sns
    except ImportError as exc:
        raise ImportError(
            "seaborn_palette() requires Seaborn. Install it with "
            "`pip install seaborn`."
        ) from exc

    return sns.color_palette(QUALITATIVE_COLORS, n_colors=n_colors)


def set_seaborn_theme(style: str = "whitegrid") -> None:
    """Set a Seaborn theme using the portfolio palette and surface colors."""
    try:
        import seaborn as sns
    except ImportError as exc:
        raise ImportError(
            "set_seaborn_theme() requires Seaborn. Install it with "
            "`pip install seaborn`."
        ) from exc

    sns.set_theme(
        style=style,
        palette=QUALITATIVE_COLORS,
        rc={
            "axes.facecolor": COLORS["surface"],
            "figure.facecolor": COLORS["background"],
            "axes.edgecolor": COLORS["muted"],
            "axes.labelcolor": COLORS["text"],
            "text.color": COLORS["text"],
            "xtick.color": COLORS["muted"],
            "ytick.color": COLORS["muted"],
            "grid.color": COLORS["surface_alt"],
        },
    )
