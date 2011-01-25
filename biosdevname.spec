Summary:	Udev helper for naming devices per BIOS names
Name:		biosdevname
Version:	0.3.4
Release:	1
License:	GPL v2
Group:		Base
URL:		http://linux.dell.com/files/biosdevname
Source0:	http://linux.dell.com/files/biosdevname/permalink/%{name}-%{version}.tar.gz
# Source0-md5:	6dfc8802a51786b9b851c0b2705312c7
BuildRequires:	pciutils-devel
BuildRequires:	zlib-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
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

# don't build static
%{__sed} -i -e '/sbin_PROGRAMS/ s/src\/biosdevnameS//' src/Makefile.am

# path was supposed to be configurable
%{__sed} -i -e 's,/sbin/biosdevname,@sbindir@/biosdevname,' biosdevname.rules.in
%{__sed} -i -e '/AC_CONFIG_FILES/ s/Makefile/& biosdevname.rules/' configure.ac
%{__sed} -i -e '/INSTALL_DATA/ s/biosdevname.rules.in/biosdevname.rules/' Makefile.am

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--prefix=/ \
	--sbindir=/lib/udev \
	--sysconfdir=/lib \

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
%attr(755,root,root) /lib/udev/%{name}
/lib/udev/rules.d/*.rules
%{_mandir}/man1/%{name}.1*
