Name: smb-conf-usershares
Version: 0.1
Release: alt1
Summary: Control for samba usershare option in section global
Group: Other

License: GPLv3+

Source0: %name-%version.tar.gz

Requires: bash local-policy
BuildArch: noarch

%description
Control for samba, in which comments in the global section are turned on and off

%prep
%setup -q

%build

%install
mkdir -p %_controldir

install -m 0755 %name %_sysconfdir/%name

%files
%_sysconfdir/%name

%changelog
* Tue Oct 11 2022 Valentin Sokolov  <sokolovvaly.158@gmail.com> 0.1-alt1
- First smb-conf-usershare package
