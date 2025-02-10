# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))

# import sphinx_rtd_theme

# -- Project information -----------------------------------------------------

project = 'Engine Driver Home'
copyright = 'M Steve Todd'
author = 'M Steve Todd, Peter Akers, Robert Posener'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
   # 'sphinx.ext.intersphinx',
    'sphinx.ext.autosectionlabel',
    'sphinx.ext.todo',
   # 'sphinx.ext.coverage',
   # 'sphinx.ext.mathjax',
   # 'sphinx.ext.ifconfig',
   # 'sphinx.ext.viewcode',
   # 'sphinx.ext.graphviz',
   # 'sphinx.ext.inheritance_diagram',
    'sphinxcontrib.spelling',
    'sphinx_sitemap', 
    'sphinx_rtd_dark_mode',
    'sphinx_reredirects'
]

# Make sure the target is unique
autosectionlabel_prefix_document = True

spelling_lang='en_UK'
tokenizer_lang='en_US'
spelling_word_list_filename = ['spelling_wordlist.txt']

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = [
    '_build', 'Thumbs.db', '.DS_Store',
]

# Set the default for literal blocks and code-block
highlight_language = 'none'

# Automatically number figure captions
numfig = True

numfig_format = {'figure': 'Figure %s'}

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_rtd_theme"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

html_logo = "./_static/images/logo.png"

html_favicon = "./_static/images/favicon.ico"

html_baseurl = "https://EngineDriver.mstevetodd.com/"

html_theme_options = {
    'style_nav_header_background': 'white',
    'logo_only': True,
    # Toc options
    'includehidden': True,
#    'titles_only': True,
    'collapse_navigation': False,
    'navigation_depth': -1 
} 

html_context = {
    'display_github': True,
    'github_user': 'mstevetodd',
    'github_repo': 'EngineDriver_Home',
    'github_version': 'main/docs/', 
} 

#leave this off to have todos invisible, set to true to render them and make the easy to see
#A list of all the todos in the document can be shown in the about page
todo_include_todos = True

#html_additional_pages = {
#    'exwebthrottle': 'exwebthrottle/index.html',
#}

html_css_files = [
    'css/engine_driver_home_theme.css',
] 

html_js_files = [
    'js/platform.js',
    'js/extra.js',
#    'js/commandController.js',
#    'js/fnMaster.js',
#    'js/jquery-3.2.1.min.js',
#    'js/jquery-ui.min.js',
#    'js/roundslider.min.js',
#    'js/storageController.js'
]

# Configure sphinx-notfound-page
notfound_context = {
    "title": "Page Not Found",
    "body": """
<h1>Page Not Found</h1>

<p>Sorry, we couldn't find that page.</p>

<p>Try using the search box or go to the <a href="/index.html">homepage</a>.</p>
""",
}
notfound_urls_prefix = "/mstevetodd.github.io/"

