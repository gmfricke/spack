# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class PyGast(PythonPackage):
    """Python AST that abstracts the underlying Python version"""

    homepage = "https://github.com/serge-sans-paille/gast"
    url      = "https://pypi.io/packages/source/g/gast/gast-0.3.2.tar.gz"

    version('0.3.2', sha256='5c7617f1f6c8b8b426819642b16b9016727ddaecd16af9a07753e537eba8a3a5')
    version('0.2.0', sha256='7068908321ecd2774f145193c4b34a11305bd104b4551b09273dfd1d6a374930')

    depends_on('py-setuptools', type='build')
