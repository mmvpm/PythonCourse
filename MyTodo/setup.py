"""Setup the application."""

import setuptools

setuptools.setup(
    name='my-todo',
    version='0.1.0',
    author='IdeaSeeker',
    author_email='stroganov.n.36@gmail.com',
    description='Simple command-line task-tracking tool.',
    packages=setuptools.find_packages(),
    entry_points={
        'console_scripts': [
            'my-todo=mytodo.command_line:main',
        ],
    },
)
