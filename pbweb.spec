Summary:	The PunkBuster update tool
Summary(pl.UTF-8):	Narzędzie do aktualizacji PunkBustera
Name:		pbweb
Version:	2.2
Release:	1
Vendor:		Even Balance, Inc.
License:	PB EULA
Group:		Applications/Games
Source0:	http://www.evenbalance.com/downloads/%{name}.x86
# NoSource0-md5:	74964cd7c3f107a66f7380e95d019669
NoSource:	0
URL:		http://www.evenbalance.com/
ExclusiveArch:	%{ix86}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Even Balance, Inc. spearheads the effort to fight cheating in the
online multiplayer gaming industry. Their flagship product,
PunkBuster(TM), spawned the Anti-Cheat movement in online gaming
several years ago and was the first system proven effective against
cheating in online games.

%description -l pl.UTF-8
Even Balance, Inc. przoduje w wysiłkach na rzecz walki z oszustami w
przemyśle gier online dla wielu graczy. Ich flagowy produkt,
PunkBuster(TM), zrodził kilka lat temu ruch przeciwdziałania oszustom
w dziedzinie gier online i okazał się pierwszym efektywnym systemem
przeciwko oszustwom w grach online.

%prep
if [ "%(md5sum %{SOURCE0} | cut -d" " -f1)" != "74964cd7c3f107a66f7380e95d019669" ]; then
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
