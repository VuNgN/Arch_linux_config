# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import os
import re
import socket
import subprocess
from libqtile import qtile
from libqtile.config import Click, Drag, Group, KeyChord, Key, Match, Screen
from libqtile.command import lazy
from libqtile import layout, bar, widget, hook
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from typing import List  # noqa: F401from typing import List  # noqa: F401

colors = [["#282c34", "#282c34"], # panel background
          ["#3d3f4b", "#434758"], # background for current screen tab
          ["#ffffff", "#ffffff"], # font color for group names
          ["#ff5555", "#ff5555"], # border line color for current tab
          ["#74438f", "#74438f"], # border line color for 'other tabs' and color for 'odd widgets'
          ["#4f76c7", "#4f76c7"], # color for the 'even widgets'
          ["#e1acff", "#e1acff"], # window name
          ["#ecbbfb", "#ecbbfb"]] # backbround for inactive screens

prompt = "{0}@{1}: ".format(os.environ["USER"], socket.gethostname())
mod = "mod4"
terminal = guess_terminal()
myTerm = "alacritty"      # My terminal of choice
myBrowser = "firefox" # My terminal of choice
myCodeEditor = "code" # My code editor

keys = [
    # Switch between windows
    Key([mod], "j", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "k", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "i", lazy.layout.up(), desc="Move focus up"),
    Key(["mod1"], "Tab", lazy.layout.next(),
        desc="Move window focus to other window"),

    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "j", lazy.layout.shuffle_left(),
        desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(),
        desc="Move window to the right"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_down(),
        desc="Move window down"),
    Key([mod, "shift"], "i", lazy.layout.shuffle_up(), desc="Move window up"),

    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "j", lazy.layout.grow_left(),
        desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(),
        desc="Grow window to the right"),
    Key([mod, "control"], "k", lazy.layout.grow_down(),
        desc="Grow window down"),
    Key([mod, "control"], "i", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod, "shift"], "Return", lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack"),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),

    Key([mod, "control"], "r", lazy.restart(), desc="Restart Qtile"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(),
        desc="Spawn a command using a prompt widget"),

    # Open applications 
    Key([mod], "f", lazy.spawn(myBrowser), desc="Open firefox"),
    Key([mod], "v", lazy.spawn(myCodeEditor), desc="Open my code editor"),
    Key([mod], "n", lazy.spawn("notion-snap"), desc="Open notion"),
    Key([mod], "m", lazy.spawn("spotify"), desc="Open music app (spotify)"),
    Key([mod], "g", lazy.spawn("google-chrome-stable"), desc="open google chrome")

    # Screenshot
    #Key([mod], "", lazy.spawn("gnome-screenshot -i"), desc="Open gnome-screenshot"),
]

groups = [Group(i) for i in "123456789"]
for i in groups:
    keys.extend([
        # mod1 + letter of group = switch to group
        Key([mod], i.name, lazy.group[i.name].toscreen(),
            desc="Switch to group {}".format(i.name)),

        # mod1 + shift + letter of group = switch to & move focused window to group
        Key([mod, "shift"], i.name, lazy.window.togroup(i.name, switch_group=True),
            desc="Switch to & move focused window to group {}".format(i.name)),
        # Or, use below if you prefer not to switch to that group.
        # # mod1 + shift + letter of group = move focused window to group
        # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
        #     desc="move focused window to group {}".format(i.name)),
    ])

# groups = [Group("WWW", {'layout': 'monadtall'}),
#               Group("DEV", {'layout': 'monadtall'}),
#               Group("SYS", {'layout': 'monadtall'}),
#               Group("DOC", {'layout': 'monadtall'}),
#               Group("VBOX", {'layout': 'monadtall'}),
#               Group("CHAT", {'layout': 'monadtall'}),
#               Group("MUS", {'layout': 'monadtall'}),
#               Group("VID", {'layout': 'monadtall'}),
#               Group("GFX", {'layout': 'floating'})]

