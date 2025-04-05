Name:		python-gpustat
Version:	1.1.1
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/g/gpustat/gpustat-%{version}.tar.gz
Summary:	An utility to monitor NVIDIA GPU status and usage
URL:		https://pypi.org/project/gpustat/
License:	MIT
Group:		System
BuildRequires:	python
BuildRequires:	python-setuptools_scm
BuildSystem:	python
BuildArch:	noarch

%description
An utility to monitor NVIDIA GPU status and usage

%prep
%autosetup -p1 -n gpustat-%{version}

%files
%{py_sitedir}/gpustat
%{py_sitedir}/gpustat-*.*-info
%{_bindir}/gpustat
