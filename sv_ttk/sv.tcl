package require Tk 8.6

source [file join [file dirname [info script]] theme light.tcl]
source [file join [file dirname [info script]] theme dark.tcl]


if {[tk windowingsystem] == "win32"} {
  set static ""
} else {
  set static " static"
}

# Run to continue apply the theme
proc start_config_theme {fallback_list} {
  # Logics for fallback font
  # Procedure to find the first available font
  proc select_available_font {font_list} {
      foreach font $font_list {
          if {[lsearch [font families] $font] != -1} {
              return $font
          }
      }
      return "Arial"  ; # Default fallback font
  }
    # Find the best available font
  set selected_font [select_available_font $fallback_list]

  # Debug
  #puts "tcl font list: [font families]"
  #puts "tcl selected font: $selected_font"

  # Use the selected font in the theme
  font create SunValleyCaptionFont -family $selected_font -size -12
  font create SunValleyBodyFont -family $selected_font -size -14
  font create SunValleyBodyStrongFont -family $selected_font -weight bold -size -14
  font create SunValleyBodyLargeFont -family $selected_font -size -18
  font create SunValleySubtitleFont -family $selected_font -weight bold -size -20
  font create SunValleyTitleFont -family $selected_font -weight bold -size -28
  font create SunValleyTitleLargeFont -family $selected_font -weight bold -size -40
  font create SunValleyDisplayFont -family $selected_font -weight bold -size -68

  proc config_entry_font {w} {
    set font_config [$w config -font]
    if {[lindex $font_config 3] != [lindex $font_config 4]} {
      return
    }
    if {[ttk::style theme use] in {"sun-valley-dark" "sun-valley-light"}} {
      $w configure -font SunValleyBodyFont
    }
  }


  proc config_menus {w} {
    if {[tk windowingsystem] == "aqua" || [tk windowingsystem] == "win32"} {
      return
    }

    set theme [ttk::style theme use]
    if {$theme == "sun-valley-dark"} {
      $w configure \
        -relief solid \
        -borderwidth 1 \
        -activeborderwidth 0 \
        -background "#292929" \
        -activebackground $ttk::theme::sv_dark::colors(-selbg) \
        -activeforeground $ttk::theme::sv_dark::colors(-selfg) \
        -selectcolor $ttk::theme::sv_dark::colors(-selfg)
    } elseif {$theme == "sun-valley-light"} {
      $w configure \
        -relief solid \
        -borderwidth 1 \
        -activeborderwidth 0 \
        -background "#e7e7e7" \
        -activebackground $ttk::theme::sv_dark::colors(-selbg) \
        -activeforeground $ttk::theme::sv_dark::colors(-selfg) \
        -selectcolor $ttk::theme::sv_dark::colors(-selfg)
    }

    if {[[winfo toplevel $w] cget -menu] != $w} {
      if {$theme == "sun-valley-dark"} {
        $w configure -borderwidth 0 -background $ttk::theme::sv_dark::colors(-bg)
      } elseif {$theme == "sun-valley-light"} {
        $w configure -borderwidth 0 -background $ttk::theme::sv_light::colors(-bg)
      }
    }
  }


  proc configure_colors {} {
    set theme [ttk::style theme use]
    if {$theme == "sun-valley-dark"} {
      ttk::style configure . \
        -background $ttk::theme::sv_dark::colors(-bg) \
        -foreground $ttk::theme::sv_dark::colors(-fg) \
        -troughcolor $ttk::theme::sv_dark::colors(-bg) \
        -focuscolor $ttk::theme::sv_dark::colors(-selbg) \
        -selectbackground $ttk::theme::sv_dark::colors(-selbg) \
        -selectforeground $ttk::theme::sv_dark::colors(-selfg) \
        -insertwidth 1 \
        -insertcolor $ttk::theme::sv_dark::colors(-fg) \
        -fieldbackground $ttk::theme::sv_dark::colors(-bg) \
        -font SunValleyBodyFont \
        -borderwidth 0 \
        -relief flat

      tk_setPalette \
        background $ttk::theme::sv_dark::colors(-bg) \
        foreground $ttk::theme::sv_dark::colors(-fg) \
        highlightColor $ttk::theme::sv_dark::colors(-selbg) \
        selectBackground $ttk::theme::sv_dark::colors(-selbg) \
        selectForeground $ttk::theme::sv_dark::colors(-selfg) \
        activeBackground $ttk::theme::sv_dark::colors(-selbg) \
        activeForeground $ttk::theme::sv_dark::colors(-selfg)

      ttk::style map . -foreground [list disabled $ttk::theme::sv_dark::colors(-disfg)]
    } elseif {$theme == "sun-valley-light"} {
      ttk::style configure . \
        -background $ttk::theme::sv_light::colors(-bg) \
        -foreground $ttk::theme::sv_light::colors(-fg) \
        -troughcolor $ttk::theme::sv_light::colors(-bg) \
        -focuscolor $ttk::theme::sv_light::colors(-selbg) \
        -selectbackground $ttk::theme::sv_light::colors(-selbg) \
        -selectforeground $ttk::theme::sv_light::colors(-selfg) \
        -insertwidth 1 \
        -insertcolor $ttk::theme::sv_light::colors(-fg) \
        -fieldbackground $ttk::theme::sv_light::colors(-bg) \
        -font SunValleyBodyFont \
        -borderwidth 0 \
        -relief flat

      tk_setPalette \
        background $ttk::theme::sv_light::colors(-bg) \
        foreground $ttk::theme::sv_light::colors(-fg) \
        highlightColor $ttk::theme::sv_light::colors(-selbg) \
        selectBackground $ttk::theme::sv_light::colors(-selbg) \
        selectForeground $ttk::theme::sv_light::colors(-selfg) \
        activeBackground $ttk::theme::sv_light::colors(-selbg) \
        activeForeground $ttk::theme::sv_light::colors(-selfg)

      ttk::style map . -foreground [list disabled $ttk::theme::sv_light::colors(-disfg)]
    }
  }


  bind [winfo class .] <<ThemeChanged>> {+configure_colors}
  bind TEntry <<ThemeChanged>> {+config_entry_font %W}
  bind TCombobox <<ThemeChanged>> {+config_entry_font %W}
  bind TSpinbox <<ThemeChanged>> {+config_entry_font %W}
  bind Menu <<ThemeChanged>> {+config_menus %W}
}
