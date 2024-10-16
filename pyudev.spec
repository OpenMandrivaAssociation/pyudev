Summary:	A libudev binding
Name:		pyudev
Version:	0.24.3
Release:	1
Source0:	https://github.com/pyudev/pyudev/archive/v%{version}.tar.gz
License:	MIT or X11
URL:		https://packages.python.org/pyudev
Group:		Development/Python
BuildArch:	noarch
BuildRequires:	python-pkg-resources
BuildRequires:	python-setuptools
Requires:	udev
Suggests:	python-gi
BuildSystem:	python

%description
pyudev is a Python binding to libudev, the hardware management library
and service found in modern linux systems.

%files
%dir %{py_puresitedir}/pyudev/
%{py_puresitedir}/pyudev/*
%{py_puresitedir}/*-%{version}.*-info
