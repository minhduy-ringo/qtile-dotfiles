from libqtile.config import Key
from libqtile.lazy import lazy

# Mod keys
mod = "mod4"
mod1 = "mod1"
mod2 = "mod2"
mod3 = "mod3"

# Key binds
keys = [
    # D E F A U L T
    # Layout behavior
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    Key(
        [mod, "control"],
        "h",
        lazy.layout.shuffle_left(),
        desc="Move window to the left",
    ),
    Key(
        [mod, "control"],
        "l",
        lazy.layout.shuffle_right(),
        desc="Move window to the right",
    ),
    Key([mod, "control"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "control"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    Key([mod], "f", lazy.window.toggle_fullscreen()),
    Key([mod, "control"], "f", lazy.window.toggle_floating(), desc="Toggle floating mode of a window"),
    Key([mod1], "Tab", lazy.layout.down()),
    Key([mod, "shift"], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    # Rofi menu
    Key(
        [mod],
        "r",
        lazy.spawn("rofi -show drun"),
        desc="Spawn a command using a prompt widget",
    ),
    # Shortcut
    Key([mod], "Return", lazy.spawn("kitty"), desc="Launch terminal"),
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),
    Key([mod], "p", lazy.spawn("sh -c ~/.config/rofi/scripts/power"), desc="powermenu"),
    Key([mod], "d", lazy.spawn("sh -c ~/.config/rofi/scripts/display"), desc="Switch display mode"),
    Key([mod, "shift"], "l", lazy.spawn("slock"), desc="Lock computer"),
    Key([mod], "n", lazy.spawn("dunstctl set-paused toggle"), desc="Toggle notification"),
    # Key(
    #     [mod],
    #     "t",
    #     lazy.spawn("sh -c ~/.config/rofi/scripts/themes"),
    #     desc="theme_switcher",
    # ),
    Key([], "Print", lazy.spawn("flameshot gui"), desc="screen capture"),
    Key([mod], "e", lazy.spawn("thunar"), desc="file manager"),
    # System
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    # C U S T O M
    Key(
        [], "XF86AudioMute", lazy.spawn("amixer set Master toggle"), desc="Volume Mute"
    ),
    # Work on spotify
    Key([], "XF86AudioPrev", lazy.spawn("playerctl previous"), desc="playerctl"),
    Key([], "XF86AudioNext", lazy.spawn("playerctl next"), desc="playerctl"),
    # Key(
    #     [],
    #     "XF86KbdBrightnessUp",
    #     lazy.spawn("brightnessctl s 10%+"),
    #     desc="brightness UP",
    # ),
    # Key(
    #     [],
    #     "XF86KbdBrightnessDown",
    #     lazy.spawn("brightnessctl s 10%-"),
    #     desc="brightness Down",
    # ),
    # Key(
    #     [],
    #     "XF86AudioRaiseVolume",
    #     lazy.spawn("pactl set-sink-volume 0 +5%"),
    #     desc="Volume Up",
    # ),
    # Key(
    #     [],
    #     "XF86AudioLowerVolume",
    #     lazy.spawn("pactl set-sink-volume 0 -5%"),
    #     desc="volume down",
    # ),
]
