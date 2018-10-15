Summary:	Udev helper for naming devices per BIOS names
Summary(pl.UTF-8):	Program pomocniczy udev do nazywania urządzeń zgodnie z nazwami BIOS-u
Name:		biosdevname
Version:	0.7.3
Release:	1
License:	GPL v2
Group:		Base
#Source0Download: https://github.com/dell/biosdevname/releases
#TODO: switch to named sources:
#Source0:	https://github.com/dell/biosdevname/archive/v%{version}/%{name}-%{version}.tar.gz
Source0:	https://github.com/dell/biosdevname/archive/v%{version}.tar.gz
# Source0-md5:	e7e76fd8e4b72e7364b10655a9e5f716
URL:		https://github.com/dell/biosdevname
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake
BuildRequires:	pciutils-devel
BuildRequires:	zlib-devel
Requires:	udev-core
# SMBIOS only exists on these arches.  It's also likely that other
# arches don't expect the PCI bus to be sorted breadth-first, or if
# so, there haven't been any comments about that on LKML.
ExclusiveArch:	%{ix86} %{x8664} x32
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
biosdevname in its simplest form takes a kernel device name as an
argument, and returns the BIOS-given name it "should" be. This is
necessary on systems where the BIOS name for a given device (e.g. the
label on the chassis is "Gb1") doesn't map directly and obviously to
the kernel name (e.g. eth0).

%description -l pl.UTF-8
biosdevname w najprostszej formie przyjmuje jako arugmnet nazwę
urządzenia wg jądra Linuksa i zwraca, jaką ono powinno mieć nazwę
nadaną przez BIOS. Jest to przydatne na systemach, gdzie BIOS-owa
nazwa danego urządzenia (np. etykieta na obudowie "Gb1") nie ma
bezpośredniego, oczywistego odwzorowania na nazwę wg jądra Linuksa
(np. eth0).

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--prefix=/ \
	--sbindir=/sbin
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install install-data \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README TODO
%attr(755,root,root) /sbin/biosdevname
/lib/udev/rules.d/*-biosdevname.rules
%{_mandir}/man1/biosdevname.1*
