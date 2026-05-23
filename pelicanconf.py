import os
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()  # This loads variables from .env into os.environ

CURRENT_YEAR = datetime.now().year

AUTHOR = os.getenv('AUTHOR')
SITENAME = os.getenv('SITENAME')

PATH = 'content'
OUTPUT_PATH = 'docs'

TIMEZONE = os.getenv('TIMEZONE')

DEFAULT_LANG = os.getenv('DEFAULT_LANG')

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
AUTHOR_FEED_ATOM = None

# Tell Pelican to generate both 'index' and 'blog' as direct templates
DIRECT_TEMPLATES = ['blog']

# Map your blog template
BLOG_SAVE_AS = 'blog.html'
BLOG_URL = 'blog.html'

# Completely disable the default index generation
INDEX_SAVE_AS = ''
INDEX_URL = ''

# Move pagination from the default index to your new blog template
# The 'None' value tells it to fall back to your DEFAULT_PAGINATION number
PAGINATED_TEMPLATES = {'blog': None}

# ARTICLE_URL = '{date:%Y}/{slug}/'
# ARTICLE_SAVE_AS = '{date:%Y}/{slug}/index.html'
DEFAULT_CATEGORY = 'other'
EXTRA_PATH_METADATA = {
    'images/favicons/android-chrome-192x192.png': {'path': 'android-chrome-192x192.png'},
    'images/favicons/android-chrome-512x512.png': {'path': 'android-chrome-512x512.png'},
    'images/favicons/apple-touch-icon.png': {'path': 'apple-touch-icon.png'},
    'images/favicons/favicon.ico': {'path': 'favicon.ico'},
    'images/favicons/manifest.json': {'path': 'manifest.json'},
}
FONT_AWESOME = os.getenv('FONT_AWESOME')
HOSTING_PROVIDER = 'Cloudflare'
HOSTING_PROVIDER_URL = 'https://www.cloudflare.com/'
LICENSE = 'Attribution-NonCommercial-NoDerivatives 4.0 International'
LICENSE_URL = 'https://creativecommons.org/licenses/by-nc-nd/4.0/'
OVERRIDE_CSS = 'styles.css'
PLUGIN_PATHS = ['plugins']
PLUGINS = ['asciidoc_reader', 'sitemap']
STATIC_PATHS = ['css', 'images', 'robots.txt', 'wrangler.jsonc']
THEME = 'themes/GhostLight-Research-Theme'
TWITTER_USERNAME = os.getenv('TWITTER_USERNAME')
USE_FOLDER_AS_CATEGORY = False

# for sitemap plugin
SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
    },
    'changefreqs': {
        'articles': 'daily',
        'indexes': 'daily',
        'pages': 'never',
    }
}
