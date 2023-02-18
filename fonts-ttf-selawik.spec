Name:		fonts-ttf-selawik
Version:	1.0
Release:	1
Summary:	Selawik ttf fonts
License:	SIL Open Font License v1.10
Group:		System/Fonts/True type
Url:		https://github.com/Microsoft/Selawik
Source0:	%{name}-%version.tar.gz
BuildArch:	noarch

%description
Selawik is an open source replacement for Segoe UI.

%files
%dir %{_datadir}/fonts/TTF/selawik/
%{_datadir}/fonts/TTF/selawik/*

%prep
%setup -qn %{name}-%{version}/fonts/TTF/selawik/

%build
#

%install
mkdir -p %{buildroot}%{_datadir}/fonts/TTF/selawik
install -Dm 644  *.ttf  %{buildroot}%{_datadir}/fonts/TTF/selawik/
