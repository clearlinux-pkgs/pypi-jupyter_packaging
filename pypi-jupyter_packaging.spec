#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-jupyter_packaging
Version  : 0.12.3
Release  : 45
URL      : https://files.pythonhosted.org/packages/25/c5/b0e154e6403c6790bb1e66acddf9787296a8196f5b14f4bb9e4c92b6734e/jupyter_packaging-0.12.3.tar.gz
Source0  : https://files.pythonhosted.org/packages/25/c5/b0e154e6403c6790bb1e66acddf9787296a8196f5b14f4bb9e4c92b6734e/jupyter_packaging-0.12.3.tar.gz
Summary  : Jupyter Packaging Utilities.
Group    : Development/Tools
License  : BSD-3-Clause
Requires: pypi-jupyter_packaging-license = %{version}-%{release}
Requires: pypi-jupyter_packaging-python = %{version}-%{release}
Requires: pypi-jupyter_packaging-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(hatchling)

%description
# Jupyter Packaging
Tools to help build and install Jupyter Python packages that require a pre-build step that may include JavaScript build steps.

%package license
Summary: license components for the pypi-jupyter_packaging package.
Group: Default

%description license
license components for the pypi-jupyter_packaging package.


%package python
Summary: python components for the pypi-jupyter_packaging package.
Group: Default
Requires: pypi-jupyter_packaging-python3 = %{version}-%{release}

%description python
python components for the pypi-jupyter_packaging package.


%package python3
Summary: python3 components for the pypi-jupyter_packaging package.
Group: Default
Requires: python3-core
Provides: pypi(jupyter_packaging)
Requires: pypi(deprecation)
Requires: pypi(packaging)
Requires: pypi(setuptools)
Requires: pypi(tomlkit)
Requires: pypi(wheel)

%description python3
python3 components for the pypi-jupyter_packaging package.


%prep
%setup -q -n jupyter_packaging-0.12.3
cd %{_builddir}/jupyter_packaging-0.12.3
pushd ..
cp -a jupyter_packaging-0.12.3 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1666707135
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -msse2avx"
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -msse2avx "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-jupyter_packaging
cp %{_builddir}/jupyter_packaging-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/pypi-jupyter_packaging/7a88a926691422ae250d28e9a8214e9e40469383 || :
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
## Remove excluded files
rm -f %{buildroot}*/usr/lib/python3.11/site-packages/tests/*.py
rm -f %{buildroot}*/usr/lib/python3.11/site-packages/tests/__pycache__/*
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-jupyter_packaging/7a88a926691422ae250d28e9a8214e9e40469383

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