# # Allow MODKEY+[0 through 9] to bind to groups, see https://docs.qtile.org/en/stable/manual/config/groups.html
# # MOD4 + index Number : Switch to Group[index]
# # MOD4 + shift + index Number : Send active window to another Group
# from libqtile.dgroups import simple_key_binder
# dgroups_key_binder = simple_key_binder("mod4")


# groupIndex= [i for i in "123456789"]
# for i in groupIndex:
#     keys.extend([
#         # mod1 + letter of group = switch to group
#         Key([mod], i, lazy.group[i].toscreen(),
#             desc="Switch to group {}".format(i)),

#         # mod1 + shift + letter of group = switch to & move focused window to group
#         Key([mod, "shift"], i, lazy.window.togroup(i, switch_group=True),
#             desc="Switch to & move focused window to group {}".format(i)),
#         # Or, use below if you prefer not to switch to that group.
#         # # mod1 + shift + letter of group = move focused window to group
#         # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
#         #     desc="move focused window to group {}".format(i.name)),
#     ])

layout_theme = {"border_width": 2,
                "margin": 5,
                "border_focus": "e1acff",
                "border_normal": "1D2330"
                }

layouts = [
    layout.Columns(**layout_theme),
    layout.Max(**layout_theme),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadTall(),
    # layout.MonadWide(), 
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    layout.Zoomy(**layout_theme),
]

widget_defaults = dict(
    font='Ubuntu Mono',
    fontsize=12,
    padding=2,
    background=colors[2]
)
extension_defaults = widget_defaults.copy()

