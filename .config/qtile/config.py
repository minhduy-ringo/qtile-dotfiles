from libqtile.config import ScratchPad, DropDown, Key
from libqtile.lazy import lazy
from libqtile.dgroups import simple_key_binder
from libqtile import hook
from time import sleep

# Key binds
from settings.keys import mod, keys

# Layouts
from settings.layouts import layouts, floating_layout

# Groups
from settings.groups import groups

# Mouse
from settings.mouse import mouse

# Screens
from settings.widgets import widget_defaults, extension_defaults
from settings.screens import screens

import os
import subprocess

@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser("~/.config/qtile/autostart.sh")
    subprocess.Popen([home])

@hook.subscribe.client_managed
def switch_to_group_when_open_app(window):
   window.group.cmd_toscreen()

# Extend groups for scratchpad dropdown
groups.extend([
    ScratchPad('scratchpad', [
        DropDown('monitor', 'kitty -e gotop', witdh=0.2, height=0.6, y=0.2, on_focus_lost_hide=False),
        DropDown('mixer', 'pavucontrol', witdh=0.4, height=0.6, y=0.2, on_focus_lost_hide=False),
    ])
])

keys.extend([
    Key([mod], "m", lazy.group['scratchpad'].dropdown_toggle('monitor'), desc="Spawn monitor"),
    Key([mod], "v", lazy.group['scratchpad'].dropdown_toggle('mixer'), desc="Spawn volume mixer"),
])

dgroups_key_binder = None
dgroups_app_rules = []  # type: Listp

follow_mouse_focus = True
bring_front_click = False
cursor_warp = True

auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = False

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3d"
