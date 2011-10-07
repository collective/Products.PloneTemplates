from setuptools import setup


CLASSIFIERS = [
    'Programming Language :: Python',
    'Framework :: Zope2',
    'Framework :: Plone',
]

version = '1.0.3'

readme_file = 'README.txt'
desc = open(readme_file).read().strip()
changes_file = 'CHANGES.txt'
changes = open(changes_file).read().strip()

long_description = desc + '\n\nCHANGES\n=======\n\n' +  changes 

setup(name='Products.PloneTemplates',
      version=version,
      license='ZPL',
      author='Danny Bloemendaal',
      author_email='danny.bloemendaal@informaat.nl',
      maintainer='Danny Bloemendaal',
      maintainer_email='danny.bloemendaal@informaat.nl',
      classifiers=CLASSIFIERS,
      keywords='Zope Plone Templates', 
      url='http://pypi.python.org/pypi/Products.PloneTemplates',
      description='Content templates for Plone',
      long_description=long_description,
      packages=['Products', 'Products.PloneTemplates'],
      include_package_data = True,
      zip_safe=False,
      install_requires=['setuptools'],
      namespace_packages=['Products'],

      )
