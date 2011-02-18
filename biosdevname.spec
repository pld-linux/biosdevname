Summary:	Udev helper for naming devices per BIOS names
Name:		biosdevname
Version:	0.3.7
Release:	1
License:	GPL v2
Group:		Base
URL:		http://linux.dell.com/files/biosdevname
Source0:	http://linux.dell.com/files/biosdevname/permalink/%{name}-%{version}.tar.gz
# Source0-md5:	6b6de50f642bb6a2ec7d8c594b5320fc
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
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

%prep
%setup -q

%build
%{__libtoolize}
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
%doc README
%attr(755,root,root) /sbin/%{name}
/lib/udev/rules.d/*.rules
%{_mandir}/man1/%{name}.1*