redirects = {

    "connect": "./operation/operation.html#connecting",

    "en/about/index.html": "../../about/index.html",
    "en/about/privacy-policy.html": "../../about/privacy-policy.html",
    "en/changes/index.html": "../../changes/index.html",
    "en/configuration/configuration_withrottle.html": "../../configuration/configuration_withrottle.html",
    "en/configuration/configuration.html": "../../configuration/configuration.html",

    "en/configuration/conserving_power.html": "../../configuration/conserving_power.html",
    "en/configuration/functions.html": "../../configuration/functions.html",
    "en/configuration/gamepads.html": "../../configuration/gamepads.html",
    "en/configuration/index.html": "../../configuration/index.html",
    "en/configuration/ipls.html": "../../configuration/ipls.html",
    "en/configuration/loco_icons.html": "../../configuration/loco_icons.html",
    "en/configuration/new_device.html": "../../configuration/new_device.html",
    "en/configuration/preferences_index.html": "../../configuration/preferences_index.html",
    "en/configuration/preferences.html": "../../configuration/preferences.html",
    "en/configuration/setup_wizard.html": "../../configuration/setup_wizard.html",
    "en/contact/index.html": "../../contact/index.html",
    "en/contributing/index.html": "../../contributing/index.html",
    "en/downloads/index.html": "../../downloads/index.html",
    "en/genindex.html": "../../genindex.html",
    "en/glossary/index.html": "../../glossary/index.html",
    "en/include.html": "../../index.html",
    "en/index.html": "../../index.html",
    "en/operation/advanced.html": "../../operation/advanced.html",
    "en/operation/consist-follow-functions.html": "../../operation/consist-follow-functions.html",
    "en/operation/dcc-ex-native-protocol.html": "../../operation/dcc-ex-native-protocol.html",
    "en/operation/esu_mcii.html": "../../operation/esu_mcii.html",
    "en/operation/faq.html": "../../operation/faq.html",
    "en/operation/gamepads": "../../operation/gamepads.html",
    "en/operation/index.html": "../../operation/index.html",
    "en/operation/interface.html": "../../operation/interface.html",
    "en/operation/operation.html": "../../operation/operation.html",
    "en/operation/semi-realistic-throttle.html": "../../operation/semi-realistic-throttle.html",
    "en/operation/wifi_issues.html": "../../operation/wifi_issues.html",
    "en/prerequisites/index.html": "../../prerequisites/index.html",
    "en/search.html": "../../index.html",
    "en/videos/index.html": "../../videos/index.html",

    "import-preferences": "./configuration/preferences.html#import-export-reset-log-preferences",


    "index.php": "./index.html",
    "index.php/": "./index.html",
    "index.php/configuration": "../configuration/index.html",
    "index.php/connect": "../operation/operation.html#connecting",
    "index.php/contact": "../about/index.html",
    "index.php/downloads": "../downloads/index.html",
    "index.php/import-preferences": "../configuration/preferences.html#import-export-reset-log-preferences",
    "index.php/operation": "../operation/index.html",
    "index.php/screenshots": "../glossary/index.html#screenshots",
    "index.php/simple-throttle-4": "../configuration/preferences.html#throttle-screen-layout",
    "index.php/simple-throttle-6": "../configuration/preferences.html#throttle-screen-layout",
    "index.php/throttle-big-buttons": "../configuration/preferences.html#throttle-screen-layout",
    "index.php/throttle-type-big-buttons-left": "../configuration/preferences.html#throttle-screen-layout",
    "index.php/throttle-vertical-right": "../configuration/preferences.html#throttle-screen-layout",
    "index.php/videos": "../videos/index.html",

    "operation/import-preferences": "../configuration/preferences.html#import-export-reset-log-preferences",
    "operation/emergencystopbutton": "../operation/interface.html#emergency-stop-button",
    "operation/RecentTurnout/Pointlist": "../../operation/interface.html#turnouts-points-screen",

    "privacy-policy": "./about/privacy-policy.html",

    "screenshots": "./glossary/index.html#screenshots",
    "simple-throttle-6": "./configuration/preferences.html#throttle-screen-layout",
    "sites/enginedriver.mstevetodd.com/files/": "../../downloads/index.html",
    "sites/enginedriver.mstevetodd.com/files/EngineDriver_App-MRC_Wi-Fi_Module_Settings.pdf": "../../../_static/files/EngineDriver_App-MRC_Wi-Fi_Module_Settings.pdf",
    "supported-withrottle-servers": "./about/index.html",

    "tablet-web-conductor": "./index.html",
    "throttle-big-buttons": "./configuration/preferences.html#throttle-screen-layout",
    "throttle-default": "./configuration/preferences.html#throttle-screen-layout",
    "throttle-no-slider": "./configuration/preferences.html#throttle-screen-layout",
    "turnouts": "./operation/operation.html#turnouts-points",

    "wifi": "./operation/wifi_issues.html"
}
