#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-cssselect
Version  : 1.2.0
Release  : 73
URL      : https://files.pythonhosted.org/packages/d1/91/d51202cc41fbfca7fa332f43a5adac4b253962588c7cc5a54824b019081c/cssselect-1.2.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/d1/91/d51202cc41fbfca7fa332f43a5adac4b253962588c7cc5a54824b019081c/cssselect-1.2.0.tar.gz
Summary  : cssselect parses CSS3 Selectors and translates them to XPath 1.0
Group    : Development/Tools
License  : BSD-3-Clause
Requires: pypi-cssselect-license = %{version}-%{release}
Requires: pypi-cssselect-python = %{version}-%{release}
Requires: pypi-cssselect-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi-pytest
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

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
%setup -q -n cssselect-1.2.0
cd %{_builddir}/cssselect-1.2.0
pushd ..
cp -a cssselect-1.2.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1672265982
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz "
export FCFLAGS="$FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz "
export FFLAGS="$FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz "
export CXXFLAGS="$CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-cssselect
cp %{_builddir}/cssselect-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/pypi-cssselect/b44b1b116e90b52ab7da1109a774acce7b67cd35 || :
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pip install --root=%{buildroot}-v3 --no-deps --ignore-installed dist/*.whl
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

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
