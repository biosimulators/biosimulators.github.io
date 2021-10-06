BioSimulators technical documentation
=====================================

This package provides a summary of the documentation for the `BioSimulators <https://biosimulators.org>`_ registry of biosimulation tools.

* Tutorials for users and developers of simulation tools
  
  * `Executing simulations online <https://biosimulators.org/help>`_
  * `Executing simulations using standardized Docker images <https://biosimulators.org/help>`_
  * `Executing simulations using standardized command-line applications <https://biosimulators.org/help>`_
  * `Programmatically introspecting model/simulation files <https://mybinder.org/v2/gh/biosimulators/Biosimulators_tutorials/HEAD>`_
  * `Programmatically creating SED-ML files and COMBINE/archives from model model/simulation files <https://mybinder.org/v2/gh/biosimulators/Biosimulators_tutorials/HEAD>`_
  * `Programmatically retrieving information about the capabilities of simulation tools <https://mybinder.org/v2/gh/biosimulators/Biosimulators_tutorials/HEAD>`_
  * `Programmatically executing simulations in Python <https://mybinder.org/v2/gh/biosimulators/Biosimulators_tutorials/HEAD>`_
  * `Creating standardized interfaces to simulation tools <https://github.com/biosimulators/Biosimulators_simulator_template>`_

* `Example SED-ML files and COMBINE archives <https://github.com/biosimulators/Biosimulators_test_suite/tree/dev/examples>`_. This includes examples for the BioNetGen Language (BNGL), CellML, NeuroML/LEMS, the RBApy language, the Smoldyn language, the Systems Biology Markup Language (SBML), SBML-fbc, SBML-qual, the SBML schema for MASS models, and XPP.
* `Template Python package for a standardized interface to a simulation tool <https://github.com/biosimulators/Biosimulators_simulator_template>`_
* `FAQs for users and developers of simulation tools <https://biosimulators.org/help/faq>`_
* `Documentation about BioSimulators' conventions for users and developers of simulation tools <https://biosimulators.org/standards>`_
* Documementation for users of the Python packages for the individual standardized simulation tools available through BioSimulators

  * `AMICI <https://docs.biosimulators.org/Biosimulators_AMICI/>`_
  * `BioNetGen <https://docs.biosimulators.org/Biosimulators_BioNetGen/>`_
  * `BoolNet <https://docs.biosimulators.org/Biosimulators_BoolNet/>`_
  * `CBMPy <https://docs.biosimulators.org/Biosimulators_CBMPy/>`_
  * `COBRApy <https://docs.biosimulators.org/Biosimulators_COBRApy/>`_
  * `COPASI <https://docs.biosimulators.org/Biosimulators_COPASI/>`_
  * `GillesPy2 <https://docs.biosimulators.org/Biosimulators_GillesPy2/>`_
  * `GINsim <https://docs.biosimulators.org/Biosimulators_GINsim/>`_
  * `LibSBMLSim <https://docs.biosimulators.org/Biosimulators_LibSBMLSim/>`_
  * `MASSpy <https://docs.biosimulators.org/Biosimulators_MASSpy/>`_
  * `NetPyNe <https://docs.biosimulators.org/Biosimulators_pyNeuroML/>`_
  * `NEURON <https://docs.biosimulators.org/Biosimulators_pyNeuroML/>`_
  * `OpenCOR <https://docs.biosimulators.org/Biosimulators_OpenCOR/>`_
  * `pyNeuroML <https://docs.biosimulators.org/Biosimulators_pyNeuroML/>`_
  * `PySCeS <https://docs.biosimulators.org/Biosimulators_PySCeS/>`_
  * `RBApy <https://docs.biosimulators.org/Biosimulators_RBApy/>`_
  * `Smoldyn <https://smoldyn.readthedocs.io/en/latest/python/api.html#sed-ml-combine-biosimulators-api>`_
  * `tellurium <https://docs.biosimulators.org/Biosimulators_tellurium/>`_
  * `VCell <https://github.com/virtualcell/vcell>`_
  * `XPP <https://docs.biosimulators.org/Biosimulators_XPP/>`_

* Documentation for using SED-ML and COMBINE archives with model languages

  * `BioNetGen Language (BNGL) <https://docs.biosimulators.org/Biosimulators_BioNetGen/tutorial.html>`_  
  * `CellML <http://sed-ml.org/specifications.html>`_
  * `NeuroML/LEMS <https://docs.neuroml.org/Userdocs/Paths.html>`_
  * `RBApy  <https://docs.biosimulators.org/Biosimulators_RBApy/tutorial.html>`_
  * `Smoldyn language <https://github.com/ssandrews/Smoldyn/blob/master/Using-Smoldyn-with-SED-ML-COMBINE-BioSimulators.md>`_
  * `Systems Biology Markup Language (SBML) <http://sed-ml.org/specifications.html>`_ including SBML-fbc, SBML-qual, and the SBML schema for MASS models
  * `XPP <https://docs.biosimulators.org/Biosimulators_XPP/tutorial.html>`_

* URNs and specification URIs for using using SED-ML and COMBINE archives with model languages

    ==============  ===============  ==============================  ========================================================  ==========================  =====================
    Language        EDAM format      SED-ML URN                      COMBINE archive specification URI                         MIME type                   Extensions
    ==============  ===============  ==============================  ========================================================  ==========================  =====================
    BNGL            ``format_3972``  ``urn:sedml:language:bngl``     ``http://purl.org/NET/mediatypes/text/bngl+plain``        ``text/bngl+plain``         ``.bngl``
    CellML          ``format_3240``  ``urn:sedml:language:cellml``   ``http://identifiers.org/combine.specifications/cellml``  ``application/cellml+xml``  ``.xml``, ``.cellml``
    (NeuroML)/LEMS  ``format_9004``  ``urn:sedml:language:lems``     ``http://purl.org/NET/mediatypes/application/lems+xml``   ``application/lems+xml``    ``.xml``
    RBA             ``format_9012``  ``urn:sedml:language:rba``      ``http://purl.org/NET/mediatypes/application/rba+zip``    ``application/rba+zip``     ``.zip``
    SBML            ``format_2585``  ``urn:sedml:language:sbml``     ``http://identifiers.org/combine.specifications/sbml``    ``application/sbml+xml``    ``.xml``, ``.sbml``
    Smoldyn         ``format_9001``  ``urn:sedml:language:smoldyn``  ``http://purl.org/NET/mediatypes/text/smoldyn+plain``     ``text/smoldyn+plain``      ``.txt``
    XPP             ``format_9010``  ``urn:sedml:language:xpp``      ``http://purl.org/NET/mediatypes/text/x-xpp``             ``text/x-xpp``              ``.xpp``
    ==============  ===============  ==============================  ========================================================  ==========================  =====================

* `Documentation about the BioSimulators util library for developers of simulation tools <https://docs.biosimulators.org/Biosimulators_utils/>`_
* `Documentation about the BioSimulators test suite for developers of simulation tools <https://docs.biosimulators.org/Biosimulators_test_suite/>`_
* `Information about combining multiple models and/or simulation tools using Vivarium <https://vivarium-collective.github.io/>`_

Contents
--------

.. toctree::
   :maxdepth: 2

   docker.rst
   about.rst
