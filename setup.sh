echo "+++ Installing mplayer"
sudo apt-get install mplayer

echo "+++ Installing python-setuptools"
sudo apt-get install python-setuptools

echo "+++ Installing python-tornado"
sudo easy_install tornado

echo "+++ Creating setup dir"
mkdir setup
cd setup

echo "+++ Installing python-mplayer"
git clone git://github.com/djungowski/mplayer.py.git
cd mplayer.py
sudo python setup.py install

echo "+++ Removing setup dir"
cd ../
cd ../
sudo rm -rf setup
