

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # 'bootstrap',
    # Uncomment the next line to enable the admin:
    'djangocms_admin_style',
    'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
    'djangocms_text_ckeditor',

    'cms',
    'mptt',
    'menus',
    'south',
    'sekizai',

    'easy_thumbnails',
    'filer',
    'cmsplugin_filer_file',
    'cmsplugin_filer_folder',
    'cmsplugin_filer_image',
    'django.contrib.markup',
    'cmsplugin_markdown',
    # 'cms.plugins.text',

    'm_cmsplugin_labs',
    'm_cmsplugin_toc',
    'cmsplugin_syntax_highlight',
    'menu_icons',
    'excursions',
    'image_gallery',

    'utils'
)

# THUMBNAIL_DEBUG = True
