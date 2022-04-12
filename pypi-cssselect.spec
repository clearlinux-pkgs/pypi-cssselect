#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-cssselect
Version  : 1.1.0
Release  : 62
URL      : https://files.pythonhosted.org/packages/70/54/37630f6eb2c214cdee2ae56b7287394c8aa2f3bafb8b4eb8c3791aae7a14/cssselect-1.1.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/70/54/37630f6eb2c214cdee2ae56b7287394c8aa2f3bafb8b4eb8c3791aae7a14/cssselect-1.1.0.tar.gz
Summary  : cssselect parses CSS3 Selectors and translates them to XPath 1.0
Group    : Development/Tools
License  : BSD-3-Clause
Requires: pypi-cssselect-license = %{version}-%{release}
Requires: pypi-cssselect-python = %{version}-%{release}
Requires: pypi-cssselect-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pytest

%description
===================================
cssselect: CSS Selectors for Python
===================================

%package license
Summary: license components for the pypi-cssselect package.
Group: Default

%description license
license components for the pypi-cssselect package.


%package python
Summary: python components for the pypi-cssselect package.
Group: Default
Requires: pypi-cssselect-python3 = %{version}-%{release}

%description python
python components for the pypi-cssselect package.


%package python3
Summary: python3 components for the pypi-cssselect package.
Group: Default
Requires: python3-core
Provides: pypi(cssselect)

%description python3
python3 components for the pypi-cssselect package.


%prep
%setup -q -n cssselect-1.1.0
cd %{_builddir}/cssselect-1.1.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1649732857
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-cssselect
cp %{_builddir}/cssselect-1.1.0/LICENSE %{buildroot}/usr/share/package-licenses/pypi-cssselect/b44b1b116e90b52ab7da1109a774acce7b67cd35
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-cssselect/b44b1b116e90b52ab7da1109a774acce7b67cd35

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
