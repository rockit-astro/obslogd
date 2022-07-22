Name:      observatory-log-server
Version:   20220722
Release:   0
Url:       https://github.com/warwick-one-metre/obslogd
Summary:   Log database wrapper for the Warwick La Palma telescopes.
License:   GPL-3.0
Group:     Unspecified
BuildArch: noarch
Requires:  python3 python3-Pyro4 python3-warwick-observatory-common python3-PyMySQL mariadb

%description

%build
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_unitdir}

%{__install} %{_sourcedir}/obslogd %{buildroot}%{_bindir}
%{__install} %{_sourcedir}/obslogd.service %{buildroot}%{_unitdir}

%files
%defattr(0755,root,root,-)
%{_bindir}/obslogd
%defattr(-,root,root,-)
%{_unitdir}/obslogd.service

%changelog
