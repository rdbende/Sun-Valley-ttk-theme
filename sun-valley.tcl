# Copyright © 2021 rdbende <rdbende@gmail.com>

source [file join [file dirname [info script]] theme light.tcl]
source [file join [file dirname [info script]] theme dark.tcl]

option add *tearOff 0

proc set_theme {mode} {
	if {$mode == "dark"} {
		ttk::style theme use "sun-valley-dark"

		array set colors {
		    -fg             "#ffffff"
		    -bg             "#1c1c1c"
		    -disabledfg     "#595959"
		    -selectfg       "#ffffff"
		    -selectbg       "#2f60d8"
		}
        
        ttk::style configure . \
            -background $colors(-bg) \
            -foreground $colors(-fg) \
            -troughcolor $colors(-bg) \
            -focuscolor $colors(-selectbg) \
            -selectbackground $colors(-selectbg) \
            -selectforeground $colors(-selectfg) \
            -insertwidth 1 \
            -insertcolor $colors(-fg) \
            -fieldbackground $colors(-selectbg) \
            -font {"Segoe Ui" 10} \
            -borderwidth 1 \
            -relief flat

        tk_setPalette \
        	background [ttk::style lookup . -background] \
            foreground [ttk::style lookup . -foreground] \
            highlightColor [ttk::style lookup . -focuscolor] \
            selectBackground [ttk::style lookup . -selectbackground] \
            selectForeground [ttk::style lookup . -selectforeground] \
            activeBackground [ttk::style lookup . -selectbackground] \
            activeForeground [ttk::style lookup . -selectforeground]
        
        ttk::style map . -foreground [list disabled $colors(-disabledfg)]

        option add *font [ttk::style lookup . -font]
        option add *Menu.selectcolor $colors(-fg)
        option add *Menu.background #2f2f2f
    
	} elseif {$mode == "light"} {
		ttk::style theme use "sun-valley-light"

		array set colors {
		    -fg             "#202020"
		    -bg             "#fafafa"
		    -disabledfg     "#a0a0a0"
		    -selectfg       "#ffffff"
		    -selectbg       "#2f60d8"
		}

        ttk::style configure . \
            -background $colors(-bg) \
            -foreground $colors(-fg) \
            -troughcolor $colors(-bg) \
            -focuscolor $colors(-selectbg) \
            -selectbackground $colors(-selectbg) \
            -selectforeground $colors(-selectfg) \
            -insertwidth 1 \
            -insertcolor $colors(-fg) \
            -fieldbackground $colors(-selectbg) \
            -font {"Segoe Ui" 10} \
            -borderwidth 0 \
            -relief flat

        tk_setPalette background [ttk::style lookup . -background] \
            foreground [ttk::style lookup . -foreground] \
            highlightColor [ttk::style lookup . -focuscolor] \
            selectBackground [ttk::style lookup . -selectbackground] \
            selectForeground [ttk::style lookup . -selectforeground] \
            activeBackground [ttk::style lookup . -selectbackground] \
            activeForeground [ttk::style lookup . -selectforeground]
        
        ttk::style map . -foreground [list disabled $colors(-disabledfg)]

        option add *font [ttk::style lookup . -font]
        option add *Menu.selectcolor $colors(-fg)
        option add *Menu.background #e7e7e7
	}
}
