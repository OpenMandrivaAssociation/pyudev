Summary:	A libudev binding
Name:		pyudev
Version:	0.24.0
Release:	1
Source0:	https://github.com/pyudev/pyudev/archive/v%{version}.tar.gz
License:	MIT or X11
URL:		http://packages.python.org/pyudev
Group:		Development/Python
BuildArch:	noarch
BuildRequires:	python-pkg-resources
BuildRequires:	python-setuptools
Requires:	udev
Suggests:	python-gi

%description
pyudev is a Python binding to libudev, the hardware management library
and service found in modern linux systems.

%prep
%setup -q -c
mv %{name}-%{version} python3
cp -r python3 python2

%build
pushd python3
python setup.py build
popd

%install
pushd python3
python setup.py install --root=%{buildroot}
popd

%files
%dir %{py_puresitedir}/pyudev/
%{py_puresitedir}/pyudev/*
%dir %{py_puresitedir}/pyudev-*-py%{py_ver}.egg-info/
%{py_puresitedir}/pyudev-*-py%{py_ver}.egg-info/*
