
# references:
# https://gist.github.com/bbugyi200/7ca065161dc4186ff2e97021d4e9c18a
# https://gist.github.com/Ape/d0c48b3f7ec9c8efaecf48eaa1e75d0d

config.load_autoconfig()

c.url.searchengines = {"DEFAULT": "https://www.google.com/search?q={}"}
c.url.start_pages = "https://www.google.com/"


def bind(key, *commands, mode='normal'):
    config.bind(key, ' ;; '.join(commands), mode=mode)


# bind('<Ctrl-r>', 'restart')
