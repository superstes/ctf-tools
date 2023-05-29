import setuptools

with open('README.md', 'r', encoding='utf-8') as info:
    long_description = info.read()

setuptools.setup(
    name='superstes_ctf_tools',
    version='1.0.0',
    author='René Rath',
    author_email='contact@superstes.eu',
    description='Some python utils and scripts that I find useful for security challenges',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/superstes/ctf-tools',
    project_urls={
        'Repository': 'https://github.com/superstes/ctf-tools',
        'Bug Tracker': 'https://github.com/superstes/ctf-tools/issues',
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.3'
)
