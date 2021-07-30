HISTFILE=~/.histfile
HISTSIZE=1000
SAVEHIST=1000
PROMPT=': '
RPROMPT='%/'
bindkey -e
zstyle :compinstall filename '$HOME/.zshrc'

setopt HIST_IGNORE_DUPS
bindkey "^[[1;5C" forward-word
bindkey "^[[1;5D" backward-word
bindkey "\e[3~" delete-char 
source /usr/share/zsh/plugins/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh

# COLORING TTY

color0="073642"
color8="002b36"

#: black
color1="dc322f"
color9="cb4b16"

#: red
color2="859900"
color10="586e75"

#: green
color3="b58900"
color11="657b83"

#: yellow
color4="268bd2"
color12="839496"

#: blue
color5="d33682"
color13="6c71c4"

#: magenta
color6="2aa198"
color14="93a1a1"

#: cyan
color7="eee8d5"
color15="fdf6e3"

if [ "$TERM" = "linux" ]; then
    echo -en "\e]P0$color0" #black
    echo -en "\e]P8$color8" #darkgrey
    echo -en "\e]P1$color1" #darkred
    echo -en "\e]P9$color9" #red
    echo -en "\e]P2$color2" #darkgreen
    echo -en "\e]PA$color10" #green
    echo -en "\e]P3$color3" #brown
    echo -en "\e]PB$color11" #yellow
    echo -en "\e]P4$color4" #darkblue
    echo -en "\e]PC$color12" #blue
    echo -en "\e]P5$color5" #darkmagenta
    echo -en "\e]PD$color13" #magenta
    echo -en "\e]P6$color6" #darkcyan
    echo -en "\e]PE$color14" #cyan
    echo -en "\e]P7$color7" #lightgrey
    echo -en "\e]PF$color15" #white
    setfont /usr/share/kbd/consolefonts/Lat2-Terminus16.psfu.gz
    clear # for background artifacting
fi
export SolarizedType=SolarizedDark