def init_widgets_list():
    widgets_list = [
                #   widget.CurrentLayout(),
                # widget.GroupBox(),
                # widget.Prompt(),
                # widget.Chord(
                #     chords_colors={
                #         'launch': ("#ff0000", "#ffffff"),
                #     },
                #     name_transform=lambda name: name.upper(),
                # ),
                #widget.TextBox("default config", name="default"),
                #widget.TextBox("Press &lt;M-r&gt; to spawn", foreground="#d75f5f"),
                # widget.Clock(format='%Y-%m-%d %a %I:%M %p'),
                # widget.Systray(),
                #widget.QuickExit(),
              widget.Sep(
                     linewidth = 0,
                     padding = 6,
                     foreground = colors[2],
                     background = colors[0]
                     ),
              widget.Image(
                     filename = "~/.config/qtile/icons/arch1.png",
                     scale = "False",
                     mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(myTerm)},
                     padding = 2,
                     background = colors[0]
                     ),
              widget.Sep(
                     linewidth = 0,
                     padding = 6,
                     foreground = colors[2],
                     background = colors[0]
                     ),
              widget.GroupBox(
                     font = "Ubuntu Bold",
                     fontsize = 12,
                     margin_y = 3,
                     margin_x = 3,
                     padding_y = 5,
                     padding_x = 3,
                     borderwidth = 3,
                     active = colors[2],
                     inactive = colors[7],
                     rounded = False,
                     highlight_color = colors[1],
                     highlight_method = "line",
                     this_current_screen_border = colors[6],
                     this_screen_border = colors [4],
                     other_current_screen_border = colors[6],
                     other_screen_border = colors[4],
                     foreground = colors[2],
                     background = colors[0]
                     ),
              widget.Prompt(
                     prompt = prompt,
                     font = "Ubuntu Mono",
                     padding = 10,
                     foreground = colors[3],
                     background = colors[1]
                     ),
              widget.Sep(
                     linewidth = 0,
                     padding = 40,
                     foreground = colors[2],
                     background = colors[0]
                     ),
              widget.WindowName(
                     foreground = colors[6],
                     background = colors[0],
                     padding = 0
                     ),
              widget.Systray(
                     background = colors[0],
                     padding = 5
                     ),     
              widget.Sep(
                     linewidth = 0,
                     padding = 6,
                     foreground = colors[0],
                     background = colors[0]
                     ),
              widget.TextBox(
                     text = '',
                     background = colors[0],
                     foreground = colors[5],
                     padding = -11,
                     fontsize = 67,
                     ),
              widget.Clock(
                     foreground = colors[2],
                     background = colors[5],
                     format = "%A, %B %d - %H:%M "
                     ),
                
              widget.TextBox(
                     text = '',
                     background = colors[5],
                     foreground = colors[4],
                     padding = -11,
                     fontsize = 67,
                     ),
              widget.TextBox(
                     text = " 🌡",
                     padding = 2,
                     foreground = colors[2],
                     background = colors[4],
                     fontsize = 11
                     ),
              widget.ThermalSensor(
                     foreground = colors[2],
                     background = colors[4],
                     threshold = 90,
                     padding = 5
                     ),
              widget.TextBox(
                     text='',
                     background = colors[4],
                     foreground = colors[5],
                     padding = -11,
                     fontsize = 67,
                     ),
              widget.TextBox(
                     text = " ⟳",
                     padding = 2,
                     foreground = colors[2],
                     background = colors[5],
                     fontsize = 14
                     ),
              widget.CheckUpdates(
                     update_interval = 1800,
                     distro = "Arch Linux",
                     display_format = "{updates} Updates",
                     foreground = colors[2],
                     mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(myTerm + ' -e sudo pacman -Syu')},
                     background = colors[5]
                     ),
              widget.TextBox(
                     text = '',
                     background = colors[5],
                     foreground = colors[4],
                     padding = -11,
                     fontsize = 67,
                     ),
              widget.TextBox(
                     text = " 🖬",
                     foreground = colors[2],
                     background = colors[4],
                     padding = 2,
                     fontsize = 14
                     ),
              widget.Memory(
                     foreground = colors[2],
                     background = colors[4],
                     mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(myTerm + ' -e htop')},
                     padding = 5
                     ),
              widget.TextBox(
                     text = '',
                     background = colors[4],
                     foreground = colors[5],
                     padding = -11,
                     fontsize = 67,
                     ),
              widget.TextBox(
                     text = " Vol:",
                     foreground = colors[2],
                     background = colors[5],
                     padding = 2
                     ),
              widget.Volume(
                     foreground = colors[2],
                     background = colors[5],
                     mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(myTerm + ' -e alsamixer')},
                     padding = 5
                     ),
              widget.TextBox(
                     text = '',
                     background = colors[5],
                     foreground = colors[4],
                     padding = -11,
                     fontsize = 67,
                     ),
              widget.CurrentLayoutIcon(
                     custom_icon_paths = [os.path.expanduser("~/.config/qtile/icons")],
                     foreground = colors[0],
                     background = colors[4],
                     padding = 2,
                     scale = 0.7
                     ),
              widget.CurrentLayout(
                     foreground = colors[2],
                     background = colors[4],
                     padding = 5
                     ),
              widget.TextBox(
                     text = '',
                     background = colors[4],
                     foreground = colors[5],
                     padding = -11,
                     fontsize = 67,
                     ),
              widget.Net(
                     interface = "wlp0s20f3",
                     format = '{down} ↓↑ {up}',
                     foreground = colors[2],
                     background = colors[5],
                     padding = 5
                     ),
              widget.TextBox(
                     text = '',
                     background = colors[5],
                     foreground = colors[4],
                     padding = -11,
                     fontsize = 67,
                     ),
              widget.TextBox(
                     text = 'ᯤ',
                     foreground = colors[2],
                     background = colors[4],
                     padding = 2,
                     fontsize = 14
                     ),
              widget.Wlan(
                     interface='wlp0s20f3',
                     foreground = colors[2],
                     background = colors[4],
                     padding = 5,
                     ),
              widget.TextBox(
                     text = '',
                     background = colors[4],
                     foreground = colors[5],
                     padding = -11,
                     fontsize = 67,
                     ),
              widget.WindowCount(
                     foreground = colors[2],
                     background = colors[5],
                     padding = 5,
                     ),
              widget.TextBox(
                     text = "🀆  ",
                     padding = 2,
                     foreground = colors[2],
                     background = colors[5],
                     fontsize = 14
                     ),
              widget.TextBox(
                     text = '',
                     background = colors[5],
                     foreground = colors[4],
                     padding = -11,
                     fontsize = 67,
                     ),
              widget.BatteryIcon(
                     foreground = colors[2],
                     background = colors[4],
                     padding = 2,
                     ),
              widget.Battery(
                     foreground = colors[2],
                     background = colors[4],
                     padding = 5,
                     ),
              widget.TextBox(
                     text = '',
                     background = colors[4],
                     foreground = colors[5],
                     padding = -11,
                     fontsize = 67,
                     ),
              widget.WidgetBox(
                     widgets=[
                            widget.KeyboardLayout(
                                   foreground = colors[2],
                                   background = colors[5],
                                   mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(myTerm + ' -e ibus-setup')},
                                   padding = 5,
                                   ),
                            widget.TextBox(
                                   text = '',
                                   background = colors[5],
                                   foreground = colors[4],
                                   padding = -11,
                                   fontsize = 67,
                                   ),
                            widget.TextBox(
                                   text = ' ⛶  ',
                                   foreground = colors[2],
                                   background = colors[4],
                                   padding = 10,
                                   mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(myTerm + ' -e gnome-screenshot -i')},
                                   fontsize = 14
                                   ),
                            widget.TextBox(
                                   text = '',
                                   background = colors[4],
                                   foreground = colors[5],
                                   padding = -11,
                                   fontsize = 67,
                                   ),
                            widget.WidgetBox(
                                   widgets=[
                                          widget.QuickExit(
                                                 foreground = colors[2],
                                                 background = colors[5],
                                                 padding = 5, 
                                                 default_text= '[ log out ]',
                                          ),
                                          widget.TextBox(
                                                 text = '',
                                                 background = colors[5],
                                                 foreground = colors[4],
                                                 padding = -11,
                                                 fontsize = 67,
                                                 ),
                                          widget.TextBox(
                                                 text = ' ⏻ ',
                                                 foreground = colors[2],
                                                 background = colors[4],
                                                 padding = 10,
                                                 mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(myTerm + ' -e shutdown now')},
                                                 fontsize = 14
                                          ), 
                                          
                                   ],
                                   text_closed= "  ⚠  ",
                                   text_open= "❌  ",
                                   foreground = colors[2],
                                   background = colors[5],
                                   padding = 5, 
                                   ),
                     ],
                     text_closed= "◀︎  ",
                     text_open= "▶︎  ",
                     foreground = colors[2],
                     background = colors[5],
                     padding = 5, 
                     ),
              ]
    return widgets_list

