Name:      onemetre-obslog-server
Version:   1.0
Release:   0
Url:       https://github.com/warwick-one-metre/obslogd
Summary:   Log database wrapper for the Warwick one-metre telescope.
License:   GPL-3.0
Group:     Unspecified
BuildArch: noarch
Requires:  python3, python3-Pyro4, python3-warwickobservatory, %{?systemd_requires}
BuildRequires: systemd-rpm-macros

%description
Part of the observatory software for the Warwick one-meter telescope.

obslogd is a Pyro wrapper for the log database.

%build
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_unitdir}

%{__install} %{_sourcedir}/obslogd %{buildroot}%{_bindir}
%{__install} %{_sourcedir}/obslogd.service %{buildroot}%{_unitdir}

%pre
%service_add_pre obslogd.service

%post
%service_add_post obslogd.service
%fillup_and_insserv -f -y obslogd.service

%preun
%stop_on_removal obslogd.service
%service_del_preun obslogd.service

%postun
%restart_on_update obslogd.service
%service_del_postun obslogd.service

%files
%defattr(0755,root,root,-)
%{_bindir}/obslogd
%defattr(-,root,root,-)
%{_unitdir}/obslogd.service

%changelog
