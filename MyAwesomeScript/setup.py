"""Setup the application."""

import setuptools

setuptools.setup(
    name='my-awesome-script',
    version='0.1.0',
    author='IdeaSeeker',
    author_email='stroganov.n.36@gmail.com',
    description='Simple command-line tool.',
    packages=setuptools.find_packages(),
    entry_points={
        'console_scripts': [
            'my-awesome-script=myawesomescript.command_line:main',
        ],
    },
)
