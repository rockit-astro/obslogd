Name:      rockit-obslog
Version:   %{_version}
Release:   1
Summary:   Log database daemon
Url:       https://github.com/rockit-astro/obslogd
License:   GPL-3.0
BuildArch: noarch

%description


%build
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_unitdir}
mkdir -p %{buildroot}%{_sysconfdir}/obslogd

%{__install} %{_sourcedir}/obslogd %{buildroot}%{_bindir}
%{__install} %{_sourcedir}/obslogd@.service %{buildroot}%{_unitdir}
%{__install} %{_sourcedir}/lapalma.json %{buildroot}%{_sysconfdir}/obslogd
%{__install} %{_sourcedir}/warwick.json %{buildroot}%{_sysconfdir}/obslogd

%package server
Summary:  Log database server
Group:    Unspecified
Requires: python3-rockit-common python3-PyMySQL mariadb
%description server

%files server
%defattr(0755,root,root,-)
%{_bindir}/obslogd
%defattr(0644,root,root,-)
%{_unitdir}/obslogd@.service

%package data-lapalma
Summary: Log data for La Palma telescopes
Group:   Unspecified
%description data-lapalma

%files data-lapalma
%defattr(0644,root,root,-)
%{_sysconfdir}/obslogd/lapalma.json

%package data-warwick
Summary: Log data for Windmill Hill observatory
Group:   Unspecified
%description data-warwick

%files data-warwick
%defattr(0644,root,root,-)
%{_sysconfdir}/obslogd/warwick.json

%changelog