def init_widgets_list_2():
    widgets_list_2 = [
              widget.Sep(
                     linewidth = 0,
                     padding = 6,
                     foreground = colors[2],
                     background = colors[0]
                     ),
              widget.Image(
                     filename = "~/.config/qtile/icons/arch1.png",
                     scale = "False",
                     mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(myTerm)},
                     padding = 2,
                     background = colors[0]
                     ),
              widget.Sep(
                     linewidth = 0,
                     padding = 6,
                     foreground = colors[2],
                     background = colors[0]
                     ),
              widget.GroupBox(
                     font = "Ubuntu Bold",
                     fontsize = 12,
                     margin_y = 3,
                     margin_x = 3,
                     padding_y = 5,
                     padding_x = 3,
                     borderwidth = 3,
                     active = colors[2],
                     inactive = colors[7],
                     rounded = False,
                     highlight_color = colors[1],
                     highlight_method = "line",
                     this_current_screen_border = colors[6],
                     this_screen_border = colors [4],
                     other_current_screen_border = colors[6],
                     other_screen_border = colors[4],
                     foreground = colors[2],
                     background = colors[0]
                     ),
              widget.Prompt(
                     prompt = prompt,
                     font = "Ubuntu Mono",
                     padding = 10,
                     foreground = colors[3],
                     background = colors[1]
              ),
              widget.Sep(
                     linewidth = 0,
                     padding = 40,
                     foreground = colors[2],
                     background = colors[0]
              ),
              widget.WindowName(
                     foreground = colors[6],
                     background = colors[0],
                     padding = 0
              ),
              widget.Systray(
                     background = colors[0],
                     padding = 5
              ),
              widget.Sep(
                     linewidth = 0,
                     padding = 6,
                     foreground = colors[0],
                     background = colors[0]
                     ),
              widget.TextBox(
                     text = '',
                     background = colors[0],
                     foreground = colors[5],
                     padding = -11,
                     fontsize = 67,
                     ),
              widget.Clock(
                     foreground = colors[2],
                     background = colors[5],
                     format = "%A, %B %d - %H:%M "
                     ),
              widget.TextBox(
                     text = '',
                     background = colors[5],
                     foreground = colors[4],
                     padding = -11,
                     fontsize = 67,
                     ),
              widget.TextBox(
                     text = " 🖬",
                     foreground = colors[2],
                     background = colors[4],
                     padding = 2,
                     fontsize = 14
                     ),
              widget.Memory(
                     foreground = colors[2],
                     background = colors[4],
                     mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(myTerm + ' -e htop')},
                     padding = 5
                     ),
              widget.TextBox(
                     text = '',
                     background = colors[4],
                     foreground = colors[5],
                     padding = -11,
                     fontsize = 67,
                     ),
              widget.TextBox(
                     text = " Vol:",
                     foreground = colors[2],
                     background = colors[5],
                     padding = 2
                     ),
              widget.Volume(
                     foreground = colors[2],
                     background = colors[5],
                     mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(myTerm + ' -e alsamixer')},
                     padding = 5
                     ),
              widget.TextBox(
                     text = '',
                     background = colors[5],
                     foreground = colors[4],
                     padding = -11,
                     fontsize = 67,
                     ),
              widget.CurrentLayoutIcon(
                     custom_icon_paths = [os.path.expanduser("~/.config/qtile/icons")],
                     foreground = colors[0],
                     background = colors[4],
                     padding = 2,
                     scale = 0.7
                     ),
              widget.CurrentLayout(
                     foreground = colors[2],
                     background = colors[4],
                     padding = 5
                     ),
              widget.TextBox(
                     text = '',
                     background = colors[4],
                     foreground = colors[5],
                     padding = -11,
                     fontsize = 67,
                     ),
              widget.TextBox(
                     text = 'ᯤ',
                     foreground = colors[2],
                     background = colors[5],
                     padding = 2,
                     fontsize = 14
                     ),
              widget.Wlan(
                     interface='wlp0s20f3',
                     foreground = colors[2],
                     background = colors[5],
                     padding = 5,
              ),
              widget.TextBox(
                     text = '',
                     background = colors[5],
                     foreground = colors[4],
                     padding = -11,
                     fontsize = 67,
                     ),
              widget.BatteryIcon(
                     foreground = colors[2],
                     background = colors[4],
                     padding = 2,
              ),
              widget.Battery(
                     foreground = colors[2],
                     background = colors[4],
                     padding = 5,
                     ),
                     widget.TextBox(
                     text = '',
                     background = colors[4],
                     foreground = colors[5],
                     padding = -11,
                     fontsize = 67,
                     ),
              widget.WidgetBox(
                     widgets=[
                            widget.KeyboardLayout(
                                   foreground = colors[2],
                                   background = colors[5],
                                   mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(myTerm + ' -e ibus-setup')},
                                   padding = 5,
                                   ),
                            widget.TextBox(
                                   text = '',
                                   background = colors[5],
                                   foreground = colors[4],
                                   padding = -11,
                                   fontsize = 67,
                                   ),
                            widget.TextBox(
                                   text = ' ⛶  ',
                                   foreground = colors[2],
                                   background = colors[4],
                                   padding = 10,
                                   mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(myTerm + ' -e gnome-screenshot -i')},
                                   fontsize = 14
                                   ),
                            widget.TextBox(
                                   text = '',
                                   background = colors[4],
                                   foreground = colors[5],
                                   padding = -11,
                                   fontsize = 67,
                                   ),
                            widget.WidgetBox(
                                   widgets=[
                                          widget.QuickExit(
                                                 foreground = colors[2],
                                                 background = colors[5],
                                                 padding = 5, 
                                                 default_text= '[ log out ]',
                                          ),
                                          widget.TextBox(
                                                 text = '',
                                                 background = colors[5],
                                                 foreground = colors[4],
                                                 padding = -11,
                                                 fontsize = 67,
                                                 ),
                                          widget.TextBox(
                                                 text = ' ⏻ ',
                                                 foreground = colors[2],
                                                 background = colors[4],
                                                 padding = 10,
                                                 mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(myTerm + ' -e shutdown now')},
                                                 fontsize = 14
                                          ), 
                                          
                                   ],
                                   text_closed= "  ⚠  ",
                                   text_open= "❌  ",
                                   foreground = colors[2],
                                   background = colors[5],
                                   padding = 5, 
                                   ),
                     ],
                     text_closed= "◀︎  ",
                     text_open= "▶︎  ",
                     foreground = colors[2],
                     background = colors[5],
                     padding = 5, 
                     ),
              ]
    return widgets_list_2

