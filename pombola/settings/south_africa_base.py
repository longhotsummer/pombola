from .apps import *  # noqa

COUNTRY_APP = 'south_africa'

OPTIONAL_APPS = APPS_REQUIRED_BY_SPEECHES + (
    'speeches',
    'za_hansard',
    'pombola.interests_register',
    'pombola.spinner',
)

SPEECH_SUMMARY_LENGTH = 30

BLOG_RSS_FEED = ''

BREADCRUMB_URL_NAME_MAPPINGS = {
    'info': ['Information', '/info/'],
    'organisation': ['People', '/organisation/all/'],
    'person': ['Politicians', '/person/all/'],
    'place': ['Places', '/place/all/'],
    'search': ['Search', '/search/'],
    'mp-corner': ['MP Corner', '/blog/category/mp-corner'],
    'newsletter': ['MONITOR Newsletter', '/info/newsletter'],
}

TWITTER_USERNAME = 'PeoplesAssem_SA'
TWITTER_WIDGET_ID = '431408035739607040'

MAP_BOUNDING_BOX_NORTH = -22.06
MAP_BOUNDING_BOX_EAST = 32.95
MAP_BOUNDING_BOX_SOUTH = -35.00
MAP_BOUNDING_BOX_WEST = 16.30

MAPIT_COUNTRY = 'ZA'

COUNTRY_CSS = {
    'south-africa': {
        'source_filenames': (
            'sass/south-africa.scss',
        ),
        'output_filename': 'css/south-africa.css'
    },
    'datatables': {
        'source_filenames': (
            'css/libs/datatables-1.10.10.css',
        ),
        'output_filename': 'css/datatables.css'
    }
}

COUNTRY_JS = {
    'tabs': {
        'source_filenames': (
            'js/tabs.js',
        ),
        'output_filename': 'js/tabs.js',
        'template_name': 'pipeline/js-array.html',
    },
    'za-map-drilldown': {
        'source_filenames': (
            'js/za-map-drilldown.js',
        ),
        'output_filename': 'js/za-map-drilldown.js',
        'template_name': 'pipeline/js-array.html',
    },
    'za-map-drilldown': {
        'source_filenames': (
            'js/election_countdown.js',
        ),
        'output_filename': 'js/election_countdown.js',
        'template_name': 'pipeline/js-array.html',
    },
    'advanced-search': {
        'source_filenames': (
            'js/advanced-search.js',
        ),
        'output_filename': 'js/advanced-search.js',
        'template_name': 'pipeline/js-array.html',
    },
    'interests-filter': {
        'source_filenames' : (
            'js/interests-filter.js',
        ),
        'output_filename': 'js/interests-filter.js',
        'template_name': 'pipeline/js-array.html',
    },
    'attendance-table': {
        'source_filenames': (
            'js/libs/datatables-1.10.10.js',
            'js/attendance-table.js',
        ),
        'output_filename': 'js/attendance-table.js',
        'template_name': 'pipeline/js-array.html',
    }
}

INFO_PAGES_ALLOW_RAW_HTML = True

PAGINATION_DEFAULT_WINDOW = 3

PG_DUMP_EXTRA_TABLES_TO_IGNORE = []
PG_DUMP_EXTRA_EXPECTED_TABLES = [
    'interests_register_category',
    'interests_register_entry',
    'interests_register_entrylineitem',
    'interests_register_release',
    'pombola_sayit_pombolasayitjoin',
    'speeches_recording',
    'speeches_recordingtimestamp',
    'speeches_section',
    'speeches_slug',
    'speeches_speaker',
    'speeches_speech',
    'speeches_speech_tags',
    'speeches_tag',
    'za_hansard_answer',
    'za_hansard_pmgcommitteeappearance',
    'za_hansard_pmgcommitteereport',
    'za_hansard_question',
    'za_hansard_questionpaper',
    'za_hansard_source',
    'spinner_imagecontent',
    'spinner_quotecontent',
    'spinner_slide',
]
