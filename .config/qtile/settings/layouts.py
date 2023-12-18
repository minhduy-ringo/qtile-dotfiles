from libqtile import layout
from libqtile.config import Match
from .theme import colors

layout_conf = {
    "border_focus": colors["Lavender"],
    "border_normal": colors["Overlay0"],
    "border_witdh": 3,
    "margin": 8,
}

layouts = [
    layout.MonadTall(**layout_conf, name="MonadTall"),
    layout.Max(**layout_conf, name="Max"),
]

floating_layout = layout.Floating(
    float_rules=[
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),
        Match(wm_class="makebranch"),
        Match(wm_class="maketag"),
        Match(wm_class="ssh-askpass"),
        Match(title="branchdialog"),
        Match(title="pinentry"),
    ],
    border_focus=colors["Lavender"],
)
