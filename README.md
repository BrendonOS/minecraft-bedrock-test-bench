spiffy [![CircleCI](https://img.shields.io/circleci/project/spiffy/spiffy.svg)]() [![Gitter](https://badges.gitter.im/spiffy/spiffy.svg)](https://gitter.im/spiffy/spiffy?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge)
======
**A Minecraft: PE server in Python**

The brainchild of four, who like Python and like Minecraft: PE...
<img align="right" src="https://raw.githubusercontent.com/ZedCee/various_graphics/master/sheepLogo/sheepLogoCrossSectionTrans.png" height="250" width="250">

### Features
- Python plugin system
- Threaded RakLib with deadlock security
- Parts written as C extensions for maximum speed
- LevelDB world saving/loading
### Dependencies
* Python 3.5 (CPython, PyPy or Nuitka if you're feeling dangerous :wink:)
* virtualenv, preferrably installed via pip (may also be installed via source or Linux repository)

### Installation
It's easy, just make sure you've got virtualenv (preferrably installed via pip, may also be installed via source or Linux repository) and Python 3.5 (CPython, PyPy or Nuitka if you're feeling dangerous :wink:) then just run the following
```sh
$ pip install virtualenv  # Optional, but highly, highly recommended
$ virtualenv -p /usr/bin/python .venv
$ source ./venv/bin/activate
$ pip install -r requirements.txt
$ python main.py
$ deactivate
```

### Chat / Help & Support

This project is presently a work in progress
<!--If you have an issue, please make sure to check the [FAQs](https://github.com/spiffy/spiffy/wiki/FAQs) page before opening any issues. We are constantly fixing issues and are continuously updating, so please also ensure that you are up-to-date before opening any issues.-->

### Licence
We're licensed under the GNU GPLv3, here's your copy:

	This program is free software: you can redistribute it and/or modify
	it under the terms of the GNU General Public License as published by
	the Free Software Foundation, either version 3 of the License, or
	(at your option) any later version.

	This program is distributed in the hope that it will be useful,
	but WITHOUT ANY WARRANTY; without even the implied warranty of
	MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
	GNU General Public License for more details.

	You should have received a copy of the GNU General Public License
	along with this program.  If not, see <http://www.gnu.org/licenses/>.

Logo by [@ZedCee](https://github.com/ZedCee) - *All rights reserved, copy and reuse of the logo is forbidden*
