%{?python_enable_dependency_generator}
%global pypi_name aiohttp-socks
%global srcname aiohttp_socks
%global _description \
SOCKS proxy connector for aiohttp. SOCKS4(a) and SOCKS5 are supported.

Name:           python-%{pypi_name}
Version:        0.3.7
Release:        1
Summary:        SOCKS proxy connector for aiohttp

License:        ASL 2.0
URL:            https://pypi.org/project/aiohttp-socks/
Source:         https://files.pythonhosted.org/packages/51/da/f9bd57339175ec9253dbeba47d6b012a46f7165a6ee04b3df60799180809/aiohttp_socks-0.3.7.tar.gz

BuildArch:      noarch

%description %{_description}

%package -n python3-%{pypi_name}
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
Provides:	python-%{pypi_name} = %{EVRD}

%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name} %{_description}

Python 3 version.

%prep
%autosetup -n %{srcname}-%{version}
rm -vrf *.egg-info
sed -i -e 's/\r//' README.md

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%license LICENSE.txt
%doc README.md
%{python3_sitelib}/%{srcname}/
%{python3_sitelib}/%{srcname}-*.egg-info/
