# BioSimulators documentation
This package provides a summary of the documentation for the [BioSimulators](https://biosimulators.org) registry of biosimulation tools.

* [Tutorials for users and developers of simulation tools](https://biosimulators.org/help)
* [Example SED-ML files and COMBINE archives](https://github.com/biosimulators/Biosimulators_test_suite/tree/dev/examples). This includes examples for the BioNetGen Language (BNGL), CellML, NeuroML/LEMS, the RBApy language, the Smoldyn language, the Systems Biology Markup Language (SBML), SBML-fbc, SBML-qual, the SBML schema for MASS models, and XPP.
* [FAQs for users and developers of simulation tools](https://biosimulators.org/help/faq)
* [Documentation about BioSimulators' conventions for users and developers of simulation tools](https://biosimulators.org/standards)
* Documementation for users of the Python packages for the individual standardized simulation tools available through BioSimulators
  * [AMICI](https://biosimulators.github.io/Biosimulators_AMICI/)
  * [BioNetGen](https://biosimulators.github.io/Biosimulators_BioNetGen/)
  * [BoolNet](https://biosimulators.github.io/Biosimulators_BoolNet/)
  * [CBMPy](https://biosimulators.github.io/Biosimulators_CBMPy/)
  * [COBRAPy](https://biosimulators.github.io/Biosimulators_COBRAPy/)
  * [COPASI](https://biosimulators.github.io/Biosimulators_COPASI/)
  * [GillesPy2](https://biosimulators.github.io/Biosimulators_GillesPy2/)
  * [GINsim](https://biosimulators.github.io/Biosimulators_GINsim/)
  * [LibSBMLSim](https://biosimulators.github.io/Biosimulators_LibSBMLSim/)
  * [MASSpy](https://biosimulators.github.io/Biosimulators_MASSpy/)
  * [NetPyNe](https://biosimulators.github.io/Biosimulators_pyNeuroML/)
  * [NEURON](https://biosimulators.github.io/Biosimulators_pyNeuroML/)  
  * [OpenCOR](https://biosimulators.github.io/Biosimulators_OpenCOR/)
  * [pyNeuroML](https://biosimulators.github.io/Biosimulators_pyNeuroML/)
  * [PySCeS](https://biosimulators.github.io/Biosimulators_PySCeS/)
  * [RBApy](https://biosimulators.github.io/Biosimulators_RBApy/)
  * [Smoldyn](https://smoldyn.readthedocs.io/en/latest/python/api.html#sed-ml-combine-biosimulators-api)
  * [tellurium](https://biosimulators.github.io/Biosimulators_tellurium/)
  * [VCell](https://github.com/virtualcell/vcell)
  * [XPP](https://biosimulators.github.io/Biosimulators_XPP/)
* Documentation for using SED-ML and COMBINE archives with model languages
  * [BioNetGen Language (BNGL)](https://biosimulators.github.io/Biosimulators_BioNetGen/tutorial.html)
  * [CellML](http://sed-ml.org/specifications.html)
  * [NeuroML/LEMS](https://docs.neuroml.org/Userdocs/Paths.html)
  * [RBApy](https://biosimulators.github.io/Biosimulators_RBApy/tutorial.html)
  * [Smoldyn language](https://github.com/ssandrews/Smoldyn/blob/master/Using-Smoldyn-with-SED-ML-COMBINE-BioSimulators.md)
  * [Systems Biology Markup Language (SBML)](http://sed-ml.org/specifications.html) including SBML-fbc, SBML-qual, and the SBML schema for MASS models
  * [XPP](https://biosimulators.github.io/Biosimulators_XPP/tutorial.html)
* URNs and specification URIs for using using SED-ML and COMBINE archives with model languages
    | Language       | EDAM format   | SED-ML URN                   | COMBINE archive specification URI                      | MIME type                | Extensions        |
    | -------------- | ------------- | ---------------------------- | ------------------------------------------------------ | ------------------------ | ----------------- |
    | BNGL           | `format_3972` | `urn:sedml:language:bngl`    | `http://purl.org/NET/mediatypes/text/bngl+plain`       | `text/bngl+plain`        | `.bngl`           |
    | CellML         | `format_3240` | `urn:sedml:language:cellml`  | `http://identifiers.org/combine.specifications/cellml` | `application/cellml+xml` | `.xml`, `.cellml` |
    | (NeuroML)/LEMS | `format_9004` | `urn:sedml:language:lems`    | `http://purl.org/NET/mediatypes/application/lems+xml`  | `application/lems+xml`   | `.xml`            |
    | RBA            | `format_9012` | `urn:sedml:language:rba`     | `http://purl.org/NET/mediatypes/application/rba+zip`   | `application/rba+zip`    | `.zip`            |
    | SBML           | `format_2585` | `urn:sedml:language:sbml`    | `http://identifiers.org/combine.specifications/sbml`   | `application/sbml+xml`   | `.xml`, `.sbml`   |
    | Smoldyn        | `format_9001` | `urn:sedml:language:smoldyn` | `http://purl.org/NET/mediatypes/text/smoldyn+plain`    | `text/smoldyn+plain`     | `.txt`            |
    | XPP            | `format_9010` | `urn:sedml:language:xpp`     | `http://purl.org/NET/mediatypes/text/x-xpp`            | `text/x-xpp`             | `.xpp`            |
* [Documentation about the BioSimulators util library for developers of simulation tools](https://biosimulators.github.io/Biosimulators_utils/)
* [Documentation about the BioSimulators test suite for developers of simulation tools](https://biosimulators.github.io/Biosimulators_test_suite/)

## License
BioSimulators is released under the [MIT License](https://github.com/biosimulators/Biosimulators/blob/dev/LICENSE).

## Development team
BioSimulators was developed by the [Karr Lab](https://www.karrlab.org) at the Icahn School of Medicine at Mount Sinai in New York and the [Center for Reproducible Biomedical Modeling](http://reproduciblebiomodels.org).

## Contributing to BioSimulators
We enthusiastically welcome contributions to BioSimulators! Please see the [guide to contributing](https://github.com/biosimulators/Biosimulators/blob/dev/CONTRIBUTING.md) and the [developer's code of conduct](https://github.com/biosimulators/Biosimulators/blob/dev/CODE_OF_CONDUCT.md).

## Acknowledgements
This work was supported by National Institutes of Health award P41EB023912.

## Questions and comments
Please contact the [BioSimulators Team](mailto:info@biosimulators.org) with any questions or comments.
