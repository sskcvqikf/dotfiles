# Uncomment this to still load settings configured via autoconfig.yml
# config.load_autoconfig()
import os
HOMe = os.environ['HOME']

# Enable JavaScript.
# Type: Bool
config.set('content.javascript.enabled', True, 'file://*')

# Enable JavaScript.
# Type: Bool
config.set('content.javascript.enabled', True, 'chrome://*/*')

# Enable JavaScript.
# Type: Bool
config.set('content.javascript.enabled', True, 'qute://*/*')
config.set('tabs.padding', { 'top': 15, 'bottom': 15, 'left': 10, 'right': 10 })
config.set('zoom.default', '150%')
config.set('url.searchengines', {"DEFAULT": "https://searx.info/?q={}"})
config.set('url.start_pages', f'{HOME}.config/browserhome/index.html')
config.set('url.default_page', f'{HOME}.config/browserhome/index.html')

# Default monospace fonts. Whenever "monospace" is used in a font
# setting, it's replaced with the fonts listed here.
# Type: Font

c.zoom.default = '100%'

# Font used in the completion widget.
# Type: Font
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

# Base16 qutebrowser template by theova
# iA theme by @dab
# set qutebrowser colors

# Text color of the completion widget. May be a single color to use for
# all columns or a list of three colors, one for each column.
c.colors.completion.fg = "#455e7e"

# Background color of the completion widget for odd rows.
c.colors.completion.odd.bg = "#eaeaea"

# Background color of the completion widget for even rows.
c.colors.completion.even.bg = "#ffdee2"

# Foreground color of completion widget category headers.
c.colors.completion.category.fg = "#eaeaea"

# Background color of the completion widget category headers.
c.colors.completion.category.bg = "#ff93a0"

# Top border color of the completion widget category headers.
c.colors.completion.category.border.top = "#ff93a0"

# Bottom border color of the completion widget category headers.
c.colors.completion.category.border.bottom = "#ff93a0"

# Foreground color of the selected completion item.
c.colors.completion.item.selected.fg = "#ff93a0"

# Background color of the selected completion item.
c.colors.completion.item.selected.bg = "#eaeaea"

# Top border color of the completion widget category headers.
c.colors.completion.item.selected.border.top = "#eaeaea"

# Bottom border color of the selected completion item.
c.colors.completion.item.selected.border.bottom = "#eaeaea"

# Foreground color of the matched text in the completion.
c.colors.completion.match.fg = "#344d6c"

# Color of the scrollbar handle in the completion view.
c.colors.completion.scrollbar.fg = "#455e7e"

# Color of the scrollbar in the completion view.
c.colors.completion.scrollbar.bg = "#ff93a0"

# Background color for the download bar.
c.colors.downloads.bar.bg = "#ff93a0"

# Color gradient start for download text.
c.colors.downloads.start.fg = "#ff93a0"

# Color gradient start for download backgrounds.
c.colors.downloads.start.bg = "#ea808e"

# Color gradient end for download text.
c.colors.downloads.stop.fg = "#ff93a0"

# Color gradient stop for download backgrounds.
c.colors.downloads.stop.bg = "#d6d6d6"

# Foreground color for downloads with errors.
c.colors.downloads.error.fg = "#eaeaea"

# Font color for hints.
c.colors.hints.fg = "#ff93a0"

# Background color for hints. Note that you can use a `rgba(...)` value
# for transparency.
c.colors.hints.bg = "#eaeaea"

# Font color for the matched part of hints.
c.colors.hints.match.fg = "#455e7e"

# Text color for the keyhint widget.
c.colors.keyhint.fg = "#455e7e"

# Highlight color for keys to complete the current keychain.
c.colors.keyhint.suffix.fg = "#455e7e"

# Background color of the keyhint widget.
c.colors.keyhint.bg = "#ff93a0"

# Foreground color of an error message.
c.colors.messages.error.fg = "#ff93a0"

# Background color of an error message.
c.colors.messages.error.bg = "#eaeaea"

# Border color of an error message.
c.colors.messages.error.border = "#eaeaea"

# Foreground color of a warning message.
c.colors.messages.warning.fg = "#eaeaea"

# Background color of a warning message.
c.colors.messages.warning.bg = "#ff5a5d"

# Border color of a warning message.
c.colors.messages.warning.border = "#ff5a5d"

# Foreground color of an info message.
c.colors.messages.info.fg = "#455e7e"

# Background color of an info message.
c.colors.messages.info.bg = "#ff93a0"

