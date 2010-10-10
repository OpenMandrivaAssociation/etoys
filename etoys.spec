%define name    etoys
%define version 4.1.2388
%define release 1
%define source  %{name}-%{version}

Name:		%{name}
Summary:	A media-rich model, game, and simulation construction kit and authoring tool
Version:	%{version}
Release:	%{release}
Vendor:		Squeakland Foundation
URL:		http://squeakland.org/
License:	MIT/Apache
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
# git clone git://dev.laptop.org/git/projects/etoys
# cd etoys
# git archive --format=tar --prefix=etoys-4.1.2388/ da36a993bede5edc64ff444f45fdc67dcc7865c8 | bzip2 > etoys-4.1.2388.tar.bz2
#
# Changes to spec to match Mandriva environment and build system
# Original spec (and changelog) in tarball or git checkout
Source:		%{source}.tar.bz2
Group:		Development/Languages
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
%setup -n %{source}

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
