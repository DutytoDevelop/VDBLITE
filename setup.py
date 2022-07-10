from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()


"""
cheat sheet reminder for myself because I'm dumb

python setup.py sdist bdist_wheel
python -m twine upload dist/*
"""


setup(name='vdblite',
      version='0.1',
      description='Vector Database Lite',
      url='https://github.com/daveshap/VDBLITE',
      long_description=long_description,
      long_description_content_type="text/markdown",
      author='David Shapiro',
      author_email='noone@gmail.com',
      license='MIT',
      packages=['vdblite'],
      install_requires=["numpy"],
      extras_require={
        "cpu" = ['faiss-cpu'],
        "gpu" = ['faiss-gpu'],
      },
      zip_safe=False)
