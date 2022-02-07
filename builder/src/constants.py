#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import Dict

# Info
AUTHOR = "Kaiz Khatri"
URL = "https://github.com/ful1e5/pokemon-cursor"

# XCursor
X_DELAY: int = 10

# Windows Cursor
WIN_DELAY = 1

X_CURSORS_CFG: Dict[str, Dict[str, int]] = {
    ##########
    # Static #
    ##########
    "all-scroll.png": {"xhot": 98, "yhot": 101},
    "bottom_left_corner.png": {"xhot": 96, "yhot": 97},
    "bottom_right_corner.png": {"xhot": 104, "yhot": 97},
    "bottom_tee.png": {"xhot": 95, "yhot": 123},
    "center_ptr.png": {"xhot": 92, "yhot": 42},
    "context-menu.png": {"xhot": 48, "yhot": 34},
    "copy.png": {"xhot": 48, "yhot": 34},
    "cross.png": {"xhot": 98, "yhot": 100},
    "crossed_circle.png": {"xhot": 48, "yhot": 34},
    "crosshair.png": {"xhot": 100, "yhot": 100},
    "dnd_no_drop.png": {"xhot": 100, "yhot": 100},
    "dotbox.png": {"xhot": 100, "yhot": 100},
    "hand1.png": {"xhot": 101, "yhot": 50},
    "hand2.png": {"xhot": 75, "yhot": 40},
    "left_ptr.png": {"xhot": 48, "yhot": 34},
    "left_side.png": {"xhot": 102, "yhot": 97},
    "left_tee.png": {"xhot": 76, "yhot": 99},
    "link.png": {"xhot": 48, "yhot": 34},
    "ll_angle.png": {"xhot": 66, "yhot": 142},
    "lr_angle.png": {"xhot": 126, "yhot": 137},
    "move.png": {"xhot": 98, "yhot": 53},
    "pencil.png": {"xhot": 63, "yhot": 151},
    "plus.png": {"xhot": 97, "yhot": 99},
    "question_arrow.png": {"xhot": 48, "yhot": 34},
    "right_ptr.png": {"xhot": 141, "yhot": 35},
    "right_tee.png": {"xhot": 119, "yhot": 98},
    "sb_down_arrow.png": {"xhot": 99, "yhot": 123},
    "sb_h_double_arrow.png": {"xhot": 98, "yhot": 101},
    "sb_left_arrow.png": {"xhot": 72, "yhot": 97},
    "sb_right_arrow.png": {"xhot": 139, "yhot": 101},
    "sb_up_arrow.png": {"xhot": 99, "yhot": 65},
    "sb_v_double_arrow.png": {"xhot": 98, "yhot": 99},
    "top_side.png": {"xhot": 101, "yhot": 95},
    "top_tee.png": {"xhot": 101, "yhot": 96},
    "ul_angle.png": {"xhot": 78, "yhot": 77},
    "ur_angle.png": {"xhot": 124, "yhot": 78},
    "vertical-text.png": {"xhot": 100, "yhot": 97},
    "wayland-cursor.png": {"xhot": 100, "yhot": 100},
    "X_cursor.png": {"xhot": 100, "yhot": 100},
    "xterm.png": {"xhot": 101, "yhot": 93},
    "zoom-in.png": {"xhot": 82, "yhot": 82},
    "zoom-out.png": {"xhot": 82, "yhot": 82},
    ############
    # Animated #
    ############
    # Note: Animated cursors don't need an extension and frame numbers.
    "left_ptr_watch": {"xhot": 48, "yhot": 34},
    "wait": {"xhot": 100, "yhot": 100},
}

WIN_CURSORS_CFG: Dict[str, Dict[str, str]] = {
    ##########
    # Static #
    ##########
    "right_ptr.png": {"to": "Alternate", "position": "top_left"},
    "cross.png": {"to": "Cross"},
    "left_ptr.png": {"to": "Default", "position": "top_left"},
    "bottom_right_corner.png": {"to": "Diagonal_1"},
    "bottom_left_corner.png": {"to": "Diagonal_2"},
    "pencil.png": {"to": "Handwriting"},
    "question_arrow.png": {"to": "Help", "position.png": "top_left"},
    "sb_h_double_arrow.png": {"to": "Horizontal"},
    "xterm.png": {"to": "IBeam", "position": "top_left"},
    "hand2.png": {"to": "Link", "position": "top_left"},
    "hand1.png": {"to": "Move"},
    "crossed_circle.png": {"to": "Unavailiable", "position": "top_left"},
    "sb_v_double_arrow.png": {"to": "Vertical"},
    ############
    # Animated #
    ############
    # Note: Animated cursors don't need frame numbers.
    "left_ptr_watch": {"to": "Work", "position": "top_left"},
    "wait": {"to": "Busy"},
}
