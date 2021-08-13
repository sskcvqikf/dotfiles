call plug#begin()

Plug 'neoclide/coc.nvim'

call plug#end()

function! s:insert_gates()
    let reponame = trim(system("basename $(git rev-parse --show-toplevel)"))
    let filename = expand("%:t")
    let gatename = substitute(toupper(reponame . "_" . filename . "_"), "\\.", "_", "g")
    execute "normal! i#ifndef " . gatename
    execute "normal! o#define " . gatename . " "
    execute "normal! o#pragma once\n\n\n"
    execute "normal! o#endif // " . gatename
    normal! kk
endfunction

let mapleader = " "
nnoremap <space> <Nop>

set number
set whichwrap+=<,>,[,]
set tabstop=4       " number of visual spaces per TAB
set softtabstop=4   " number of spaces in tab when editing
set shiftwidth=4    " number of spaces to use for autoindent
set expandtab       " tabs are space
set copyindent

nnoremap <ESC>[1;5D <C-Left>
nnoremap <ESC>[1;5C <C-Right>
inoremap <ESC>[1;5D <C-o><C-Left>
inoremap <ESC>[1;5C <C-o><C-Right>

noremap L $
noremap H ^
noremap J 25j
noremap K 25k

nnoremap <leader>v viw
nnoremap <leader>b gT
nnoremap <leader>n gt

noremap <leader>h <c-w>h
noremap <leader>l <c-w>l
noremap <leader>j <c-w>j
noremap <leader>k <c-w>k

inoremap <c-q> <esc>

autocmd FileType c,cpp,cc,hh,h,hpp vnoremap <buffer> <c-c> <esc>`<i/*<esc>`>lla*/<esc>
autocmd FileType c,cpp,cc,hh,h,hpp nnoremap <buffer> <c-c> I//<space><esc>
autocmd FileType c,cpp,cc,hh,h,hpp inoremap <buffer> <c-c> //<space>

hi CocFloating ctermbg=Black
hi CocErrorFloat ctermbg=Black ctermfg=Red
hi CocWarningFloat ctermbg=Black ctermfg=Red

autocmd BufNewFile *.{h,hpp,hh} call <SID>insert_gates()

set statusline=%f%m%r%y%=%c,[%l/%L]%p%%
