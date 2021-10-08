import os
HOME = os.environ['HOME']

config.set('content.javascript.enabled', True, 'file://*')

config.set('content.javascript.enabled', True, 'chrome://*/*')


config.load_autoconfig()
config.set('content.javascript.enabled', True, 'qute://*/*')
config.set('tabs.padding', { 'top': 2, 'bottom': 5, 'left': 5, 'right': 2 })
config.set('zoom.default', '150%')
config.set('hints.chars', 'abcdefghijklmnopqrstuvwxyz')
config.set('url.searchengines', {"DEFAULT": "https://searx.tuxcloud.net/?q={}"})
config.set('url.start_pages', f'{HOME}/.config/browserhome/index.html')
config.set('url.default_page', f'{HOME}/.config/browserhome/index.html') 

c.zoom.default = '100%'

c.fonts.default_family = ['Source Code Pro']
c.fonts.hints = '10pt monospace'
c.fonts.keyhint = '10pt monospace'
c.fonts.prompts = '10pt monospace'
c.fonts.downloads = '10pt monospace'
c.fonts.statusbar = '10pt monospace'
c.fonts.contextmenu = '10pt monospace'
c.fonts.messages.info = '10pt monospace'
c.fonts.debug_console = '10pt monospace'
c.fonts.completion.entry = '10pt monospace'
c.fonts.completion.category = '10pt monospace'




c.colors.completion.fg = base05

c.colors.completion.odd.bg = base01

c.colors.completion.even.bg = base00

c.colors.completion.category.fg = base0A

c.colors.completion.category.bg = base00

c.colors.completion.category.border.top = base00

c.colors.completion.category.border.bottom = base00

c.colors.completion.item.selected.fg = base05

c.colors.completion.item.selected.bg = base02

c.colors.completion.item.selected.border.top = base02

c.colors.completion.item.selected.border.bottom = base02

c.colors.completion.item.selected.match.fg = base0B

c.colors.completion.match.fg = base0B

c.colors.completion.scrollbar.fg = base05

c.colors.completion.scrollbar.bg = base00

c.colors.contextmenu.disabled.bg = base01

c.colors.contextmenu.disabled.fg = base04

c.colors.contextmenu.menu.bg = base00

c.colors.contextmenu.menu.fg =  base05

c.colors.contextmenu.selected.bg = base02

c.colors.contextmenu.selected.fg = base05

c.colors.downloads.bar.bg = base00

c.colors.downloads.start.fg = base00

c.colors.downloads.start.bg = base0D

c.colors.downloads.stop.fg = base00

c.colors.downloads.stop.bg = base0C

c.colors.downloads.error.fg = base08

c.colors.hints.fg = base00

c.colors.hints.bg = base0A

c.colors.hints.match.fg = base05

c.colors.keyhint.fg = base05

c.colors.keyhint.suffix.fg = base05

c.colors.keyhint.bg = base00

c.colors.messages.error.fg = base00

c.colors.messages.error.bg = base08

c.colors.messages.error.border = base08

c.colors.messages.warning.fg = base00

c.colors.messages.warning.bg = base0E

c.colors.messages.warning.border = base0E

c.colors.messages.info.fg = base05

c.colors.messages.info.bg = base00

c.colors.messages.info.border = base00

c.colors.prompts.fg = base05

c.colors.prompts.border = base00

c.colors.prompts.bg = base00

c.colors.prompts.selected.bg = base02

c.colors.statusbar.normal.fg = base0B

c.colors.statusbar.normal.bg = base00

c.colors.statusbar.insert.fg = base00

c.colors.statusbar.insert.bg = base0D

c.colors.statusbar.passthrough.fg = base00

c.colors.statusbar.passthrough.bg = base0C

c.colors.statusbar.private.fg = base00

c.colors.statusbar.private.bg = base01

c.colors.statusbar.command.fg = base05

c.colors.statusbar.command.bg = base00

c.colors.statusbar.command.private.fg = base05

c.colors.statusbar.command.private.bg = base00

c.colors.statusbar.caret.fg = base00

c.colors.statusbar.caret.bg = base0E

c.colors.statusbar.caret.selection.fg = base00

c.colors.statusbar.caret.selection.bg = base0D

c.colors.statusbar.progress.bg = base0D

c.colors.statusbar.url.fg = base05

c.colors.statusbar.url.error.fg = base08

c.colors.statusbar.url.hover.fg = base05

c.colors.statusbar.url.success.http.fg = base0C

c.colors.statusbar.url.success.https.fg = base0B

c.colors.statusbar.url.warn.fg = base0E

c.colors.tabs.bar.bg = base00

c.colors.tabs.indicator.start = base0D

c.colors.tabs.indicator.stop = base0C

c.colors.tabs.indicator.error = base08

c.colors.tabs.odd.fg = base05

c.colors.tabs.odd.bg = base01

c.colors.tabs.even.fg = base05

c.colors.tabs.even.bg = base00

c.colors.tabs.pinned.even.bg = base0C

c.colors.tabs.pinned.even.fg = base07

c.colors.tabs.pinned.odd.bg = base0B

c.colors.tabs.pinned.odd.fg = base07

c.colors.tabs.pinned.selected.even.bg = base02

c.colors.tabs.pinned.selected.even.fg = base05

c.colors.tabs.pinned.selected.odd.bg = base02

c.colors.tabs.pinned.selected.odd.fg = base05

c.colors.tabs.selected.odd.fg = base05

c.colors.tabs.selected.odd.bg = base02

c.colors.tabs.selected.even.fg = base05

c.colors.tabs.selected.even.bg = base02


config.bind("zz", "back")
config.bind("xx", "forward")
c.downloads.location.directory = "~/downloads"
c.auto_save.session = True
config.bind(',X', 'spawn -dv mpv --volume=50 {url}')
c.completion.height = "20%"
c.scrolling.bar = "never"
