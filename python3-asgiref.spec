#
# Conditional build:
%bcond_without	tests	# unit tests

%define		module	asgiref
Summary:	ASGI specs, helper code, and adapters
Name:		python3-%{module}
Version:	3.8.1
Release:	1
License:	BSD
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/asgiref/
Source0:	https://files.pythonhosted.org/packages/source/a/asgiref/%{module}-%{version}.tar.gz
# Source0-md5:	fb2927e26ea34c97e0a4c89612e80562
URL:		https://pypi.org/project/asgiref/
BuildRequires:	python3-modules >= 1:3.2
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-pytest-asyncio
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python3-modules >= 1:3.2
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ASGI is a standard for Python asynchronous web apps and servers to
communicate with each other, and positioned as an asynchronous
successor to WSGI.
You can read more at https://asgi.readthedocs.io/en/latest/

This package includes ASGI base libraries, such as:

- Sync-to-async and async-to-sync function wrappers, asgiref.sync
- Server base classes, asgiref.server
- A WSGI-to-ASGI adapter, in asgiref.wsgi

%prep
%setup -q -n %{module}-%{version}

%build
%py3_build

%if %{with tests}
# use explicit plugins list for reliable builds (delete PYTEST_PLUGINS if empty)
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
PYTEST_PLUGINS=asyncio \
%{__python3} -m pytest tests
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.rst
%dir %{py3_sitescriptdir}/%{module}
%{py3_sitescriptdir}/%{module}/*.py
%{py3_sitescriptdir}/%{module}/py.typed
%{py3_sitescriptdir}/%{module}/__pycache__
%{py3_sitescriptdir}/%{module}-%{version}-py*.egg-info
