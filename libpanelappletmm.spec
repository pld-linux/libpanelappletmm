Summary:	C++ wrappers for libpanel-applet library
Summary(pl.UTF-8):	Interfejsy C++ dla biblioteki libpanel-applet
Name:		libpanelappletmm
Version:	2.26.0
Release:	2
License:	LGPL v2+
Group:		X11/Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/libpanelappletmm/2.26/%{name}-%{version}.tar.bz2
# Source0-md5:	def2bc3298dd9ffc3838bf5245e5939e
URL:		http://www.gnome.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gconfmm-devel >= 2.6.1
BuildRequires:	gnome-panel-devel >= 2.26.0
BuildRequires:	gtkmm-devel >= 2.4.1
BuildRequires:	libgnomemm-devel >= 2.6.0
BuildRequires:	libtool
BuildRequires:	perl-base
BuildRequires:	pkgconfig
BuildRequires:	readline-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
C++ wrappers for libpanel-applet library.

%description -l pl.UTF-8
Interfejsy C++ dla biblioteki libpanel-applet.

%package devel
Summary:	Devel files for libpanelappletmm
Summary(pl.UTF-8):	Pliki nagłówkowe dla libpanelappletmm
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	gconfmm-devel >= 2.6.1
Requires:	gnome-panel-devel >= 2.26.0
Requires:	gtkmm-devel >= 2.4.1

%description devel
Devel files for libpanelappletmm.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla libpanelappletmm.

%package static
Summary:	libpanelappletmm static library
Summary(pl.UTF-8):	Biblioteka statyczna libpanelappletmm
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
libpanelappletmm static library.

%description static -l pl.UTF-8
Biblioteka statyczna libpanelappletmm.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal} -I scripts
%{__autoconf}
%{__automake}
%configure \
	--enable-static

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_libdir}/libpanelappletmm-2.6.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libpanelappletmm-2.6.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libpanelappletmm-2.6.so
%{_libdir}/libpanelappletmm-2.6.la
%{_libdir}/libpanelappletmm-2.6
%{_includedir}/libpanelappletmm-2.6
%{_pkgconfigdir}/libpanelappletmm-2.6.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libpanelappletmm-2.6.a
