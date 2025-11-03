#
# Conditional build:
%bcond_without	tests	# unit tests

%define		module	asgiref
Summary:	ASGI specs, helper code, and adapters
Summary(pl.UTF-8):	Specyfikacja ASGI, kod pomocniczy i adaptery
Name:		python3-%{module}
Version:	3.10.0
Release:	1
License:	BSD
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/asgiref/
Source0:	https://files.pythonhosted.org/packages/source/a/asgiref/%{module}-%{version}.tar.gz
# Source0-md5:	6799fce19314e0aaeb789a6d0f6d45fa
URL:		https://pypi.org/project/asgiref/
BuildRequires:	python3-modules >= 1:3.9
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-pytest
BuildRequires:	python3-pytest-asyncio
%if "%{_ver_lt %{py3_ver} 3.11}" == "1"
%endif
BuildRequires:	python3-typing_extensions >= 4
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.749
Requires:	python3-modules >= 1:3.9
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ASGI is a standard for Python asynchronous web apps and servers to
communicate with each other, and positioned as an asynchronous
successor to WSGI. You can read more at
<https://asgi.readthedocs.io/en/latest/>.

This package includes ASGI base libraries, such as:
- Sync-to-async and async-to-sync function wrappers, asgiref.sync
- Server base classes, asgiref.server
- A WSGI-to-ASGI adapter, in asgiref.wsgi

%description -l pl.UTF-8
ASGI to standard dla asynchronicznych aplikacji WWW i serwerów w
Pythonie, komunikujących się ze sobą i uważanych za asynchronicznych
następców WSGI. Więcej na ten temat można się dowiedzieć pod
<https://asgi.readthedocs.io/en/latest/>.

Ten pakiet zawiera biblioteki podstawowe ASGI, takie jak:
- asgiref.sync - funkcje obudowujące sync-do-async i async-do-sync
- asgiref.server - klasy bazowe serwera
- asgiref.wsgi - adapter WSGI-do-ASGI

%prep
%setup -q -n %{module}-%{version}

%build
%py3_build

%if %{with tests}
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
%doc LICENSE README.rst
%dir %{py3_sitescriptdir}/%{module}
%{py3_sitescriptdir}/%{module}/*.py
%{py3_sitescriptdir}/%{module}/py.typed
%{py3_sitescriptdir}/%{module}/__pycache__
%{py3_sitescriptdir}/%{module}-%{version}-py*.egg-info
