try:
    from setuptools import setup
except ImportError:
    from distutils import setup
    import warnings
    warnings('Please install setuptools or distribute!')

# Workaround for http://bugs.python.org/issue15881#msg170215
try:
    import multiprocessing  # noqa
except ImportError:
    pass


long_description = open('README.rst').read()

setup(
    name='requirements-parser',
    version='0.2.0',
    description='Parses Pip requirement files',
    long_description=long_description,
    author='David Fischer',
    author_email='djfische@gmail.com',
    url='https://github.com/davidfischer/requirements-parser',
    license='BSD',
    platforms=['OS Independent'],
    packages=['requirements'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    install_requires=['setuptools'],
    tests_require=['nose'],
    test_suite='nose.collector',
)
