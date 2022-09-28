#!/bin/bash

if [ "$#" -ne 1 ]; then
    echo "Usage: setup.sh SERVER_IP" >&2
    exit 1
fi

SERVER_IP="$1"

set -e

# quietly add a user without password
sudo adduser --quiet --disabled-password --shell /bin/bash --home /home/pioner --gecos "Pioner" pioner

# set password
echo "pioner:voyager" | sudo chpasswd

cat sources.list | sed s/SERVER_IP/${SERVER_IP}/ > sources.list.patched
cat pip.conf | sed s/SERVER_IP/${SERVER_IP}/ > pip.conf.patched

sudo cp /etc/apt/sources.list /etc/apt/sources.list.default
sudo cp sources.list.patched /etc/apt/sources.list
sudo apt-get update -y
sudo apt-get upgrade -y
sudo apt-get install -y --allow-unauthenticated g++ qtcreator python3-venv python3-pip openssh-server syncthing htop mc cmake qtcreator git gimp tmux

# For PyQt, for spyder from pip:
sudo apt install black blt docutils-common fonts-elusive-icons fonts-font-awesome fonts-lyx fonts-mathjax helpdev ipython3  libapr1 libaprutil1 libboost-dev libboost1.74-dev libcmark-gfm-extensions0.29.0.gfm.3  libcmark-gfm0.29.0.gfm.3 libjs-jquery-ui libjs-mathjax liblbfgsb0 libopenblas-dev libopenblas-pthread-dev  libopenblas0 libopenblas0-pthread libqhull-r8.0 libqt5location5 libqt5positioningquick5 libqt5websockets5  libserf-1-1 libsvn1 libtk8.6 libutf8proc2 libxsimd-dev mercurial mercurial-common pandoc pandoc-data  pyflakes3 pylint python-babel-localedata python-matplotlib-data python-qtawesome-common python3-alabaster  python3-appdirs python3-astroid python3-atomicwrites python3-attr python3-autopep8 python3-babel  python3-backcall python3-beniget python3-bleach python3-brotli python3-bs4 python3-certifi  python3-cloudpickle python3-cycler python3-dateutil python3-decorator python3-defusedxml  python3-diff-match-patch python3-docutils python3-entrypoints python3-fonttools python3-fs python3-gast  python3-html5lib python3-idna python3-imagesize python3-intervaltree python3-ipykernel python3-ipython  python3-ipython-genutils python3-isort python3-jedi python3-jinja2 python3-jsonschema  python3-jupyter-client python3-jupyter-core python3-jupyterlab-pygments python3-kiwisolver  python3-lazy-object-proxy python3-logilab-common python3-lxml python3-lz4 python3-markupsafe  python3-matplotlib python3-matplotlib-inline python3-mccabe python3-mock python3-mpmath  python3-mypy-extensions python3-nbclient python3-nbconvert python3-nbformat python3-nest-asyncio  python3-numpy python3-numpydoc python3-packaging python3-pandocfilters python3-parso python3-pathspec  python3-pbr python3-pep8 python3-pickleshare python3-pil.imagetk python3-platformdirs python3-pluggy  python3-ply python3-prompt-toolkit python3-psutil python3-py python3-pycodestyle python3-pydocstyle  python3-pyflakes python3-pyls python3-pyls-black python3-pyls-jsonrpc python3-pylsp  python3-pylsp-jsonrpc python3-pyqt5.qtmultimedia python3-pyqt5.qtopengl python3-pyqt5.qtpositioning  python3-pyqt5.qtquick python3-pyqt5.qtsensors python3-pyqt5.qtserialport python3-pyqt5.qtsql  python3-pyqt5.qtsvg python3-pyqt5.qttexttospeech python3-pyqt5.qtwebchannel python3-pyqt5.qtwebengine  python3-pyqt5.qtwebkit python3-pyqt5.qtwebsockets python3-pyqt5.qtxmlpatterns python3-pyrsistent  python3-pythran python3-qdarkstyle python3-qtawesome python3-qtconsole python3-qtpy python3-requests  python3-roman python3-rope python3-scipy python3-snowballstemmer python3-sortedcontainers  python3-soupsieve python3-sphinx python3-svn python3-sympy  python3-testpath python3-textdistance python3-three-merge python3-tk python3-toml python3-tomli  python3-traitlets python3-typing-extensions python3-tz python3-ufolib2 python3-ujson python3-unicodedata2  python3-urllib3 python3-watchdog python3-wcwidth python3-webencodings python3-wrapt python3-wurlitzer  python3-xdg python3-yapf python3-zmq sphinx-common tk8.6-blt2.5 unicode-data

sudo mkdir -p /home/pioner/.config/pip/
sudo cp pip.conf.patched /home/pioner/.config/pip/pip.conf
sudo chown -R pioner:pioner /home/pioner/.config

sudo su pioner <<EOSU
mkdir -p /home/pioner/.config/pip/
cp pip.conf.patched /home/pioner/.config/pip/pip.conf
EOSU


