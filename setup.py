from setuptools import setup

setup(name='minimap_reminder',
      version='0.1',
      description='Play random sound to remind you to look at minimap',
      url='https://github.com/Theraggon/MinimapReminder',
      author='Theraggon',
      author_email='theraggon@gmail.com',
      license='Apache-2.0',
      packages=['minimap_reminder'],
      install_requires=[
          'playsound',
      ],
      zip_safe=False)
