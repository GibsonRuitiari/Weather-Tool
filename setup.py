from setuptools import setup

setup(
    name='wilio',
    version='1.0',
    py_modules=['weatherTool',
                'config', 'data_sources',
                'models', 'repo'],
    include_package_data=True,
    install_requires=[
        'click',
        'aiohttp', 'dateutil'

    ],
    entry_points='''
        [console_scripts]
        weatherTool=main:main_command
    ''',
)