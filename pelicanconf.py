#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Kenneth Feng'
SITENAME = u'Log@tomic'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS = (
    ('Pelican', 'http://getpelican.com/'),
    ('Python.org', 'http://python.org/'),
    ('Jinja2', 'http://jinja.pocoo.org/'),
    ('You can modify those links in your config file', '#'),
)

# Social widget
SOCIAL = (
    ('Github', 'https://github.com/kennethzfeng'),
    ('Twitter', 'http://twitter.com/kennethzfeng'),
)

DEFAULT_PAGINATION = 10

# Theme
THEME = 'my_themes/kfeng-blog'
THEME_STATIC_PATHS = ['static']

DISPLAY_PAGES_ON_MENU = True
# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# CNAME
STATIC_PATHS = ['extra/CNAME', 'pdfs']
EXTRA_PATH_METADATA = {
    'extra/CNAME': {'path': 'CNAME'}
}
