
# references:
# https://gist.github.com/bbugyi200/7ca065161dc4186ff2e97021d4e9c18a
# https://gist.github.com/Ape/d0c48b3f7ec9c8efaecf48eaa1e75d0d

config.load_autoconfig()

c.url.searchengines = {"DEFAULT": "https://www.google.com/search?q={}",
                       "gg": "https://www.google.com/search?q={}",
                       "nd": "https://en.dict.naver.com/#/search?query={}",
                       "gk": "https://translate.google.co.kr/?hl=ko&sl=auto&tl=ko&text={}&op=translate",
                       "ge": "https://translate.google.co.kr/?hl=ko&sl=auto&tl=en&text={}&op=translate"}
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

# unbind closing shortcut
config.unbind("<ctrl+q>")

# tab move binding
config.bind("gj", 'tab-move +', mode='normal')
config.bind("gk", 'tab-move -', mode='normal')

# Escape setting
# https://gist.github.com/jumper047/ee821f789cd336b1105309f3ebf44f70
ESC_BIND = 'clear-keychain ;; search ;; fullscreen --leave'

config.bind("<ctrl+g>", ESC_BIND, mode='normal')
config.bind("<ctrl+g>", 'mode-leave', mode='insert')
config.bind("<ctrl+g>", 'mode-leave', mode='command')
config.bind("<ctrl+g>", 'mode-leave', mode='hint')
config.bind("<ctrl+g>", 'mode-leave', mode='caret')
config.bind("<ctrl+g>", 'mode-leave', mode='prompt')

# emacs binding for insert mode
# https://gist.github.com/jumper047/ee821f789cd336b1105309f3ebf44f70
c.bindings.commands['insert'].update({
    # editing
    '<ctrl-f>': 'fake-key <Right>',
    '<ctrl-b>': 'fake-key <Left>',
    '<ctrl-a>': 'fake-key <Home>',
    '<ctrl-e>': 'fake-key <End>',
    '<ctrl-n>': 'fake-key <Down>',
    '<ctrl-p>': 'fake-key <Up>',
    '<alt-f>': 'fake-key <Ctrl-Right>',
    '<alt-b>': 'fake-key <Ctrl-Left>',
    '<ctrl-d>': 'fake-key <Delete>',
    '<alt-d>': 'fake-key <Ctrl-Delete>',
    '<alt-backspace>': 'fake-key <Ctrl-Backspace>',
    '<ctrl-w>': 'fake-key <Ctrl-x>',
    '<ctrl-y>': 'insert-text {primary}',
    '<ctrl-g>': 'mode-leave',

    '<ctrl-shift-f>': 'fake-key <Shift-Right>',
    '<ctrl-shift-b>': 'fake-key <Shift-Left>',
    '<alt-shift-f>': 'fake-key <Ctrl-Shift-Right>',
    '<alt-shift-b>': 'fake-key <Ctrl-Shift-Left>',

    '<ctrl-k>': "fake-key '<Ctrl-Shift-End>' ;; fake-key '<Ctrl-x>'",
    '<ctrl-/>': 'fake-key <Ctrl-z>',
    '<ctrl-r>': 'fake-key <Ctrl-y>'
})

# emacs binding for normal mode
c.bindings.commands['normal'].update({
    '<ctrl-n>': 'fake-key <Down>',
    '<ctrl-p>': 'fake-key <Up>',

    'n': 'search-next',
    'p': 'search-prev',

    'W': 'open -w',  # open new window

    'ee': 'open -- {clipboard}',
    'eE': 'open -- {primary}',
    'Ee': 'open -t -- {clipboard}',
    'EE': 'open -t -- {primary}',
})
