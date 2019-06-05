#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Urban Institute Python Users Group'
SITENAME = 'Python at Urban'
SITEURL = ''
#SITESUBURL = 'Python-at-Urban/'
PATH = 'content'
TIMEZONE = 'America/New_York'
DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

MARKUP = ('md', )

PLUGIN_PATHS = ['./plugins', './plugins/pelican-plugins']
PLUGINS = [
    'ipynb.liquid',
    'liquid_tags.include_code',  # including code blocks
    'liquid_tags.literal'
]

IGNORE_FILES = ['.ipynb_checkpoints']

# THEME SETTINGS
#THEME = './theme/'