Summary: A libudev binding
Name: pyudev
Version: 0.13
Release: %mkrel 1
Source0: http://pypi.python.org/packages/source/p/pyudev/%{name}-%{version}.tar.gz
License: MIT or X11
URL: http://packages.python.org/pyudev
Group: Development/Python
BuildRoot: %{_tmppath}/%{name}-%{version}-buildroot
BuildArch: noarch
BuildRequires: python-setuptools
Provides: python-udev = %{version}-%{release}
Requires: udev
Suggests: python-qt4
Suggests: python-gobject

%description
pyudev is a Python binding to libudev, the hardware management library
and service found in modern linux systems.

%prep
%setup -q -n %{name}-%{version}

%build
python setup.py build

%install
rm -fr %buildroot
python setup.py install --root=%buildroot

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%py_puresitedir/*
