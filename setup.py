"""Golem: An Algorithm for Robust Experiment and Process Optimization
"""

import versioneer
from setuptools import setup, Extension
import numpy as np


# readme file
def readme():
    with open('README.md') as f:
        return f.read()


# extensions
ext_modules = [Extension("golem.extensions",
                         ["src/golem/extensions.c"],
                         include_dirs=[np.get_include()],
                         # pin to the NumPy 1.7 C API explicitly: silences the
                         # "deprecated NumPy API" build warning and makes explicit
                         # that we rely only on the long-stable subset of the API,
                         # which is what keeps this extension forward/backward
                         # compatible across NumPy 1.x and 2.x at runtime.
                         define_macros=[("NPY_NO_DEPRECATED_API", "NPY_1_7_API_VERSION")])]

# -----
# Setup
# -----
setup(name='matter-golem',
      version=versioneer.get_version(),
      cmdclass=versioneer.get_cmdclass(),
      description='Golem: An Algorithm for Robust Experiment and Process Optimization',
      long_description=readme(),
      long_description_content_type='text/markdown',
      classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering',
      ],
      url='https://github.com/aspuru-guzik-group/golem',
      author='Matteo Aldeghi',
      author_email='matteo.aldeghi@vectorinstitute.ai',
      license='MIT',
      packages=['golem'],
      package_dir={'': 'src'},
      zip_safe=False,
      tests_require=['pytest', 'deap'],
      # numpy>=1.22 matches the floor chosen for matter-chimera (see its setup.py);
      # no ceiling is set because the extension is now built against numpy>=2.0,
      # which numpy's own ABI-compatibility guarantee extends back to numpy 1.x
      # and forward to all future 2.x releases.
      install_requires=['numpy>=1.22', 'scipy>=1.4', 'scikit-learn', 'pandas'],
      # 3.7/3.8 are EOL upstream; floor raised to match the CI matrix in
      # .github/workflows/ci.yml.
      python_requires=">=3.9",
      ext_modules=ext_modules
      )
