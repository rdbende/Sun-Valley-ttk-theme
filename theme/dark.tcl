source [file join [file dirname [info script]] sprites_dark.tcl]

namespace eval ttk::theme::sv_dark {
  package provide ttk::theme::sv_dark 2.4

  array set theme_colors {
    -fg      "#fafafa"
    -bg      "#1c1c1c"
    -disfg   "#595959"
    -selfg   "#ffffff"
    -selbg   "#2f60d8"
    -accent  "#57c8ff"
  }

  proc load_images {imgfile} {
    variable I
    image create photo spritesheet -file $imgfile -format png
    foreach {name x y width height} $::spriteinfo {
      set I($name) [image create photo -width $width -height $height]
      $I($name) copy spritesheet -from $x $y [expr {$x+$width}] [expr {$y+$height}]
    }
  }

  load_images [file join [file dirname [info script]] spritesheet_dark.png]

  ttk::style theme create sun-valley-dark -parent clam -settings {
        
    # Button
    ttk::style layout TButton {
      Button.button -children {
        Button.padding -children {
          Button.label -side left -expand 1
        } 
      }
    }

    ttk::style configure TButton -padding {8 2 8 3} -anchor center -foreground $theme_colors(-fg)
    ttk::style map TButton -foreground [list disabled "#7a7a7a" pressed "#d0d0d0"]
    
    ttk::style element create Button.button image \
      [list $I(button-rest) \
        {selected disabled} $I(button-dis) \
        disabled $I(button-dis) \
        selected $I(button-rest) \
        pressed $I(button-pressed) \
        {active focus} $I(button-focus-hover) \
        active $I(button-hover) \
        focus $I(button-focus) \
      ] -border 4 -sticky nsew

    # Toolbutton
    ttk::style layout Toolbutton {
      Toolbutton.button -children {
        Toolbutton.padding -children {
          Toolbutton.label -side left -expand 1
        } 
      }
    }

    ttk::style configure Toolbutton -padding {8 2 8 3} -anchor center
    
    ttk::style element create Toolbutton.button image \
      [list $I(empty) \
        disabled $I(button-dis) \
        pressed $I(button-pressed) \
        {active focus} $I(button-focus-hover) \
        active $I(button-hover) \
        focus $I(button-focus) \
      ] -border 4 -sticky nsew

    # Accent.TButton
    ttk::style layout Accent.TButton {
      AccentButton.button -children {
        AccentButton.padding -children {
          AccentButton.label -side left -expand 1
        } 
      }
    }

    ttk::style configure Accent.TButton -padding {8 2 8 3} -anchor center -foreground "#000000"
    ttk::style map Accent.TButton -foreground [list pressed "#25536a" disabled "#a5a5a5"]

    ttk::style element create AccentButton.button image \
      [list $I(button-accent-rest) \
        {selected disabled} $I(button-accent-dis) \
        disabled $I(button-accent-dis) \
        {active focus} $I(button-accent-focus-hover) \
        focus $I(button-accent-focus) \
        selected $I(button-accent-rest) \
        pressed $I(button-accent-pressed) \
        active $I(button-accent-hover) \
      ] -border 4 -sticky nsew

    # Menubutton
    ttk::style layout TMenubutton {
      Menubutton.button -children {
        Menubutton.padding -children {
          Menubutton.label -side left -expand 1
          Menubutton.indicator -side right -sticky nsew
        }
      }
    }

    ttk::style configure TMenubutton -padding {8 2 13 3}

    ttk::style element create Menubutton.button image \
      [list $I(button-rest) \
        disabled $I(button-dis) \
        pressed $I(button-pressed) \
        {active focus} $I(button-focus-hover) \
        active $I(button-hover) \
        focus $I(button-focus) \
      ] -border 4 -sticky nsew 

    ttk::style element create Menubutton.indicator image $I(down) -width 10 -sticky e

    # OptionMenu
    ttk::style layout TOptionMenu {
      OptionMenu.button -children {
        OptionMenu.padding -children {
          OptionMenu.label -side left -expand 1
          OptionMenu.indicator -side right -sticky nsew
        }
      }
    }
    
    ttk::style configure TOptionMenu -padding {8 2 13 3}

    ttk::style element create OptionMenu.button image \
      [list $I(button-rest) \
        disabled $I(button-dis) \
        pressed $I(button-pressed) \
        {active focus} $I(button-focus-hover) \
        active $I(button-hover) \
        focus $I(button-focus) \
      ] -border 4 -sticky nsew 

    ttk::style element create OptionMenu.indicator image $I(down) -width 10 -sticky e

    # Checkbutton
    ttk::style layout TCheckbutton {
      Checkbutton.button -children {
        Checkbutton.padding -children {
          Checkbutton.indicator -side left
          Checkbutton.label -side right -expand 1
        }
      }
    }

    ttk::style configure TCheckbutton -padding 4

    ttk::style element create Checkbutton.indicator image \
      [list $I(check-unsel-rest) \
        {alternate disabled} $I(check-tri-dis) \
        {selected disabled} $I(check-dis) \
        disabled $I(check-unsel-dis) \
        {pressed alternate} $I(check-tri-hover) \
        {active focus alternate} $I(check-tri-focus-hover) \
        {active alternate} $I(check-tri-hover) \
        {focus alternate} $I(check-tri-focus) \
        alternate $I(check-tri-rest) \
        {pressed selected} $I(check-hover) \
        {active focus selected} $I(check-focus-hover) \
        {active selected} $I(check-hover) \
        {focus selected} $I(check-focus) \
        selected $I(check-rest) \
        {pressed !selected} $I(check-unsel-pressed) \
        {active focus} $I(check-unsel-focus-hover) \
        active $I(check-unsel-hover) \
        focus $I(check-unsel-focus) \
      ] -width 26 -sticky w

    # Switch.TCheckbutton
    ttk::style layout Switch.TCheckbutton {
      Switch.button -children {
        Switch.padding -children {
          Switch.indicator -side left
          Switch.label -side right -expand 1
        }
      }
    }

    ttk::style element create Switch.indicator image \
      [list $I(switch-off-rest) \
        {selected disabled} $I(switch-dis) \
        disabled $I(switch-off-dis) \
        {pressed selected} $I(switch-pressed) \
        {active focus selected} $I(switch-focus-hover) \
        {active selected} $I(switch-hover) \
        {focus selected} $I(switch-focus) \
        selected $I(switch-rest) \
        {pressed !selected} $I(switch-off-pressed) \
        {active focus} $I(switch-off-focus-hover) \
        active $I(switch-off-hover) \
        focus $I(switch-off-focus) \
      ] -width 46 -sticky w

    # Toggle.TButton
    ttk::style layout Toggle.TButton {
      ToggleButton.button -children {
        ToggleButton.padding -children {
          ToggleButton.label -side left -expand 1
        } 
      }
    }

    ttk::style configure Toggle.TButton -padding {8 2 8 3} -anchor center -foreground $theme_colors(-fg)

    ttk::style map Toggle.TButton -foreground \
      [list {selected disabled} "#a5a5a5" \
        {selected pressed} "#d0d0d0" \
        selected "#000000" \
        pressed "#25536a" \
        disabled "#7a7a7a"
      ]

    ttk::style element create ToggleButton.button image \
      [list $I(button-rest) \
        {selected disabled} $I(button-accent-dis) \
        disabled $I(button-dis) \
        {pressed selected} $I(button-rest) \
        {active focus selected} $I(button-accent-focus-hover) \
        {active selected} $I(button-accent-hover) \
        {focus selected} $I(button-accent-focus) \
        selected $I(button-accent-rest) \
        {pressed !selected} $I(button-accent-rest) \
        {active focus} $I(button-focus-hover) \
        active $I(button-hover) \
        focus $I(button-focus) \
      ] -border 4 -sticky nsew

    # Radiobutton
    ttk::style layout TRadiobutton {
      Radiobutton.button -children {
        Radiobutton.padding -children {
          Radiobutton.indicator -side left
          Radiobutton.label -side right -expand 1
        }
      }
    }

    ttk::style configure TRadiobutton -padding 4

    ttk::style element create Radiobutton.indicator image \
      [list $I(radio-unsel-rest) \
        {selected disabled} $I(radio-dis) \
        disabled $I(radio-unsel-dis) \
        {pressed selected} $I(radio-pressed) \
        {active focus selected} $I(radio-focus-hover) \
        {active selected} $I(radio-hover) \
        {focus selected} $I(radio-focus) \
        selected $I(radio-rest) \
        {pressed !selected} $I(radio-unsel-pressed) \
        {active focus} $I(radio-unsel-focus-hover) \
        active $I(radio-unsel-hover) \
        focus $I(radio-unsel-focus) \
      ] -width 26 -sticky w

    # Entry
    ttk::style configure TEntry -foreground $theme_colors(-fg) -padding {6 1 4 2}
    ttk::style map TEntry -foreground [list disabled "#757575" pressed "#cfcfcf"]

    ttk::style element create Entry.field image \
      [list $I(textbox-rest) \
        {focus hover !invalid} $I(textbox-focus) \
        invalid $I(textbox-error) \
        disabled $I(textbox-dis) \
        {focus !invalid} $I(textbox-focus) \
        hover $I(textbox-hover) \
      ] -border 5 -sticky nsew

    # Combobox
    ttk::style layout TCombobox {
      Combobox.field -sticky nsew -children {
        Combobox.arrow -side right -sticky ns
        Combobox.padding -sticky nsew -children {
          Combobox.textarea -sticky nsew
        }
      }
    }
        
    ttk::style configure TCombobox -foreground $theme_colors(-fg) -padding {6 1 0 2}
    ttk::style configure ComboboxPopdownFrame -borderwidth 1 -relief solid
    ttk::style map TCombobox -foreground [list disabled "#757575" pressed "#cfcfcf"]
    
    ttk::style map TCombobox -selectbackground [list \
      {readonly hover} $theme_colors(-selbg) \
      {readonly focus} $theme_colors(-selbg) \
    ] -selectforeground [list \
      {readonly hover} $theme_colors(-selfg) \
      {readonly focus} $theme_colors(-selfg) \
    ]

    ttk::style element create Combobox.field image \
      [list $I(textbox-rest) \
        {readonly focus} $I(button-focus) \
        {readonly disabled} $I(button-dis) \
        {readonly pressed} $I(button-pressed) \
        {readonly hover} $I(button-hover) \
        readonly $I(button-rest) \
        {focus hover !invalid} $I(textbox-focus) \
        invalid $I(textbox-error) \
        disabled $I(textbox-dis) \
        focus $I(textbox-focus) \
        {focus !invalid} $I(textbox-focus) \
        hover $I(textbox-hover) \
      ] -border 5
        
    ttk::style element create Combobox.arrow image $I(down) -width 34 -sticky {}

    # Spinbox
    ttk::style layout TSpinbox {
      Spinbox.field -side top -sticky we -children {
        Spinbox.downarrow -side right -sticky ns
        Spinbox.uparrow -side right -sticky ns
        Spinbox.padding -sticky nswe -children {
          Spinbox.textarea -sticky nsew
        }
      }
    }

    ttk::style configure TSpinbox -foreground $theme_colors(-fg) -padding {6 1 0 2}
    ttk::style map TSpinbox -foreground [list disabled "#757575" pressed "#cfcfcf"]

    ttk::style element create Spinbox.field image \
      [list $I(textbox-rest) \
        {focus hover !invalid} $I(textbox-focus) \
        invalid $I(textbox-error) \
        disabled $I(textbox-dis) \
        focus $I(textbox-focus) \
        {focus !invalid} $I(textbox-focus) \
        hover $I(textbox-hover) \
      ] -border 5 -sticky nsew

    ttk::style element create Spinbox.uparrow image $I(up) -width 34 -height 16 -sticky {}
    ttk::style element create Spinbox.downarrow image $I(down) -width 34 -height 16 -sticky {}

    # Progressbar
    ttk::style element create Horizontal.Progressbar.trough image $I(progressbar-trough-hor) -border 1 -sticky ew
    ttk::style element create Horizontal.Progressbar.pbar image $I(progressbar-bar-hor) -border 2 -sticky ew

    ttk::style element create Vertical.Progressbar.trough image $I(progressbar-trough-vert) -border 1 -sticky ns
    ttk::style element create Vertical.Progressbar.pbar image $I(progressbar-bar-vert) -border 2 -sticky ns

    # Scale
    ttk::style element create Horizontal.Scale.trough image $I(slider-trough-hor) \
      -border 5 -padding 0 -sticky {ew}

    ttk::style element create Vertical.Scale.trough image $I(slider-trough-vert) \
      -border 5 -padding 0 -sticky {ns}

    ttk::style element create Scale.slider image \
      [list $I(slider-thumb-rest) \
        disabled $I(slider-thumb-dis) \
        pressed $I(slider-thumb-pressed) \
        {active focus} $I(slider-thumb-focus-hover) \
        active $I(slider-thumb-hover) \
        focus $I(slider-thumb-focus) \
      ] -sticky {}

    # Scrollbar
    ttk::style layout Vertical.TScrollbar {
      Vertical.Scrollbar.trough -sticky ns -children {
        Vertical.Scrollbar.uparrow -side top
        Vertical.Scrollbar.downarrow -side bottom
        Vertical.Scrollbar.thumb -expand 1
      }
    }

    ttk::style layout Horizontal.TScrollbar {
      Horizontal.Scrollbar.trough -sticky ew -children {
        Horizontal.Scrollbar.leftarrow -side left
        Horizontal.Scrollbar.rightarrow -side right
        Horizontal.Scrollbar.thumb -expand 1
      }
    }

    ttk::style element create Horizontal.Scrollbar.trough image $I(scrollbar-trough-hor) -sticky ew -border 6
    ttk::style element create Horizontal.Scrollbar.thumb image $I(scrollbar-thumb-hor) -sticky ew -border 3

    ttk::style element create Horizontal.Scrollbar.rightarrow image $I(scrollbar-right) -sticky e -width 13
    ttk::style element create Horizontal.Scrollbar.leftarrow image $I(scrollbar-left) -sticky w -width 13

    ttk::style element create Vertical.Scrollbar.trough image $I(scrollbar-trough-vert) -sticky ns -border 6
    ttk::style element create Vertical.Scrollbar.thumb image $I(scrollbar-thumb-vert) -sticky ns -border 3

    ttk::style element create Vertical.Scrollbar.uparrow image $I(scrollbar-up) -sticky n -height 13
    ttk::style element create Vertical.Scrollbar.downarrow image $I(scrollbar-down) -sticky s -height 13

    # Separator
    ttk::style element create Separator.separator image $I(sep) -width 1 -height 1

    # Sizegrip
    ttk::style element create Sizegrip.sizegrip image $I(grip) -sticky nsew

    # Card
    ttk::style layout Card.TFrame {
      Card.field {
        Card.padding -expand 1 
      }
    }

    ttk::style element create Card.field image $I(card) -border 10 -padding 4 -sticky nsew

    # Labelframe
    ttk::style layout TLabelframe {
      Labelframe.border {
        Labelframe.padding -expand 1 -children {
          Labelframe.label -side left
        }
      }
    }

    ttk::style element create Labelframe.border image $I(card) -border 5 -padding 4 -sticky nsew
    ttk::style configure TLabelframe.Label -font SunValleyBodyStrongFont -foreground "#9e9e9e"

    # Notebook
    ttk::style layout TNotebook {
      Notebook.border -children {
        TNotebook.Tab -expand 1
      }
    }

    ttk::style configure TNotebook -padding 1
    ttk::style configure TNotebook.Tab -focuscolor $theme_colors(-accent)
    ttk::style element create Notebook.border image $I(notebook-border) -border 5 -padding 5

    ttk::style element create Notebook.tab image \
      [list $I(tab-rest) \
        selected $I(tab-selected) \
        active $I(tab-hover) \
      ] -border 13 -padding {16 14 16 6} -height 32

    # Treeview
    ttk::style configure Treeview \
        -background $theme_colors(-bg) \
        -rowheight [expr {[font metrics SunValleyBodyFont -linespace] + 4}] \
        -font SunValleyBodyFont
    ttk::style map Treeview \
      -background [list selected "#292929"] \
      -foreground [list selected $theme_colors(-selfg)]

    ttk::style element create Treeview.field image $I(card) -border 5 -width 0 -height 0
    
    ttk::style element create Treeheading.cell image \
      [list $I(heading-rest) \
        pressed $I(heading-pressed) \
        active $I(heading-hover)
      ] -border 5 -padding 15 -sticky nsew
    
    ttk::style element create Treeitem.indicator image \
      [list $I(right) \
        user2 $I(empty) \
        user1 $I(down) \
      ] -width 26 -sticky {}

    # Panedwindow
    ttk::style configure Sash -lightcolor "#9e9e9e" -darkcolor "#9e9e9e" -bordercolor "#9e9e9e" -sashthickness 4 -gripcount 20
  }
}
