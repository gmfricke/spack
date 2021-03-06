# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import sys

from spack import *


class PyMatplotlib(PythonPackage):
    """matplotlib is a python 2D plotting library which produces publication
    quality figures in a variety of hardcopy formats and interactive
    environments across platforms."""

    homepage = "https://pypi.python.org/pypi/matplotlib"
    url      = "https://pypi.io/packages/source/m/matplotlib/matplotlib-3.1.1.tar.gz"

    maintainers = ['adamjstewart']

    import_modules = [
        'mpl_toolkits', 'matplotlib', 'mpl_toolkits.axes_grid1',
        'mpl_toolkits.axes_grid', 'mpl_toolkits.mplot3d',
        'mpl_toolkits.axisartist', 'matplotlib.compat', 'matplotlib.tri',
        'matplotlib.axes', 'matplotlib.sphinxext', 'matplotlib.cbook',
        'matplotlib.backends', 'matplotlib.style', 'matplotlib.projections',
        'matplotlib.testing', 'matplotlib.backends.qt_editor',
        'matplotlib.testing.jpl_units'
    ]

    version('3.1.1', sha256='1febd22afe1489b13c6749ea059d392c03261b2950d1d45c17e3aed812080c93')
    version('3.0.2', sha256='c94b792af431f6adb6859eb218137acd9a35f4f7442cea57e4a59c54751c36af')
    version('3.0.0', sha256='b4e2333c98a7c2c1ff6eb930cd2b57d4b818de5437c5048802096b32f66e65f9')
    version('2.2.3', sha256='7355bf757ecacd5f0ac9dd9523c8e1a1103faadf8d33c22664178e17533f8ce5')
    version('2.2.2', sha256='4dc7ef528aad21f22be85e95725234c5178c0f938e2228ca76640e5e84d8cde8')
    version('2.0.2', sha256='0ffbc44faa34a8b1704bc108c451ecf87988f900ef7ce757b8e2e84383121ff1')
    version('2.0.0', sha256='36cf0985829c1ab2b8b1dae5e2272e53ae681bf33ab8bedceed4f0565af5f813')
    version('1.5.3', sha256='a0a5dc39f785014f2088fed2c6d2d129f0444f71afbb9c44f7bdf1b14d86ebbc')
    version('1.5.1', sha256='3ab8d968eac602145642d0db63dd8d67c85e9a5444ce0e2ecb2a8fedc7224d40')
    version('1.4.3', sha256='61f201c6a82e89e4d9e324266203fad44f95fd8f36d8eec0d8690273e1182f75')
    version('1.4.2', sha256='17a3c7154f152d8dfed1f37517c0a8c5db6ade4f6334f684989c36dab84ddb54')

    # https://matplotlib.org/tutorials/introductory/usage.html#backends
    # From `matplotlib.rcsetup`:
    interactive_bk = [
        'gtk3agg', 'gtk3cairo', 'macosx', 'nbagg', 'qt4agg', 'qt4cairo',
        'qt5agg', 'qt5cairo', 'tkagg', 'tkcairo', 'webagg', 'wx', 'wxagg',
        'wxcairo'
    ]
    non_interactive_bk = [
        'agg', 'cairo', 'pdf', 'pgf', 'ps', 'svg', 'template'
    ]
    all_backends = interactive_bk + non_interactive_bk

    default_backend = 'agg'
    if sys.platform == 'darwin':
        default_backend = 'macosx'

    variant('backend', default=default_backend, description='Default backend',
            values=all_backends, multi=False)
    variant('movies', default=False,
            description='Enable support for saving movies')
    variant('animation', default=False,
            description='Enable animation support')
    variant('image', default=True,
            description='Enable reading/saving JPEG, BMP and TIFF files')
    variant('latex', default=False,
            description='Enable LaTeX text rendering support')

    # https://matplotlib.org/users/installing.html#dependencies
    # Required dependencies
    extends('python', ignore=r'bin/nosetests.*$|bin/pbr$')
    depends_on('python@2.7:2.8,3.4:', when='@:2')
    depends_on('python@3.5:', when='@3:')
    depends_on('python@3.6:', when='@3.1:')
    depends_on('freetype@2.3:')
    depends_on('libpng@1.2:')
    depends_on('py-numpy@1.11:', type=('build', 'run'))
    depends_on('py-setuptools', type=('build', 'run'))  # See #3813
    depends_on('py-cycler@0.10:', type=('build', 'run'))
    depends_on('py-python-dateutil@2.1:', type=('build', 'run'))
    depends_on('py-kiwisolver@1:', type=('build', 'run'), when='@2.2.0:')
    depends_on('py-pyparsing', type=('build', 'run'))
    depends_on('py-pytz', type=('build', 'run'), when='@:2')
    depends_on('py-subprocess32', type=('build', 'run'), when='^python@:2.7')
    depends_on('py-functools32', type=('build', 'run'), when='@:2.0.999 ^python@2.7')
    depends_on('py-backports-functools-lru-cache', type=('build', 'run'),
               when='@2.1.0:2.999.999 ^python@:2')
    depends_on('py-six@1.9.0:', type=('build', 'run'), when='@:2')

    # Optional backend dependencies
    depends_on('tk@8.3:8.5,8.6.2:', when='backend=tkagg')
    depends_on('tk@8.3:8.5,8.6.2:', when='backend=tkcairo')
    depends_on('python+tkinter', when='backend=tkagg')
    depends_on('python+tkinter', when='backend=tkcairo')
    depends_on('py-pyqt4@4.6:', when='backend=qt4agg')    # or py-pyside@1.0.3:
    depends_on('py-pyqt4@4.6:', when='backend=qt4cairo')  # or py-pyside@1.0.3:
    depends_on('py-pyqt5', when='backend=qt5agg')
    depends_on('py-pyqt5', when='backend=qt5cairo')
    depends_on('py-pygobject', when='backend=gtk3agg')
    depends_on('py-pygobject', when='backend=gtk3cairo')
    depends_on('py-wxpython@4:', when='backend=wx')
    depends_on('py-wxpython@4:', when='backend=wxagg')
    depends_on('py-wxpython@4:', when='backend=wxcairo')
    depends_on('py-cairocffi@0.8:', when='backend=gtk3cairo')
    depends_on('py-cairocffi@0.8:', when='backend=qt4cairo')
    depends_on('py-cairocffi@0.8:', when='backend=qt5cairo')
    depends_on('py-cairocffi@0.8:', when='backend=tkcairo')
    depends_on('py-cairocffi@0.8:', when='backend=wxcairo')
    depends_on('py-cairocffi@0.8:', when='backend=cairo')
    depends_on('py-tornado', when='backend=webagg')

    # Optional dependencies
    depends_on('ffmpeg', when='+movies')
    # depends_on('libav', when='+movies')
    depends_on('imagemagick', when='+animation')
    depends_on('py-pillow@3.4:', when='+image', type=('build', 'run'))
    depends_on('texlive', when='+latex', type='run')
    depends_on('ghostscript@0.9:', when='+latex', type='run')
    depends_on('pkgconfig', type='build')

    # Testing dependencies
    depends_on('py-pytest', type='test')

    msg = 'MacOSX backend requires the Cocoa headers included with XCode'
    conflicts('platform=linux', when='backend=macosx', msg=msg)
    conflicts('platform=bgq',   when='backend=macosx', msg=msg)
    conflicts('platform=cray',  when='backend=macosx', msg=msg)

    # Patch to pick up correct freetype headers
    patch('freetype-include-path.patch', when='@2.2.2:2.9.9')

    @run_before('build')
    def set_backend(self):
        """Set build options with regards to backend GUI libraries."""

        backend = self.spec.variants['backend'].value

        with open('setup.cfg', 'w') as setup:
            # Default backend
            setup.write('[rc_options]\n')
            setup.write('backend = ' + backend + '\n')

    def test(self):
        pytest = which('pytest')
        pytest()
