Summary:	The PunkBuster update tool
Name:		pbweb
Version:	1.8
Release:	1
Vendor:		Even Balance, Inc.
License:	PB EULA
Group:		Applications/Games
Source0:	http://www.evenbalance.com/downloads/%{name}.x86
NoSource:	0
BuildRequires:	coreutils
URL:		http://www.evenbalance.com/
ExclusiveArch:	%{ix86}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Even Balance, Inc. spearheads the effort to fight cheating in the
online multiplayer gaming industry. Their flagship product,
PunkBuster(TM), spawned the Anti-Cheat movement in online gaming
several years ago and was the first system proven effective against
cheating in online games.

%prep
if [ "%(md5sum %{SOURCE0} | cut -d" " -f1)" != "967e3f2e05e8a6b3ec1b4183746b8b2e" ]; then
    echo "\nchecksum mismatch.\n"
    exit 1
fi

%install
rm -rf $RPM_BUILD_ROOT
install -D %{SOURCE0} $RPM_BUILD_ROOT%{_bindir}/pbweb.x86

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/pbweb.x86
