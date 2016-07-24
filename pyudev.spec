Summary:	A libudev binding
Name:		pyudev
Version:	0.20.0
Release:	2
Source0:	https://github.com/pyudev/pyudev/archive/v%{version}.tar.gz
License:	MIT or X11
URL:		http://packages.python.org/pyudev
Group:		Development/Python
BuildArch:	noarch
BuildRequires:	python-setuptools
BuildRequires:	python2-setuptools
Requires:	udev
Suggests:	python-gi

%description
pyudev is a Python binding to libudev, the hardware management library
and service found in modern linux systems.

%package -n python2-pyudev
Summary:        A libudev binding
Group:          Development/Python
Requires:		udev

%description -n python2-pyudev
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
pushd python2
python2 setup.py build
popd

%install
pushd python3
python setup.py install --root=%{buildroot}
popd
pushd python2
python2 setup.py install --root=%{buildroot}
popd

%files
%dir %{py_puresitedir}/pyudev/
%{py_puresitedir}/pyudev/*
%dir %{py_puresitedir}/pyudev-*-py%{py_ver}.egg-info/
%{py_puresitedir}/pyudev-*-py%{py_ver}.egg-info/*

%files -n python2-pyudev
%dir %{py2_puresitedir}/pyudev/
%{py2_puresitedir}/pyudev/*
%dir %{py2_puresitedir}/pyudev-*-py%{py2_ver}.egg-info/
%{py2_puresitedir}/pyudev-*-py%{py2_ver}.egg-info/*
