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

%{__install} %{_sourcedir}/obslogd %{buildroot}%{_bindir}
%{__install} %{_sourcedir}/obslogd.service %{buildroot}%{_unitdir}

%package server
Summary:  Log database server
Group:    Unspecified
Requires: python3-rockit-common python3-PyMySQL mariadb
%description server

%files server
%defattr(0755,root,root,-)
%{_bindir}/obslogd
%defattr(0644,root,root,-)
%{_unitdir}/obslogd.service

%changelog
