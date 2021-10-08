call plug#begin()

Plug 'neoclide/coc.nvim'
Plug 'karimElghamry/vim-auto-comment'

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
set tabstop=2       " number of visual spaces per TAB
set softtabstop=2   " number of spaces in tab when editing
set shiftwidth=2    " number of spaces to use for autoindent
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
noremap <leader>, :bp<cr>
noremap <leader>. :bN<cr>
noremap <leader>/ :bd<cr>

nmap <silent> <leader>d <Plug>(coc-definition)
nmap <silent> <leader>x <Plug>(coc-type-definition)
nmap <silent> <leader>i <Plug>(coc-implementation)
nmap <silent> <leader>r <Plug>(coc-references)

nnoremap <c-c> :AutoInlineComment<cr>
vnoremap <c-c> :AutoBlockComment<cr>

noremap <c-y> "+y
noremap <c-p> "+p

inoremap <c-q> <esc>

hi CocFloating ctermbg=Black
hi CocErrorFloat ctermbg=Black ctermfg=Red
hi CocWarningFloat ctermbg=Black ctermfg=Red

autocmd BufNewFile *.{h,hpp,hh} call <SID>insert_gates()

set statusline=%f%m%r%y%=%c,[%l/%L]%p%%

let g:autocomment_map_keys = 0
let g:inline_comment_dict = {
		\'//': ['js', 'ts', 'cpp', 'cc', 'cxx', 'h', 'hh', 'hpp', 'hxx', 'dart'],
		\'#': ['py', 'sh'],
		\'"': ['vim'],
		\}

let g:block_comment_dict = {
		\'/*': ['js', 'ts', 'cpp', 'cc', 'cxx', 'h', 'hh', 'hpp', 'hxx', 'dart'],
		\'"""': ['py'],
		\}

