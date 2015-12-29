Summary:	Udev helper for naming devices per BIOS names
Summary(pl.UTF-8):	Program pomocniczy udev do nazywania urządzeń zgodnie z nazwami BIOS-u
Name:		biosdevname
Version:	0.7.1
Release:	1
License:	GPL v2
Group:		Base
Source0:	http://linux.dell.com/files/biosdevname/%{name}-%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	86d1040754df774f7a58e8aa2ced2d78
URL:		http://linux.dell.com/files/biosdevname/
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake
BuildRequires:	pciutils-devel
BuildRequires:	zlib-devel
Requires:	udev-core
# SMBIOS only exists on these arches.  It's also likely that other
# arches don't expect the PCI bus to be sorted breadth-first, or of
# so, there haven't been any comments about that on LKML.
ExclusiveArch:	%{ix86} %{x8664} ia64
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
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) /sbin/%{name}
/lib/udev/rules.d/*-biosdevname.rules
%{_mandir}/man1/%{name}.1*
