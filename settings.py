# -*- coding: UTF-8 -*-
from django.conf.urls import url


MAIN_ENTITY_LEVEL = 'municipio'

# Main entity name. Must be the same used in data/entidades.csv
MAIN_ENTITY_NAME = 'Menorca'

# Theme Budget Loader class name. Default: 'SimpleBudgetLoader'
BUDGET_LOADER = 'MenorcaBudgetLoader'

# Theme Payments Loader class name. Default: 'PaymentsLoader'
# PAYMENTS_LOADER = 'MenorcaPaymentsLoader'


# Show / hide Settings
# ----------------------

# Show Payments section in menu & home options. Default: False.
# SHOW_PAYMENTS = True

# Configure 'by area' payment breakdown. Default: ['area', 'payee', 'description']
# PAYMENTS_BREAKDOWN_BY_AREA = ['area', 'payee', 'description']

# Configure 'by payee' payment breakdown. Default: ['payee', 'area', 'description']
# PAYMENTS_BREAKDOWN_BY_PAYEE = ['payee', 'area', 'description']

# Define if payments year slider is a range (True) or a single year (False). Default: True
# PAYMENTS_YEAR_RANGE = False

# Show Tax Receipt section in menu & home options. Default: False.
# SHOW_TAX_RECEIPT = True

# Show Counties & Towns links in Policies section in menu & home options. Default: False.
# SHOW_COUNTIES_AND_TOWNS = True

# Search in entity names. Default: False.
# SEARCH_ENTITIES = True


# Budget Settings
# ----------------------

# Show an extra tab with institutional breakdown. Default: True.
# SHOW_INSTITUTIONAL_TAB  = False

# Show section pages. Still under development, see #347. Default: False.
# SHOW_SECTION_PAGES = True

# Are institutional codes consistent along the years. Default: False.
# Important: We need this to be True for the institutional treemap to work properly.
# CONSISTENT_INSTITUTIONAL_CODES = True

# Show an extra treemap in the Policy page, showing institutional breakdown. Default: False.
# Important: insitutional codes must be consistent along the years, see CONSISTENT_INSTITUTIONAL_CODES.
# SHOW_GLOBAL_INSTITUTIONAL_TREEMAP  = True

# Show an extra tab with funding breakdown (only applicable to some budgets). Default: False.
# SHOW_FUNDING_TAB = True

# Show breadcrumbs in policies. Default: False.
# SHOW_BREADCRUMBS = True

# Show an extra column with actual revenues/expenses. Default: True.
# Warning: the execution data still gets shown in the summary chart and in downloads.
# SHOW_ACTUAL = False

# Should we group elements at the economic subheading level, or list all of them,
# grouping by uid?. Default: True. (i.e. group by uid, show all elements)
# BREAKDOWN_BY_UID = False

# Include financial income/expenditures in overview and global policy breakdowns. Default: False
INCLUDE_FINANCIAL_CHAPTERS_IN_BREAKDOWNS = True

# Does the data includes a fifth functional classification level, subprogrammes?. Default: False
# USE_SUBPROGRAMMES = True


# Theme Settings
# ----------------------

# Supported languages. Default: ('es', 'Castellano')
LANGUAGES = (
  ('ca', 'Catal&agrave;'),
  ('es', 'Castellano'),
)

# Plausible data domain. Default: ''
PLAUSIBLE_DOMAIN = 'menorca.dondevanmisimpuestos.es'

# Setup Data Source Budget link
DATA_SOURCE_BUDGET = 'http://www.cime.es/Contingut.aspx?IdPub=2080'

# Setup Data Source Population link
DATA_SOURCE_POPULATION = 'http://www.ine.es/dynt3/inebase/index.htm?padre=517'

# Setup Data Source Inflation link
DATA_SOURCE_INFLATION = 'http://www.ine.es/jaxiT3/Tabla.htm?t=22350&L=0'

# Setup Main Entity Web Url
MAIN_ENTITY_WEB_URL = 'http://www.cime.es/'

# Setup Main Entity Legal Url (if empty we hide the link)
MAIN_ENTITY_LEGAL_URL = 'http://www.cime.es/Contingut.aspx?IdPub=1672'

# Setup Main Entity Legal Url (if empty we hide the link)
MAIN_ENTITY_PRIVACY_URL = ''

# External URL for Cookies Policy (if empty we use out template page/cookies.html)
COOKIES_URL = ''

# We can define additional URLs applicable only to the theme. These will get added
# to the project URL patterns list.
EXTRA_URLS = (
    url(r'^visita-guiada$', 'guidedvisit', name='guidedvisit'),
)


# Welcome Settings
# ----------------------

# Programmes to feature as example in home page.
FEATURED_PROGRAMMES = ['23121', '43200', '44100', '17200']

# Number of programmes to feature in home page. Default: 3
# NUMBER_OF_FEATURED_PROGRAMMES = 3


# Overview Settings
# ----------------------

# Use new Sankey visualization or the old one. Default: False
OVERVIEW_USE_NEW_VIS = True

OVERVIEW_INCOME_NODES = [
                          {
                            'nodes': ['45', '75'],
                            'label.es': 'De comunidades autónomas',
                            'label.ca': 'De comunitats autònomes'
                          },
                          {
                            'nodes': ['42', '72'],
                            'label.es': 'De la Administración del Estado',
                            'label.ca': "De l'Administració de l'Estat"
                          },
                          '31', '21', '10'
                        ]

OVERVIEW_EXPENSE_NODES = ['23', '91', '45', '92', '43', '01', '41', '33', '13', '44']

# How much padding between Sankey nodes. Default: 2 (Optional)
# OVERVIEW_NODE_PADDING = 2

# Overview node minimum height to show labels. Default: 16 (Optional)
# OVERVIEW_LABELS_MIN_SIZE = 16

# Overview node labels minimum font size. Default: 11 (Optional)
# OVERVIEW_LABELS_FONT_SIZE_MIN = 11

# Overview node labels maximum font size. Default: 11 (Optional)
# OVERVIEW_LABELS_FONT_SIZE_MAX = 38

# Nodes ordered by amount by default. If set to True keeps the order defined in nodes array. Default: False (Optional)
# OVERVIEW_FORCE_ORDER = False


# Show Subtotals panel in Overview. Default: False
# SHOW_OVERVIEW_SUBTOTALS = True

# Calculate budget indicators (True), or show/hide the ones hardcoded in HTML (False). Default: True.
# CALCULATE_BUDGET_INDICATORS = False


# Treemap Settings
# ----------------------

# Treemaps minimum height or width to show labels. Default: 30 (Optional)
# TREEMAP_LABELS_MIN_SIZE = 30

# Treemap minimum font size. Default: 11 (Optional)
# TREEMAP_LABELS_FONT_SIZE_MIN = 11

# Treemap use max value between tabs to calculate size. Default: True
# TREEMAP_GLOBAL_MAX_VALUE = False

# Allow overriding of default treemap color scheme
# COLOR_SCALE = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#e7969c', '#bcbd22', '#17becf']

# How many levels to show in the global institutional treemap? Default: 1.
# INSTITUTIONAL_MAX_LEVELS = 2