def init_widgets_screen2():
    widgets_screen2 = init_widgets_list_2()
    del widgets_screen2[7:8]               # Slicing removes unwanted widgets (systray) on Monitors 1,3
    return widgets_screen2

def init_widgets_screen1():
    widgets_screen1 = init_widgets_list()
    return widgets_screen1                 # Monitor 2 will display all widgets in widgets_list

def init_screens():
    return [Screen(top=bar.Bar(widgets=init_widgets_screen1(), opacity=1.0, size=20, margin=0)),
            Screen(top=bar.Bar(widgets=init_widgets_screen2(), opacity=1.0, size=20)),]

if __name__ in ["config", "__main__"]:
    screens = init_screens()
    widgets_list = init_widgets_list()
    widgets_list_2 = init_widgets_list_2()
    widgets_screen2 = init_widgets_screen2()
    widgets_screen1 = init_widgets_screen1()

def window_to_prev_group(qtile):
    if qtile.currentWindow is not None:
        i = qtile.groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.groups[i - 1].name)

def window_to_next_group(qtile):
    if qtile.currentWindow is not None:
        i = qtile.groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.groups[i + 1].name)

def window_to_previous_screen(qtile):
    i = qtile.screens.index(qtile.current_screen)
    if i != 0:
        group = qtile.screens[i - 1].group.name
        qtile.current_window.togroup(group)

def window_to_next_screen(qtile):
    i = qtile.screens.index(qtile.current_screen)
    if i + 1 != len(qtile.screens):
        group = qtile.screens[i + 1].group.name
        qtile.current_window.togroup(group)

def switch_screens(qtile):
    i = qtile.screens.index(qtile.current_screen)
    group = qtile.screens[i - 1].group
    qtile.current_screen.set_group(group)

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    *layout.Floating.default_float_rules,
    Match(wm_class='confirmreset'),  # gitk
    Match(wm_class='makebranch'),  # gitk
    Match(wm_class='maketag'),  # gitk
    Match(wm_class='ssh-askpass'),  # ssh-askpass
    Match(title='branchdialog'),  # gitk
    Match(title='pinentry'),  # GPG key password entry
])
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
