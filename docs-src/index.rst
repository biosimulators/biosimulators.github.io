BioSimulators technical documentation
=====================================

This package provides a summary of the documentation for the `BioSimulators <https://biosimulators.org>`_ registry of biosimulation tools.

* `Tutorials for users and developers of simulation tools <https://biosimulators.org/help>`_
* `Example SED-ML files and COMBINE archives <https://github.com/biosimulators/Biosimulators_test_suite/tree/dev/examples>`_. This includes examples for the BioNetGen Language (BNGL), CellML, NeuroML/LEMS, the Smolydn language, and the Systems Biology Markup Language (SBML).
* `FAQs for users and developers of simulation tools <https://biosimulators.org/help/faq>`_
* `Documentation about BioSimulators' conventions for users and developers of simulation tools <https://biosimulators.org/standards>`_
* Documementation for users of the Python packages for the individual standardized simulation tools available through BioSimulators

  * `AMICI <https://biosimulators.github.io/Biosimulators_AMICI/>`_
  * `BioNetGen <https://biosimulators.github.io/Biosimulators_BioNetGen/>`_
  * `BoolNet <https://biosimulators.github.io/Biosimulators_BoolNet/>`_
  * `CBMPy <https://biosimulators.github.io/Biosimulators_CBMPy/>`_
  * `COBRAPy <https://biosimulators.github.io/Biosimulators_COBRAPy/>`_
  * `COPASI <https://biosimulators.github.io/Biosimulators_COPASI/>`_
  * `GillesPy2 <https://biosimulators.github.io/Biosimulators_GillesPy2/>`_
  * `GINsim <https://biosimulators.github.io/Biosimulators_GINsim/>`_
  * `NetPyNe <https://biosimulators.github.io/Biosimulators_pyNeuroML/>`_
  * `NEURON <https://biosimulators.github.io/Biosimulators_pyNeuroML/>`_
  * `OpenCOR <https://biosimulators.github.io/Biosimulators_OpenCOR/>`_
  * `pyNeuroML <https://biosimulators.github.io/Biosimulators_pyNeuroML/>`_
  * `PySCeS <https://biosimulators.github.io/Biosimulators_PySCeS/>`_
  * `Smoldyn <https://smoldyn.readthedocs.io/en/latest/python/api.html#sed-ml-combine-biosimulators-api>`_
  * `tellurium <https://biosimulators.github.io/Biosimulators_tellurium/>`_
  * `VCell <https://github.com/virtualcell/vcell>`_

* Documentation for using SED-ML and COMBINE archives with model languages

  * `BioNetGen Language (BNGL) <https://biosimulators.github.io/Biosimulators_BioNetGen/tutorial.html>`_  
  * `CellML <http://sed-ml.org/specifications.html>`_
  * `Smoldyn language <https://github.com/ssandrews/Smoldyn/blob/master/Using-Smoldyn-with-SED-ML-COMBINE-BioSimulators.md>`_
  * `Systems Biology Markup Language (SBML) <http://sed-ml.org/specifications.html>`_

* URNs and specification URIs for using using SED-ML and COMBINE archives with model languages

    ==============  ===============  ==============================  ========================================================  ==========================  =====================
    Language        EDAM format      SED-ML URN                      COMBINE archive specification URI                         MIME type                   Extensions
    ==============  ===============  ==============================  ========================================================  ==========================  =====================
    BNGL            ``format_3972``  ``urn:sedml:language:bngl``     ``http://purl.org/NET/mediatypes/text/bngl+plain``        ``text/bngl+plain``         ``.bngl``
    CellML          ``format_3240``  ``urn:sedml:language:cellml``   ``http://identifiers.org/combine.specifications/cellml``  ``application/cellml+xml``  ``.xml``, ``.cellml``
    (NeuroML)/LEMS  ``format_9004``  ``urn:sedml:language:lems``     ``http://purl.org/NET/mediatypes/application/lems+xml``   ``application/lems+xml``    ``.xml``
    SBML            ``format_2585``  ``urn:sedml:language:sbml``     ``http://identifiers.org/combine.specifications/sbml``    ``application/sbml+xml``    ``.xml``, ``.sbml``
    Smoldyn         ``format_9001``  ``urn:sedml:language:smoldyn``  ``http://purl.org/NET/mediatypes/text/smoldyn+plain``     ``text/smoldyn+plain``      ``.txt``
    ==============  ===============  ==============================  ========================================================  ==========================  =====================

* `Documentation about the BioSimulators util library for developers of simulation tools <https://biosimulators.github.io/Biosimulators_utils/>`_
* `Documentation about the BioSimulators test suite for developers of simulation tools <https://biosimulators.github.io/Biosimulators_test_suite/>`_


Contents
--------

.. toctree::
   :maxdepth: 3
   :numbered:

   about.rst
