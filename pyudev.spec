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
%autosetup -p1

%build
%py_build

%install
%py_install

%files
%dir %{py_puresitedir}/pyudev/
%{py_puresitedir}/pyudev/*
%dir %{py_puresitedir}/pyudev-*-py%{py_ver}.egg-info/
%{py_puresitedir}/pyudev-*-py%{py_ver}.egg-info/*
