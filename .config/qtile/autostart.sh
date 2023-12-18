#!/bin/sh

# compositor
picom & disown

# Two monitor connect
# xrandr --output eDP --mode 1920x1080 --pos 0x0 --output HDMI-1-0 --mode 1920x1080 --rate 144  --pos 1920x0 --primary
# Auto detect and load display options
autorandr -c

# Wallpaper
feh --bg-scale $HOME/Pictures/Wallpaper/120_-_KnFPX73.jpg

# Low battery notifier
# ~/.config/qtile/scripts/check_battery.sh &

# ibus for Vietnamese input
ibus-daemon -drx &

# bluetooth
bluetoothctl power on

# notification
dunst &

# systray
volumeicon &
cbatticon -i notification &
nm-applet &

# start up app
firefox &
caprine &
discord &

# Start welcome
# eos-welcome & disown

/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 & disown # start polkit agent from GNOME
