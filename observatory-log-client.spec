Name:      observatory-log-client
Version:   2.0
Release:   0
Url:       https://github.com/warwick-one-metre/obslogd
Summary:   Log database helper for the Warwick one-metre telescope.
License:   GPL-3.0
Group:     Unspecified
BuildArch: noarch
%if 0%{?suse_version}
Requires:  python3, python3-warwickobservatory
%endif
%if 0%{?centos_ver}
Requires:  python34, python34-warwick-observatory-common
%endif

%description
Part of the observatory software for the Warwick one-meter telescope.

obslog is a commandline utility for writing messages into the log database.

%build
mkdir -p %{buildroot}%{_bindir}
%{__install} %{_sourcedir}/obslog %{buildroot}%{_bindir}

%files
%defattr(0755,root,root,-)
%{_bindir}/obslog

%changelog
