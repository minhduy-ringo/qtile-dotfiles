# ██╗    ██╗██╗██████╗  ██████╗ ███████╗████████╗███████╗
# ██║    ██║██║██╔══██╗██╔════╝ ██╔════╝╚══██╔══╝██╔════╝
# ██║ █╗ ██║██║██║  ██║██║  ███╗█████╗     ██║   ███████╗
# ██║███╗██║██║██║  ██║██║   ██║██╔══╝     ██║   ╚════██║
# ╚███╔███╔╝██║██████╔╝╚██████╔╝███████╗   ██║   ███████║
#  ╚══╝╚══╝ ╚═╝╚═════╝  ╚═════╝ ╚══════╝   ╚═╝   ╚══════╝

# https://github.com/L4ZYP4CM4N/DOTFILES


from libqtile import widget
from libqtile.lazy import lazy
from libqtile.config import ScratchPad, DropDown
from .theme import colors
from .spotify import Spotify
from .groups import groups
from qtile_extras.widget.decorations import PowerLineDecoration

# Quick settings #
font = "JetBrainsMono Nerd Font Mono"
power_line_size = 23
font_size = 12
icon_size = 19
workspace_icon_size = 23

def base(fg="Surface0", bg="Base"):
    return {"foreground": colors[fg], "background": colors[bg]}


def separator():
    return widget.Sep(**base(), linewidth=0, padding=5)


def powerline_left(fg="Flamingo", bg="Base"):
    return widget.TextBox(
        **base(fg, bg), text=" ", fontsize=power_line_size, padding=-3  #   
    )


def powerline_right(fg="Flamingo", bg="Base"):
    return widget.TextBox(
        **base(fg, bg), text=" ", fontsize=power_line_size, padding=-3  #   
    )


def icon(fg="Surface0", bg="Base", fontsize=icon_size, text="?"):
    return widget.TextBox(
        **base(fg, bg),
        fontsize=fontsize,
        text=text,
        padding=1,
    )


def workspaces():
    return [
        separator(),
        widget.Image(
            **base("Base", "Base"),
            filename="~/.config/qtile/assets/eos-c.png",
            scale=True,
            margin=7,
            mouse_callbacks={
                "Button1": lambda: qtile.cmd_spawn("rofi -show drun"),
                "Button3": lazy.spawn("sh .config/qtile/scripts/rofi/powermenu.sh"),
            },
        ),
        separator(),
        widget.GroupBox(
            **base(fg="Base"),
            font=font,
            fontsize=workspace_icon_size,
            margin_y=3,
            margin_x=0,
            padding_y=8,
            padding_x=5,
            borderwidth=1,
            active=colors["Rosewater"],
            inactive=colors["Base"],
            rounded=False,
            highlight_method="line",  # box, text, block, line
            block_highlight_text_color=colors["Sapphire"],
            urgent_alert_method="line",
            urgent_border=colors["Yellow"],
            # this_current_screen_border=colors["Red"],
            # this_screen_border=colors["Blue"],
            # other_current_screen_border=colors["Blue"],
            # other_screen_border=colors["Blue"],
            disable_drag=True,
            hide_unused=True,
            center_aligned=True,
        ),
    ]

primary_widgets = [
    *workspaces(),
    powerline_right("Base", "Crust"),
    widget.CurrentLayout(**base(fg="Sky", bg="Crust"), scale=0.7),
    powerline_right("Crust", "Base"),
    widget.WindowName(**base(fg="Sky"), padding=5),
    # Spotify(),
    widget.Systray(background=colors["Base"], padding=5),
    separator(),
    powerline_left("Rosewater", "Base"),
    icon(bg="Rosewater", text="󰅢"),  # Icon: nf-fa-download
    widget.CheckUpdates(
        **base(bg="Rosewater"),
        colour_have_updates=colors["Red"],
        colour_no_updates=colors["Red"],
        no_update_string=" 0",
        display_format=" {updates}",
        update_interval=1800,
        custom_command="checkupdates",
        mouse_callbacks={"Button1": lazy.spawn("kitty -e sudo pacman -Syu")},
    ),
    powerline_left("Peach", "Rosewater"),
    icon(bg="Peach", text=""),
    widget.Memory(
        **base(bg="Peach"),
        measure_mem="G",
        format="{MemUsed: .0f}{mm} ",  # /{MemTotal: .0f}{mm}
    ),
    icon(bg="Peach", text=" "),
    widget.ThermalSensor(
        **base(bg="Peach"),
        tag_sensor="Tctl",
        threshold=80,
    ),
    powerline_left("Sapphire", "Peach"),
    icon(bg="Sapphire", text=""),
    widget.Clock(
        **base(bg="Sapphire"),
        format="%H:%M %d/%m ",
    ),
]

widget_defaults = {
    "font": font,
    "fontsize": font_size,
}
extension_defaults = widget_defaults.copy()
