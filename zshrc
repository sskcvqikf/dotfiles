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

mkcd() { mkdir -p "$@" && cd "$@"; }
