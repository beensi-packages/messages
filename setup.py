from setuptools import setup, find_packages

setup(
    name='messages',
    version='0.01',
    license='BEENSI',
    author='beensi.com dev group',
    # author_email='email@example.com',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='https://github.com/beensi-packages/messages.git',
    # keywords='',
    install_requires=[
    ],

)
