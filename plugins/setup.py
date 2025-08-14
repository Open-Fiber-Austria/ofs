from setuptools import setup, find_packages

setup(
    name='mkdocs-auto-glossary-link',
    version='0.1',
    packages=find_packages(),
    entry_points={
        'mkdocs.plugins': [
            'auto_glossary_link = auto_glossary_link.plugin:AutoGlossaryLinkPlugin'
        ]
    },
)





