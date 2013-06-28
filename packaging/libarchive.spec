Name:           libarchive
Version:        2.8.3
Release:        1
License:        BSD
Summary:        A library for handling streaming archive formats
Url:            http://code.google.com/p/libarchive/
Group:          System/Libraries
Source0:        http://libarchive.googlecode.com/files/libarchive-%{version}.tar.gz
Source1001: 	libarchive.manifest
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  bison
BuildRequires:  bzip2-devel
BuildRequires:  libacl-devel
BuildRequires:  libattr-devel
BuildRequires:  libtool
BuildRequires:  zlib-devel
BuildRequires:  pkgconfig(ext2fs)
BuildRequires:  pkgconfig(liblzma)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(openssl)

%description
Libarchive is a programming library that can create and read several different
streaming archive formats, including most popular tar variants, several cpio
formats, and both BSD and GNU ar variants. It can also write shar archives and
read ISO9660 CDROM images and ZIP archives.

%package devel
Summary:        Development files for %{name}
Group:          Development/Libraries
Requires:       %{name} = %{version}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q
cp %{SOURCE1001} .


%build
%configure --disable-static \
    --disable-bsdtar \
    --disable-bsdcpio

make %{?_smp_mflags}

%install
%make_install

find %{buildroot} -name cpio.5 -exec rm -f {} ';'
find %{buildroot} -name mtree.5 -exec rm -f {} ';'
find %{buildroot} -name tar.5 -exec rm -f {} ';'

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%manifest %{name}.manifest
%license COPYING
%defattr(-,root,root,-)
%{_libdir}/*.so.*


%files devel
%manifest %{name}.manifest
%defattr(-,root,root,-)
%{_includedir}/*
%{_mandir}/*/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*