# Border color of an info message.
c.colors.messages.info.border = "#ff93a0"

# Foreground color for prompts.
c.colors.prompts.fg = "#455e7e"

# Border used around UI elements in prompts.
c.colors.prompts.border = "#ff93a0"

# Background color for prompts.
c.colors.prompts.bg = "#ff93a0"

# Background color for the selected item in filename prompts.
c.colors.prompts.selected.bg = "#eaeaea"

# Foreground color of the statusbar.
c.colors.statusbar.normal.fg = "#344d6c"

# Background color of the statusbar.
c.colors.statusbar.normal.bg = "#ff93a0"

# Foreground color of the statusbar in insert mode.
c.colors.statusbar.insert.fg = "#ff93a0"

# Background color of the statusbar in insert mode.
c.colors.statusbar.insert.bg = "#ea808e"

# Foreground color of the statusbar in passthrough mode.
c.colors.statusbar.passthrough.fg = "#ff93a0"

# Background color of the statusbar in passthrough mode.
c.colors.statusbar.passthrough.bg = "#d6d6d6"

# Foreground color of the statusbar in private browsing mode.
c.colors.statusbar.private.fg = "#ff93a0"

# Background color of the statusbar in private browsing mode.
c.colors.statusbar.private.bg = "#8c449b"

# Foreground color of the statusbar in command mode.
c.colors.statusbar.command.fg = "#455e7e"

# Background color of the statusbar in command mode.
c.colors.statusbar.command.bg = "#ff93a0"

# Foreground color of the statusbar in private browsing + command mode.
c.colors.statusbar.command.private.fg = "#455e7e"

# Background color of the statusbar in private browsing + command mode.
c.colors.statusbar.command.private.bg = "#ff93a0"

# Foreground color of the statusbar in caret mode.
c.colors.statusbar.caret.fg = "#ff93a0"

# Background color of the statusbar in caret mode.
c.colors.statusbar.caret.bg = "#ff5a5d"

# Foreground color of the statusbar in caret mode with a selection.
c.colors.statusbar.caret.selection.fg = "#ff93a0"

# Background color of the statusbar in caret mode with a selection.
c.colors.statusbar.caret.selection.bg = "#ea808e"

# Background color of the progress bar.
c.colors.statusbar.progress.bg = "#ea808e"

# Default foreground color of the URL in the statusbar.
c.colors.statusbar.url.fg = "#455e7e"

# Foreground color of the URL in the statusbar on error.
c.colors.statusbar.url.error.fg = "#eaeaea"

# Foreground color of the URL in the statusbar for hovered links.
c.colors.statusbar.url.hover.fg = "#455e7e"

# Foreground color of the URL in the statusbar on successful load
# (http).
c.colors.statusbar.url.success.http.fg = "#d6d6d6"

# Foreground color of the URL in the statusbar on successful load
# (https).
c.colors.statusbar.url.success.https.fg = "#344d6c"

# Foreground color of the URL in the statusbar when there's a warning.
c.colors.statusbar.url.warn.fg = "#ff5a5d"

# Background color of the tab bar.
c.colors.tabs.bar.bg = "#ff93a0"

# Color gradient start for the tab indicator.
c.colors.tabs.indicator.start = "#ea808e"

# Color gradient end for the tab indicator.
c.colors.tabs.indicator.stop = "#d6d6d6"

# Color for the tab indicator on errors.
c.colors.tabs.indicator.error = "#eaeaea"

# Foreground color of unselected odd tabs.
c.colors.tabs.odd.fg = "#455e7e"

# Background color of unselected odd tabs.
c.colors.tabs.odd.bg = "#eaeaea"

# Foreground color of unselected even tabs.
c.colors.tabs.even.fg = "#455e7e"

# Background color of unselected even tabs.
c.colors.tabs.even.bg = "#ffe4e4"

# Foreground color of selected odd tabs.
c.colors.tabs.selected.odd.fg = "#455e7e"

# Background color of selected odd tabs.
c.colors.tabs.selected.odd.bg = "#ff93a0"

# Foreground color of selected even tabs.
c.colors.tabs.selected.even.fg = "#455e7e"

# Background color of selected even tabs.
c.colors.tabs.selected.even.bg = "#ff93a0"

# Background color for webpages if unset (or empty to use the theme's
# color).
# c.colors.webpage.bg = "#ff93a0"<Paste>
config.bind("zz", "back")
config.bind("xx", "forward")
c.downloads.location.directory = "~/downloads"
c.auto_save.session = True
