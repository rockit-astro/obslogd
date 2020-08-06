Name:      observatory-log-server
Version:   2.1.1
Release:   0
Url:       https://github.com/warwick-one-metre/obslogd
Summary:   Log database wrapper for the Warwick one-metre telescope.
License:   GPL-3.0
Group:     Unspecified
BuildArch: noarch
Requires:  python3, python3-Pyro4 python3-warwick-observatory-common, python3-pymysql, mariadb, %{?systemd_requires}

%description
Part of the observatory software for the Warwick one-meter telescope.

obslogd is a Pyro wrapper for the log database.

%build
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_unitdir}

%{__install} %{_sourcedir}/obslogd %{buildroot}%{_bindir}
%{__install} %{_sourcedir}/obslogd.service %{buildroot}%{_unitdir}

%post
%systemd_post obslogd.service

%preun
%systemd_preun obslogd.service

%postun
%systemd_postun_with_restart obslogd.service

%files
%defattr(0755,root,root,-)
%{_bindir}/obslogd
%defattr(-,root,root,-)
%{_unitdir}/obslogd.service

%changelog
