from setuptools import setup, find_packages

setup(
    name='math_quiz_mohamedelaggouri',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        # Add your dependencies here
    ],
    entry_points={
        'console_scripts': [
            'math_quiz=math_quiz.math_quiz:main',
        ],
    },
)