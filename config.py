
# references:
# https://gist.github.com/bbugyi200/7ca065161dc4186ff2e97021d4e9c18a
# https://gist.github.com/Ape/d0c48b3f7ec9c8efaecf48eaa1e75d0d

config.load_autoconfig()

c.url.searchengines = {"DEFAULT": "https://www.google.com/search?q={}",
                       "gg": "https://www.google.com/search?q={}"}
c.url.start_pages = ["https://www.google.com/"]
c.url.default_page = "https://www.google.com/"

# fix javascript button click problem
# https://github.com/qutebrowser/qutebrowser/issues/4487#issuecomment-503755580
c.content.javascript.can_access_clipboard = True

# fix google sign-in problem
# https://github.com/qutebrowser/qutebrowser/issues/5182#issuecomment-763300346
if hasattr(c.content.site_specific_quirks, "enabled"):
    c.content.site_specific_quirks.enabled = True
else:
    c.content.site_specific_quirks = True

# c.tabs.last_close = "close"

config.unbind("<ctrl+q>")

# Escape setting
# https://gist.github.com/jumper047/ee821f789cd336b1105309f3ebf44f70
ESC_BIND = 'clear-keychain ;; search ;; fullscreen --leave'

config.bind("<ctrl+g>", ESC_BIND, mode='normal')
config.bind("<ctrl+g>", 'mode-leave', mode='command')
config.bind("<ctrl+g>", 'mode-leave', mode='hint')
config.bind("<ctrl+g>", 'mode-leave', mode='caret')
