(package-initialize)

(setq package-archives '(("gnu"   . "http://elpa.emacs-china.org/gnu/")
                         ("melpa" . "http://elpa.emacs-china.org/melpa/")))

(defun open-init-file()
  (interactive)
  (find-file "~/.emacs.d/init.el"))
(define-key global-map [f1] 'open-init-file)

(defun open-remote-file()
  (interactive)
  (find-file "/plink:pi@192.168.1.104:/home/pi"))
(define-key global-map [f12]  'open-remote-file)

(defun refresh-file ()  
  (interactive)  
  (revert-buffer t (not (buffer-modified-p)) t))    
(global-set-key [f5] 'refresh-file)

(global-disable-mouse-mode t)
(tool-bar-mode 0)  
(menu-bar-mode 0)  
(scroll-bar-mode 0) 
(global-linum-mode t) 
(setq-default cursor-type 'bar) 
(set-cursor-color "#ffffff") 
(add-to-list 'default-frame-alist '(fullscreen . maximized))
(setq visible-bell 0)
(load-theme 'deeper-blue )

;; Setting English Font
(set-face-attribute
 'default nil :font "Courier New-14")
;Setting Chinese Font
(dolist (charset '(kana han symbol cjk-misc bopomofo))
 (set-fontset-font (frame-parameter nil 'font)
           charset
           (font-spec :family "Microsoft Yahei" :size 16)))


(ido-mode t)
(global-auto-complete-mode t)
(yas-global-mode t)

(window-numbering-mode t)
(global-undo-tree-mode t)
(global-auto-highlight-symbol-mode t)
(electric-pair-mode t)
(eldoc-mode t)

(elpy-enable)
(setq elpy-rpc-timeout nil)

(global-set-key
 "\M-x"
 (lambda ()
   (interactive)
   (call-interactively
    (intern
     (ido-completing-read
      "M-x "
      (all-completions "" obarray 'commandp))))))

(require 'xcscope)

(global-set-key (kbd "M-SPC")          'set-mark-command) 
(global-set-key (kbd "C-c l")          'ido-switch-buffer)
(global-set-key (kbd "C-c c")          'comment-region)
(global-set-key (kbd "C-c u")          'uncomment-region)
(global-set-key (kbd "C-x e")          'eshell)
(global-set-key (kbd "C-c SPC")        'ace-jump-word-mode)
(global-set-key (kbd "C-c j")          'godef-jump)
(global-set-key (kbd "C-c f")          'find-name-dired)
(global-set-key (kbd "C-c g")          'cscope-find-global-definition)
(global-set-key (kbd "C-c v")          'vc-diff)
(global-set-key (kbd "C-c r")          'rgrep)

(setq default-tab-width 4)
(setq-default indent-tabs-mode nil)
(setq c-default-style "linux"
      c-basic-offset 4)

(add-hook 'go-mode-hook 'go-eldoc-setup)
(add-hook 'go-mode-hook '(lambda ()
                           (local-set-key (kbd "C-c C-k") 'godoc)))

(add-hook 'before-save-hook 'gofmt-before-save)

(require 'go-autocomplete)
(require 'flymake-go)

(require 'highlight-symbol)
(global-set-key [(control f3)] 'highlight-symbol)
(global-set-key [f3] 'highlight-symbol-next)
(global-set-key [(shift f3)] 'highlight-symbol-prev)
(global-set-key [(meta f3)] 'highlight-symbol-query-replace)

(setq ffip-project-root "~")
(add-hook 'emacs-lisp-mode-hook 'turn-on-eldoc-mode)
(custom-set-variables
 ;; custom-set-variables was added by Custom.
 ;; If you edit it by hand, you could mess it up, so be careful.
 ;; Your init file should contain only one such instance.
 ;; If there is more than one, they won't work right.
 '(package-selected-packages
   (quote
    (magit org-link-minor-mode highlight-parentheses projectile disable-mouse elpy highlight-symbol arduino-mode yasnippet xcscope window-numbering undo-tree go-eldoc go-autocomplete flymake-go flycheck find-file-in-project electric-spacing eldoc-eval c-eldoc auto-highlight-symbol ace-jump-mode))))
(custom-set-faces
 ;; custom-set-faces was added by Custom.
 ;; If you edit it by hand, you could mess it up, so be careful.
 ;; Your init file should contain only one such instance.
 ;; If there is more than one, they won't work right.
 )

(setq password-cache-expiry 36000)
(setq explicit-shell-file-name "/bin/bash")

(if (eq system-type 'windows-nt)
    (setq ffip-find-executable "d:/cygwin64/bin/find"))

(setq ffip-project-root "f:/linux/kernel")

(set-default 'truncate-lines t)

(define-globalized-minor-mode global-highlight-parentheses-mode
  highlight-parentheses-mode
  (lambda ()
    (highlight-parentheses-mode t)))
(global-highlight-parentheses-mode t)

(remove-hook 'elpy-modules 'elpy-module-flymake)
(global-flycheck-mode)

(global-set-key (kbd "C-x g") 'magit-status)

(prefer-coding-system 'utf-8)
(set-default-coding-systems 'utf-8)
(set-language-environment 'utf-8)
(set-selection-coding-system 'utf-8)

(setq exec-path (append exec-path
                        '("D:/cygwin64/bin/")))
(setq grep-program "D:/cygwin64/bin/grep.exe")
(setq find-program "D:/cygwin64/bin/find.exe")
