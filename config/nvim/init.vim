call plug#begin()

Plug 'mg979/vim-visual-multi'
Plug 'chrisbra/vim-commentary'
Plug 'matze/vim-move'
Plug 'lervag/vimtex'

Plug 'neoclide/coc.nvim'
Plug 'jackguo380/vim-lsp-cxx-highlight'

call plug#end()

" c++ syntax highlighting
let g:cpp_class_scope_highlight = 1
let g:cpp_member_variable_highlight = 1
let g:cpp_class_decl_highlight = 1

set number
set whichwrap+=<,>,[,]
set tabstop=4       " number of visual spaces per TAB
set softtabstop=4   " number of spaces in tab when editing
set shiftwidth=4    " number of spaces to use for autoindent
set expandtab       " tabs are space
set copyindent
nmap <ESC>[1;5D <C-Left>
nmap <ESC>[1;5C <C-Right>
cmap <ESC>[1;5D <C-Left>
cmap <ESC>[1;5C <C-Right>
imap <ESC>[1;5D <C-o><C-Left>
imap <ESC>[1;5C <C-o><C-Right>
