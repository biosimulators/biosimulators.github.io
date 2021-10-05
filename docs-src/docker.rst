Docker image
============

A Docker image with a Python environment with APIs for most of the validated simulation tools is available at `https://github.com/orgs/biosimulators/packages/container/package/biosimulators <https://github.com/orgs/biosimulators/packages/container/package/biosimulators>`_. An iPython shell for this environment can be launched by installing Docker and running the commands below. Information about using the Python APIs in the image is available at `https://biosimulators.org/help <https://biosimulators.org/help>`_.::

    docker pull ghcr.io/biosimulators/biosimulators
    docker run -it --rm ghcr.io/biosimulators/biosimulators

This image includes this package, as well as standardized Python APIs for the simulation tools validated by BioSimulators. Because this image aims to incorporate as many simulation tools as possible within a single Python environment, this image may sometimes lag behind the latest version of this package.

The Dockerfile for this image is available `here <https://github.com/biosimulators/Biosimulators/blob/dev/Dockerfile>`_.
