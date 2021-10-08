(load-theme 'solarized-dark t)

(setq org-directory "~/org/")

(setq display-line-numbers-type t)

(nyan-mode)
(global-set-key (kbd "C-x w") 'irony-get-type)

    (add-hook 'c++-mode-hook 'irony-mode)
    (add-hook 'c-mode-hook 'irony-mode)
    (add-hook 'objc-mode-hook 'irony-mode)

    (defun my-irony-mode-hook ()
      (define-key irony-mode-map [remap completion-at-point]
        'irony-completion-at-point-async)
      (define-key irony-mode-map [remap complete-symbol]
        'irony-completion-at-point-async))
    (add-hook 'irony-mode-hook 'my-irony-mode-hook)

(eval-after-load 'company
  '(add-to-list 'company-backends 'company-irony))
