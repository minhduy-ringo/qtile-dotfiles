from libqtile.config import Key, Group, Match, ScratchPad, DropDown
from libqtile.lazy import lazy
from .keys import mod, keys

terminal = "kitty"
browser = "firefox"
discord = "discord"
messenger = "caprine"
spotify = "spotify"
game = "steam"

groups = [
    Group(name="1", label="", matches=[Match(wm_class=terminal)], layout="MonadTall"),
    Group(name="2", label="󰈹", matches=[Match(wm_class=browser)], layout="Max"),
    Group(
        name="3",
        label="󰭹",
        matches=[Match(wm_class=discord), Match(wm_class=messenger)],
        layout="MonadTall",
    ),
    Group(name="4", label="󰊗", matches=[Match(wm_class=game)], layout="Max"),
    Group(name="5", label="", matches=[Match(wm_class=spotify)], layout="Max"),
    # Rest workspace, only to show wallpapers
    Group(
        name="6",
        label="󰽹",
        layout="Max"
    ),
]

for group in groups:
    keys.extend(
        [
            Key(
                [mod],
                group.name,
                lazy.group[group.name].toscreen(),
                desc=f"Switch to group {group.name}",
            ),
            Key(
                [mod, "shift"],
                group.name,
                lazy.window.togroup(group.name, switch_group=True),
                desc=f"Switch to & move focused window to group {group.name}",
            ),
        ]
    )
