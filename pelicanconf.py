#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'sunjianhua'
SITENAME = u'Build the World'
SITEURL = 'http://www.linuxyu.com'

GITHUB_URL = 'https://github.com/sunjianhua1990s'
ARCHIVES_URL = 'archives.html'
ARTICLE_URL = 'pages/{date:%Y}/{date:%m}/{date:%d}/{slug}.html'
ARTICLE_SAVE_AS = 'pages/{date:%Y}/{date:%m}/{date:%d}/{slug}.html'

RELATIVE_URLS = True
DEFAULT_PAGINATION = 5

TIMEZONE = 'Asia/Shanghai'

# 默认日期是markdown文件的修改日期  
DEFAULT_DATE = 'fs'  
DEFAULT_DATE_FORMAT = '%Y-%m-%d'

DEFAULT_LANG = u'zh_CN'

THEME = 'tuxlite_tbs'

DISQUS_SITENAME = 'sunjianhua1990s'

GOOGLE_ANALYTICS = 'UA-52496177-1'

GOOGLE_CUSTOM_SEARCH_SIDEBAR = '003815691719279377429:4pqhjctvz5a'

# Feed generation is usually not desired when developing
# FEED_ALL_ATOM = None
# CATEGORY_FEED_ATOM = None
# TRANSLATION_FEED_ATOM = None

FEED_RSS = 'feeds/all.rss.xml'
CATEGORY_FEED_RSS = 'feeds/%s.rss.xml'

# Blogroll
LINKS =  (('Google', 'http://74.125.20.33/'),
          ('Python', 'http://python.org/'),
          ('Pelican', 'http://docs.getpelican.com/'),
         )

# Social widget
SOCIAL = (('Github', 'https://github.com/sunjianhua1990s'),
          (u'CSDN', 'http://blog.csdn.net/huaxi1902'),
          (u'知乎', ''),
          (u'豆瓣', ''),
         )

#设置路径
PLUGIN_PATH = 'pelican-plugins'
PLUGINS = ['summary','sitemap','neighbors']
## 配置sitemap 插件
SITEMAP = {
    "format": "xml",
    "priorities": {
        "articles": 0.7,
        "indexes": 0.5,
        "pages": 0.3,
    },
    "changefreqs": {
        "articles": "monthly",
        "indexes": "daily",
        "pages": "monthly",
    }
}


#STATIC_PATHS = [u"img"]

#使用目录名作为文章的分类名
# USE_FOLDER_AS_CATEGORY = True
#使用文件名作为文章或页面的slug（url）
# FILENAME_METADATA = '(?P<slug>.*)'
#页面的显示路径和保存路径，推荐下面的方式

# PAGE_URL = '{slug}.html'
# PAGE_SAVE_AS = PAGE_URL
# CATEGORY_URL = '{slug}/index.html'
# CATEGORY_SAVE_AS = CATEGORY_URL
# TAG_URL = 'tag/{slug}.html'
# TAG_SAVE_AS = TAG_URL
# TAGS_SAVE_AS = 'tag/index.html'

