module_file = open("country_model/__init__.py").read()
long_description = open('README.md').read()

from setuptools import setup, find_packages

setup(
    name='django_countrymodel',
    description='',
    packages=find_packages(),
    author='Ivo Sanchez Checa Crosato',
    author_email='ivoscc [at] gmail.com',
    install_requires=['django', 'django_countries'],
    url='http://github.com/muleros/django-redis-countries',
    license="MIT",
    zip_safe=False,
    keywords="django, countries, models",
    long_description=long_description,
    classifiers=[
        'Development Status :: 1 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Topic :: Internet',
        'Topic :: Software Development :: Libraries',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: POSIX',
        'Programming Language :: Python :: 2.7',
    ]
)
