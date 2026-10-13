Summary:	A libudev binding
Name:		pyudev
Version:	0.24.4
Release:	2
Source0:	https://github.com/pyudev/pyudev/archive/v%{version}/%{name}-%{version}.tar.gz
License:	MIT or X11
URL:		https://github.com/pyudev/pyudev
Group:		Development/Python
BuildSystem:	python
BuildArch:	noarch
BuildRequires:	python%{pyver}dist(setuptools)
Requires:	udev
Suggests:	python-gi

%description
pyudev is a Python binding to libudev, the hardware management library
and service found in modern linux systems.

%files
%dir %{py_puresitedir}/pyudev/
%{py_puresitedir}/pyudev/*
%{py_puresitedir}/*-%{version}.*-info
