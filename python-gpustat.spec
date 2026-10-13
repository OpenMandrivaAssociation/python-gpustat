Name:		python-gpustat
Version:	1.1.1
Release:	3
Source0:	https://files.pythonhosted.org/packages/source/g/gpustat/gpustat-%{version}.tar.gz
Summary:	An utility to monitor NVIDIA GPU status and usage
URL:		https://pypi.org/project/gpustat/
License:	MIT
Group:		System
BuildRequires:	pkgconfig(python3)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(setuptools-scm)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(wheel)
BuildSystem:	python
BuildArch:	noarch

%description
An utility to monitor NVIDIA GPU status and usage

%build -p
export SETUPTOOLS_SCM_PRETEND_VERSION="%{version}"

%prep
%autosetup -p1 -n gpustat-%{version}

%files
%{py_sitedir}/gpustat
%{py_sitedir}/gpustat-*.*-info
%{_bindir}/gpustat
