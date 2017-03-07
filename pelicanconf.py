#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Reno'
SITENAME = u'reno777'
SITEURL = 'www.reno777.tech'
SITESUBTITLE = 'The most secure box is a custom box'

PATH = 'content'

TIMEZONE = 'EST'

DEFAULT_LANG = u'en'

THEME = '/home/admin/html/output/theme/elegant'

DISPlAY_PAGE_ON_MENU = 'true'
# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
#LINKS = (('Pelican', 'http://getpelican.com/'),
#         ('Python.org', 'http://python.org/'),
#         ('Jinja2', 'http://jinja.pocoo.org/'),
#         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (
('GitHub', 'https://github.com/reno777/'),
('Twitter', 'https://twitter.com/sethrasmussen13'),
('Email',  'mailto:reno.triple7s@gmail.com'),
)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

AUTHORS_SAVE_AS = ''

PLUGIN_PATHS =  ['/home/admin/html/output/pelican-plugins']
PLUGINS = ['tipue_search'] 

STATIS_PATHS = [
	'extra/favicon.ico',
]

EXTRA_PATH_METADATA = {
	'extra/favicon.ico': {'path': 'favicon.ico'},
}

#TEMPLATE_PAGES = {
DIRECT_TEMPLATES = (('categories', 'archives', 'search'))
