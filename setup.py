"""Setup file for ai2es_xai_course."""

from setuptools import setup

PACKAGE_NAMES = [
    'ai2es_xai_course', 'ai2es_xai_course.utils',
    'ai2es_xai_course.plotting'
]
KEYWORDS = [
    'machine learning', 'deep learning', 'artificial intelligence',
    'data science', 'weather', 'meteorology', 'thunderstorm', 'wind', 'tornado',
    'explainable ML', 'explainable AI', 'XAI', 'interpretable ML',
    'interpretable AI'
]
SHORT_DESCRIPTION = (
    'Notebooks for AI2ES (NSF Institute for Research on Trustworthy Artificial '
    'Intelligence in Weather, Climate, and Coastal Oceanography) short course '
    'on XAI (explainable artificial intelligence).'
)
LONG_DESCRIPTION = SHORT_DESCRIPTION
CLASSIFIERS = [
    'Development Status :: 2 - Pre-Alpha',
    'Intended Audience :: Science/Research',
    'Programming Language :: Python :: 3'
]

PACKAGE_REQUIREMENTS = [
    'numpy',
    'scipy',
    'tensorflow',
    'keras',
    'scikit-learn',
    'scikit-image',
    'netCDF4',
    'pyproj',
    'opencv-python',
    'matplotlib',
    'pandas',
    'shapely',
    'descartes',
    'geopy',
    'dill'
]

if __name__ == '__main__':
    setup(
        name='ai2es_xai_course',
        version='0.1',
        description=SHORT_DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        author='Ryan Lagerquist',
        author_email='ralager@colostate.edu',
        url='https://github.com/thunderhoser/ai2es_xai_course',
        packages=PACKAGE_NAMES,
        scripts=[],
        keywords=KEYWORDS,
        classifiers=CLASSIFIERS,
        include_package_data=True,
        zip_safe=False,
        install_requires=PACKAGE_REQUIREMENTS
    )
