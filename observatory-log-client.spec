Name:      observatory-log-client
Version:   20220722
Release:   0
Url:       https://github.com/warwick-one-metre/obslogd
Summary:   Log database helper for the Warwick La Palma telescopes.
License:   GPL-3.0
Group:     Unspecified
BuildArch: noarch
Requires:  python3 python3-warwick-observatory-common

%description

%build
mkdir -p %{buildroot}%{_bindir}
%{__install} %{_sourcedir}/obslog %{buildroot}%{_bindir}

%files
%defattr(0755,root,root,-)
%{_bindir}/obslog

%changelog
