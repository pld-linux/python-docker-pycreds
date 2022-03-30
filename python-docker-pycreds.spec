#
# Conditional build:
%bcond_without	doc	# don't build doc
%bcond_with	tests	# do not perform "make test"
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

%define 	module		dockerpycreds
%define 	egg_name	docker_pycreds
%define		pypi_name	docker-pycreds
Summary:	Python bindings for the docker credentials store API
Name:		python-%{pypi_name}
Version:	0.4.0
Release:	8
License:	Apache v2.0
Group:		Libraries/Python
Source0:	https://files.pythonhosted.org/packages/source/d/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
# Source0-md5:	322f570cea6b4661c6ac335683988e18
URL:		https://github.com/shin-/dockerpy-creds
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with python2}
BuildRequires:	python-modules
BuildRequires:	python-setuptools
%if %{with tests}
BuildRequires:	python-flake8 = 2.4.1
BuildRequires:	python-pytest = 3.0.2
BuildRequires:	python-pytest-cov = 2.3.1
%endif
%endif
%if %{with python3}
BuildRequires:	python3-modules
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-flake8 = 2.4.1
BuildRequires:	python3-pytest = 3.0.2
BuildRequires:	python3-pytest-cov = 2.3.1
%endif
%endif
Suggests:	docker-credential-helpers >= 0.4.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Python 2 bindings for the docker credentials store API

%package -n python3-%{pypi_name}
Summary:	Python bindings for the docker credentials store API
Group:		Libraries/Python
Suggests:	docker-credential-helpers >= 0.4.0

%description -n python3-%{pypi_name}
Python 3 bindings for the docker credentials store API

%prep
%setup -q -n %{pypi_name}-%{version}

# Remove bundled egg-info
%{__rm} -r %{egg_name}.egg-info

%build
%if %{with python2}
%py_build %{?with_tests:test}
%endif

%if %{with python3}
%py3_build %{?with_tests:test}
%endif

%install
rm -rf $RPM_BUILD_ROOT
%if %{with python2}
%py_install
%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc README.md
%{py_sitescriptdir}/%{module}
%{py_sitescriptdir}/%{egg_name}-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-%{pypi_name}
%defattr(644,root,root,755)
%doc README.md
%{py3_sitescriptdir}/%{module}
%{py3_sitescriptdir}/%{egg_name}-%{version}-py*.egg-info
%endif

