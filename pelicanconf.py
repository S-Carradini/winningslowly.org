#!/usr/bin/env python
# -*- coding: utf-8 -*- #

"""Build this thing!"""

from __future__ import unicode_literals

# Site configuration
AUTHOR = 'Chris Krycho and Stephen Carradini'
SITENAME = 'Winning Slowly'
SITE_DESCRIPTION = 'Taking the long view on technology, religion, ethics, and art.'
SITEURL = ''
LOGO = 'images/logotype.png'

TIMEZONE = 'America/Denver'

DEFAULT_LANG = 'en'

THEME = "2018_theme"

# Show configuration
SEASONS = {
    '6': {
        'prefix': 'Season 6',
        'title': 'Rejecting the Inevitable Future',
        'slug': 'season-6',
        'number': '6',
    },
    '5': {
        'prefix': 'Season 5',
        'title': 'Structure and Agency',
        'slug': 'season-5',
        'number': '5',
    },
    '4': {
        'prefix': 'Season 4',
        'title': 'Globalization',
        'slug': 'season-4',
        'number': '4',
    },
    '3': {
        'prefix': None,
        'title': 'Season 3',
        'slug': 'season-3',
        'number': '3',
    },
    '2': {
        'prefix': None,
        'title': 'Season 2',
        'slug': 'season-2',
        'number': '2',
    },
    '1': {
        'prefix': None,
        'title': 'Season 1',
        'slug': 'season-1',
        'number': '1',
    },
    '0': {
        'prefix': 'Season 0',
        'title': 'This Is In Beta!',
        'slug': 'season-0',
        'number': '0',
    },
    'Standalone Episodes': {
        'prefix': None,
        'title': 'Standalone Episodes',
        'slug': 'standalone-episodes',
        'number': None,
    },
    'Bonus': {
        'prefix': None,
        'title': 'Bonus',
        'slug': 'bonus-episodes',
        'number': None,
    }
}

CURRENT_SEASON = SEASONS['6']

# Feed generation is usually not desired when developing
FEED_DOMAIN = SITEURL
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
FEED_ALL_RSS = None
CATEGORY_FEED_RSS = None
TRANSLATION_FEED_RSS = None
AUTHOR_FEED_RSS = None
AUTHOR_FEED_ATOM = None
CUSTOM_FEED_URL = 'feed.xml'

# Social widget
IDENTITY = {'Site': {'RSS': FEED_DOMAIN + '/' + CUSTOM_FEED_URL,
                     'iTunes': 'https://itunes.apple.com/us/podcast/winning-slowly/id807603957?mt=2',
                     'Overcast': 'https://overcast.fm/itunes807603957/winning-slowly',
                     'Pocket Casts': 'http://pca.st/Pl01',
                     'Email': 'mailto:hello@winningslowly.org',
                     'Patreon': 'https://www.patreon.com/winningslowly',
                     'Square': 'https://cash.me/$winningslowly',
                     'Twitter': 'https://twitter.com/winningslowly'},
            'Chris': {'GitHub': 'https://github.com/chriskrycho',
                      'Twitter': 'https://twitter.com/chriskrycho',
                      'Homepage': 'http://chriskrycho.com'},
            'Stephen': {'Twitter': 'https://twitter.com/scarradini',
                        'Homepage': 'http://stephencarradini.com'}}

CDN = 'cdn.winningslowly.org'
MP3 = '.mp3'
PODTRAC_REDIRECT = 'http://www.podtrac.com/pts/redirect'
PODTRAC_MP3 = PODTRAC_REDIRECT + MP3

DEFAULT_PAGINATION = False

# URLs
SLUGIFY_SOURCE = 'basename'
ARTICLE_URL = '{category}.{number}/'
ARTICLE_SAVE_AS = '{category}.{number}/index.html'
PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = '{slug}.html'
CATEGORY_URL = 'season-{slug}.html'
CATEGORY_SAVE_AS = 'season-{slug}.html'

# Category settings
USE_FOLDER_AS_CATEGORY = False  # note: this is the default
DEFAULT_CATEGORY = 'standalone-episodes'
DIRECT_TEMPLATES = ['index']

# Disable unused elements
AUTHOR_SAVE_AS = ''
AUTHORS_SAVE_AS = ''
TAGS_SAVE_AS = ''

# Output
OUTPUT_SOURCES = False
DEFAULT_DATE_FORMAT = "%B %d, %Y"

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

# Path configuration
STATIC_PATHS = ['images', '2014', '2015', 'extra']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},
                       'extra/feed.xml': {'path': CUSTOM_FEED_URL},
                       'extra/test_feed.xml': {'path': 'test_feed.xml'},
                       'extra/Winning-Slowly_podcast.png': {'path':
                                                            'podcast.png'},
                       'extra/humans.txt': {'path': 'humans.txt'}}

ARTICLE_EXCLUDES = ['2014', '2015']
PAGE_EXCLUDES = ['2014', '2015']

# Static configuration
THEME_STATIC_DIR = ''
CSS_FILE = 'style.min.css'
THEME_STATIC_PATHS = ['static', 'static/images']

READERS = {'html': None}

PLUGIN_PATHS = ['../../pelican-plugins']
PLUGINS = ['pandoc_reader']
PANDOC_EXTENSIONS = ['-citations']

# Caching
CACHE_CONTENT = True
LOAD_CONTENT_CACHE = True
CHECK_MODIFIED_METHOD = 'md5'
CONTENT_CACHING_LAYER = 'reader'
