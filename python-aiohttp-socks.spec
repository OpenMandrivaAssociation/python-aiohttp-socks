%global module aiohttp-socks
%global srcname aiohttp_socks

Name:           python-%{module}
Version:        0.10.1
Release:        3
Summary:        SOCKS proxy connector for aiohttp

License:        ASL 2.0
URL:            https://github.com/romis2012/aiohttp-socks
Source:         https://files.pythonhosted.org/packages/source/a/%{srcname}/%{srcname}-%{version}.tar.gz

BuildRequires:	pkgconfig(python3)
BuildRequires:  python3-setuptools

BuildSystem:    python

BuildArch:      noarch

%description
SOCKS proxy connector for aiohttp. SOCKS4(a) and SOCKS5 are supported.

%files
%license LICENSE.txt
%doc README.md
%{python_sitelib}/%{srcname}/
%{python_sitelib}/%{srcname}-%version.dist-info/
#----------------------------------------------------------------------------

