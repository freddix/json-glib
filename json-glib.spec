Summary:	Library providing serialization and deserialization support for the JSON format
Name:		json-glib
Version:	0.16.0
Release:	1
License:	LGPL v2
Group:		Development/Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/json-glib/0.16/%{name}-%{version}.tar.xz
# Source0-md5:	bbca11f32509d6eb3f54d24156e7312d
URL:		http://live.gnome.org/JsonGlib
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	docbook-dtd412-xml
BuildRequires:	glib-devel
BuildRequires:	gobject-introspection-devel
BuildRequires:	gtk-doc
BuildRequires:	libtool
BuildRequires:	pkg-config
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
JSON-GLib is a library providing serialization and deserialization
support for the JavaScript Object Notation (JSON) format described by
RFC 4627.

%package devel
Summary:	Header files for the json-glib library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for the json-glib library.

%package apidocs
Summary:	json-glib API documentation
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
json-glib API documentation.

%prep
%setup -q

%build
export LDFLAGS="%{rpmldflags} -Wl,-Bsymbolic-functions"
%{__gtkdocize}
%{__libtoolize}
%{__aclocal} -I build/autotools
%{__autoheader}
%{__autoconf}
%{__automake}
%configure \
	--with-html-dir=%{_gtkdocdir} \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang json-glib-1.0

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /usr/sbin/ldconfig
%postun	-p /usr/sbin/ldconfig

%files -f json-glib-1.0.lang
%defattr(644,root,root,755)
%doc ChangeLog NEWS
%attr(755,root,root) %ghost %{_libdir}/libjson-glib-1.0.so.?
%attr(755,root,root) %{_libdir}/libjson-glib-1.0.so.*.*.*
%{_libdir}/girepository-1.0/*.typelib

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libjson-glib-1.0.so
%{_includedir}/json-glib-1.0
%{_pkgconfigdir}/json-glib-1.0.pc
%{_datadir}/gir-1.0/Json-1.0.gir

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/json-glib

