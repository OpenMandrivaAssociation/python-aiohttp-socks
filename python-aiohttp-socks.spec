%define module aiohttp-socks
%define oname aiohttp_socks

Name:		python-aiohttp-socks
Version:	0.11.0
Release:	1
Summary:	SOCKS proxy connector for aiohttp
License:	Apache-2.0
URL:		https://github.com/romis2012/aiohttp-socks
Source:		https://files.pythonhosted.org/packages/source/a/%{oname}/%{oname}-%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildSystem:	python
BuildArch:		noarch

BuildRequires:	pkgconfig(python3)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(wheel)

%description
SOCKS proxy connector for aiohttp. SOCKS4(a) and SOCKS5 are supported.

%files
%license LICENSE.txt
%doc README.md
%{python_sitelib}/%{oname}/
%{python_sitelib}/%{oname}-%version.dist-info/
