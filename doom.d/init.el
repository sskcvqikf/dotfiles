(doom! :input
       :completion
       company           ; the ultimate code completion backend
       ivy               ; a search engine for love and life

       :ui
       doom-dashboard    ; a nifty splash screen for Emacs
       doom-quit         ; DOOM quit-message prompts when you quit Emacs
       hl-todo           ; highlight TODO/FIXME/NOTE/DEPRECATED/HACK/REVIEW
       modeline          ; snazzy, Atom-inspired modeline, plus API
       ophints           ; highlight the region an operation acts on
       (popup +defaults)   ; tame sudden yet inevitable temporary windows
       vc-gutter         ; vcs diff in the fringe
       vi-tilde-fringe   ; fringe tildes to mark beyond EOB
       workspaces        ; tab emulation, persistence & separate workspaces

       :editor
       (evil +everywhere); come to the dark side, we have cookies
       file-templates    ; auto-snippets for empty files
       fold              ; (nigh) universal code folding
       snippets          ; my elves. They type so I don't have to

       :emacs
       dired             ; making dired pretty [functional]
       electric          ; smarter, keyword-based electric-indent
       undo              ; persistent, smarter undo for your inevitable mistakes
       vc                ; version-control and Emacs, sitting in a tree

       :term

       :checkers
       syntax              ; tasing you for every semicolon you forget

       :tools
       (eval +overlay)     ; run code, run (also, repls)
       lookup              ; navigate your code and its documentation
       lsp
       magit             ; a git porcelain for Emacs

       :os
       (:if IS-MAC macos)  ; improve compatibility with macOS

       :lang
       cc                ; C/C++/Obj-C madness
       common-lisp       ; if you've seen one lisp, you've seen them all
       emacs-lisp        ; drown in parentheses
       (haskell +dante)  ; a language that's lazier than I am
       latex             ; writing papers in Emacs has never been so fun
       markdown          ; writing docs for people to ignore
       org               ; organize your plain life in plain text
       python            ; beautiful is better than ugly
       rust              ; Fe2O3.unwrap().unwrap().unwrap().unwrap()
       sh                ; she sells {ba,z,fi}sh shells on the C xor

       :email

       :app

       :config
       (default +bindings +smartparens))
