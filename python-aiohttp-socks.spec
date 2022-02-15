%global module aiohttp-socks
%global srcname aiohttp_socks

Name:           python-%{module}
Version:        0.7.1
Release:        1
Summary:        SOCKS proxy connector for aiohttp

License:        ASL 2.0
URL:            https://github.com/romis2012/aiohttp-socks
Source:         https://files.pythonhosted.org/packages/source/a/%{srcname}/%{srcname}-%{version}.tar.gz

BuildRequires:	pkgconfig(python3)
BuildRequires:  python3-setuptools

BuildArch:      noarch

%description
SOCKS proxy connector for aiohttp. SOCKS4(a) and SOCKS5 are supported.

%files
%license LICENSE.txt
%doc README.md
%{python_sitelib}/%{srcname}/
%{python_sitelib}/%{srcname}-*.egg-info/

#----------------------------------------------------------------------------

%prep
%autosetup -n %{srcname}-%{version}
rm -vrf *.egg-info
sed -i -e 's/\r//' README.md

%build
%py_build

%install
%py_install
