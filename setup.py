from setuptools import setup, find_packages

setup(name='social_ids',
      version='1.0',
      description="Get user ids from social network handlers",
      author='Guillermo Carrasco',
      author_email='guillermo@getfanzone.com',
      url='https://github.com/guillermo-carrasco/social_ids',
      packages=find_packages(),
      include_package_data=True,
      keywords=['Social Media', 'Facebook', 'Twitter', 'Instagram'],
      zip_safe=True,
      install_requires=[],
      entry_points={
        'console_scripts': ['socialid = social_ids.cli.get_ids:get_id']
    },
      classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3"
      ]
)
