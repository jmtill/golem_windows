Installation
============

**Golem** can be installed with ``pip``::

    pip install matter-golem

Alternatively, you can clone the GitHub repo and install it from source::

    git clone https://github.com/aspuru-guzik-group/golem.git
    cd golem
    pip install .

Requirements
------------

* python >= 3.7
* numpy_
* scipy_ >= 1.4
* pandas_
* scikit-learn_

.. _numpy: http://www.numpy.org/
.. _scipy: https://www.scipy.org
.. _pandas: https://pandas.pydata.org/
.. _scikit-learn: https://scikit-learn.org/stable/

Windows
-------

Installing from source on Windows requires the `Microsoft C++ Build Tools <https://visualstudio.microsoft.com/visual-cpp-build-tools/>`_
(or a full Visual Studio install with the "Desktop development with C++" workload), since ``pip install matter-golem``
falls back to compiling the ``golem.extensions`` Cython extension from source whenever no prebuilt wheel matches your
Python version/architecture.

Multiprocessing on Windows
~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Golem** uses ``concurrent.futures.ProcessPoolExecutor`` for multiprocessing when ``nproc`` > 1. Windows'
multiprocessing ``spawn`` start method re-imports your script's ``__main__`` module in every worker process, so any
script that creates a **Golem** instance with ``nproc`` > 1 (directly, or transitively via another package that does)
must guard its entry point::

    if __name__ == "__main__":
        main()

Without this guard, Windows can hang, crash, or recursively re-spawn processes. To reduce the risk of hitting this by
surprise, **Golem** defaults to ``nproc=1`` on Windows (instead of ``cpu_count() - 1`` as on Linux/macOS); pass
``nproc`` explicitly once your script's entry point is guarded.
