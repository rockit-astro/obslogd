Name:      observatory-log-server
Version:   2.0
Release:   0
Url:       https://github.com/warwick-one-metre/obslogd
Summary:   Log database wrapper for the Warwick one-metre telescope.
License:   GPL-3.0
Group:     Unspecified
BuildArch: noarch
%if 0%{?suse_version}
Requires:  python3, python3-Pyro4, python3-warwickobservatory, python3-PyMySQL, mysql, %{?systemd_requires}
BuildRequires: systemd-rpm-macros
%endif
%if 0%{?centos_ver}
Requires:  python34, python34-Pyro4 python34-warwick-observatory-common, python34-PyMySQL, mariadb, %{?systemd_requires}
%endif

%description
Part of the observatory software for the Warwick one-meter telescope.

obslogd is a Pyro wrapper for the log database.

%build
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_unitdir}

%{__install} %{_sourcedir}/obslogd %{buildroot}%{_bindir}
%{__install} %{_sourcedir}/obslogd.service %{buildroot}%{_unitdir}

%pre
%if 0%{?suse_version}
%service_add_pre obslogd.service
%endif

%post
%if 0%{?suse_version}
%service_add_post obslogd.service
%endif
%if 0%{?centos_ver}
%systemd_post obslogd.service
%endif

%preun
%if 0%{?suse_version}
%stop_on_removal obslogd.service
%service_del_preun obslogd.service
%endif
%if 0%{?centos}
%systemd_preun obslogd.service
%endif

%postun
%if 0%{?suse_version}
%restart_on_update obslogd.service
%service_del_postun obslogd.service
%endif
%if 0%{?centos}
%systemd_postun_with_restart obslogd.service
%endif

%files
%defattr(0755,root,root,-)
%{_bindir}/obslogd
%defattr(-,root,root,-)
%{_unitdir}/obslogd.service

%changelog
