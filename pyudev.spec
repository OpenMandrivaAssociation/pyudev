Summary:	A libudev binding
Name:		pyudev
Version:	0.16.1
Release:	1
Source0:	http://pypi.python.org/packages/source/p/pyudev/%{name}-%{version}.tar.gz
License:	MIT or X11
URL:		http://packages.python.org/pyudev
Group:		Development/Python
BuildArch:	noarch
BuildRequires:	pythonegg(setuptools)
Requires:	udev
Suggests:	python-qt4
Suggests:	python-gobject

%description
pyudev is a Python binding to libudev, the hardware management library
and service found in modern linux systems.

%prep
%setup -q

%build
python setup.py build

%install
python setup.py install --root=%{buildroot}

%files
%dir %{py_puresitedir}/pyudev/
%{py_puresitedir}/pyudev/*
%dir %{py_puresitedir}/pyudev-%{version}-py%{py_ver}.egg-info/
%{py_puresitedir}/pyudev-%{version}-py%{py_ver}.egg-info/*
