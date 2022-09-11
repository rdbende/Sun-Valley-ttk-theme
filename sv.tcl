source [file join [file dirname [info script]] theme light.tcl]
source [file join [file dirname [info script]] theme dark.tcl]


proc set_theme {mode} {
  if {$mode == "dark"} {
    ttk::style theme use "sun-valley-dark"
    
    ttk::style configure . \
      -background $ttk::theme::sv_dark::theme_colors(-bg) \
      -foreground $ttk::theme::sv_dark::theme_colors(-fg) \
      -troughcolor $ttk::theme::sv_dark::theme_colors(-bg) \
      -focuscolor $ttk::theme::sv_dark::theme_colors(-selbg) \
      -selectbackground $ttk::theme::sv_dark::theme_colors(-selbg) \
      -selectforeground $ttk::theme::sv_dark::theme_colors(-selfg) \
      -insertwidth 1 \
      -insertcolor $ttk::theme::sv_dark::theme_colors(-fg) \
      -fieldbackground $ttk::theme::sv_dark::theme_colors(-bg) \
      -font {"Segoe UI" 10} \
      -borderwidth 0 \
      -relief flat

    tk_setPalette \
      background $ttk::theme::sv_dark::theme_colors(-bg) \
      foreground $ttk::theme::sv_dark::theme_colors(-fg) \
      highlightColor $ttk::theme::sv_dark::theme_colors(-selbg) \
      selectBackground $ttk::theme::sv_dark::theme_colors(-selbg) \
      selectForeground $ttk::theme::sv_dark::theme_colors(-selfg) \
      activeBackground $ttk::theme::sv_dark::theme_colors(-selbg) \
      activeForeground $ttk::theme::sv_dark::theme_colors(-selfg)
    
    ttk::style map . -foreground [list disabled $ttk::theme::sv_dark::theme_colors(-disfg)]

    option add *font {"Segoe UI" 10}
    option add *tearOff 0
    option add *Menu.selectColor $ttk::theme::sv_dark::theme_colors(-fg)
  
  } elseif {$mode == "light"} {
    ttk::style theme use "sun-valley-light"
    
    ttk::style configure . \
      -background $ttk::theme::sv_light::theme_colors(-bg) \
      -foreground $ttk::theme::sv_light::theme_colors(-fg) \
      -troughcolor $ttk::theme::sv_light::theme_colors(-bg) \
      -focuscolor $ttk::theme::sv_light::theme_colors(-selbg) \
      -selectbackground $ttk::theme::sv_light::theme_colors(-selbg) \
      -selectforeground $ttk::theme::sv_light::theme_colors(-selfg) \
      -insertwidth 1 \
      -insertcolor $ttk::theme::sv_light::theme_colors(-fg) \
      -fieldbackground $ttk::theme::sv_light::theme_colors(-bg) \
      -font {"Segoe UI" 10} \
      -borderwidth 0 \
      -relief flat

    tk_setPalette \
      background $ttk::theme::sv_light::theme_colors(-bg) \
      foreground $ttk::theme::sv_light::theme_colors(-fg) \
      highlightColor $ttk::theme::sv_light::theme_colors(-selbg) \
      selectBackground $ttk::theme::sv_light::theme_colors(-selbg) \
      selectForeground $ttk::theme::sv_light::theme_colors(-selfg) \
      activeBackground $ttk::theme::sv_light::theme_colors(-selbg) \
      activeForeground $ttk::theme::sv_light::theme_colors(-selfg)
    
    ttk::style map . -foreground [list disabled $ttk::theme::sv_light::theme_colors(-disfg)]

    option add *font {"Segoe UI" 10}
    option add *tearOff 0
    option add *Menu.selectColor $ttk::theme::sv_light::theme_colors(-fg)
  }
}
