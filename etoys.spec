Name:		etoys
Summary:	A media-rich model, game, and simulation construction kit and authoring tool
Version:	5.0.2408
Release:	4
URL:		https://squeakland.org/
License:	MIT/Apache
BuildArch:	noarch
Source:         %{name}-%{version}.tar.gz

Group:		Development/Other
Requires:	squeak-vm >= 3.10
Requires:	shared-mime-info
BuildRequires:	gettext

%description
Squeak Etoys was inspired by LOGO, PARC-Smalltalk, Hypercard,
and starLOGO. It is a media-rich authoring environment with a
simple powerful scripted object model for many kinds of objects
created by end-users that runs on many platforms, and is free
and open source. It includes graphics, images, text, particles,
presentations, web-pages, videos, sound and MIDI, etc.

%prep
%setup 

%build
./autogen.sh --prefix=%{_prefix}
make ROOT=%{buildroot} %{?_smp_mflags}

%install
[ -n "%{buildroot}" -a "%{buildroot}" != "/" ] && rm -rf "%{buildroot}"
make install-etoys ROOT=%{buildroot}

%clean
[ -n "%{buildroot}" -a "%{buildroot}" != "/" ] && rm -rf "%{buildroot}"

%post
%{_bindir}/update-mime-database %{_datadir}/mime &> /dev/null

%postun
%{_bindir}/update-mime-database %{_datadir}/mime &> /dev/null

%files
%{_datadir}/etoys
%{_bindir}/etoys
%{_datadir}/doc/etoys
%{_datadir}/mime/packages/etoys.xml


%changelog
* Sun Oct 10 2010 Paulo Andrade <pcpa@mandriva.com.br> 4.1.2388-1mdv2011.0
+ Revision: 584517
- Update to latest upstream release

* Sat Apr 03 2010 Aleksey Lim <alsroot@mandriva.org> 4.0.2340-1mdv2010.1
+ Revision: 530889
- Sucrose 0.88.0 release, switch to original squeak-vm

* Mon Oct 12 2009 Aleksey Lim <alsroot@mandriva.org> 4.0.2332-1mdv2010.0
+ Revision: 456969
- Push 4.0.2332

* Fri Sep 25 2009 Aleksey Lim <alsroot@mandriva.org> 4.0.2319-1mdv2010.0
+ Revision: 448671
- Update to 4.0.2319

* Fri Sep 18 2009 Aleksey Lim <alsroot@mandriva.org> 4.0.2318-1mdv2010.0
+ Revision: 444499
- Update to 4.0.2318
- Update to 4.0.2279

* Tue Aug 11 2009 Aleksey Lim <alsroot@mandriva.org> 4.0.2229-1mdv2010.0
+ Revision: 414751
- Initial commit

