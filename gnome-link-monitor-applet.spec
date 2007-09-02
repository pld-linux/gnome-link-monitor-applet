# TODO:
# - pl .desktop desc
#
%define		rname link-monitor-applet
Summary:	GNOME notification area link monitor
Summary(pl.UTF-8):	Monitor łącza dla obszaru powiadomień GNOME
Name:		gnome-link-monitor-applet
Version:	2.2
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://savannah.nongnu.org/download/link-monitor/%{rname}-%{version}.tar.bz2
# Source0-md5:	7b1be343d8809b244f7b26565caf23fb
URL:		http://www.nongnu.org/link-monitor-applet/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	intltool
BuildRequires:	libgnomeui-devel >= 2.4.0
BuildRequires:	libtool
BuildRequires:	pkgconfig
Requires(post):	GConf2 >= 2.4.0
Requires(post):	scrollkeeper
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Link Monitor Applet is a GNOME panel applet displaying the round-trip
time to one or more hosts in a bar graph. Features include full ICMP
and ICMPv6 support, configurable scale and delays, and HIG 2.0
compliance.

%description -l pl.UTF-8
Link Monitor Applet to aplet panelu GNOME wyświetlający czas podróży
do jednego lub większej liczby hostów w postaci wykresu słupkowego.
Możliwości obejmują pełną obsługę ICMP i ICMPv6, konfigurowalną skalę
i opóźnienia oraz zgodność z HIG 2.0.

%prep
%setup -q -n %{rname}-%{version}

%build
%{__intltoolize}
%{__aclocal} -I m4
%{__autoheader}
%{__automake}
%{__autoconf}
%configure \
	--disable-schemas-install \
	--enable-maintainer-mode

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1

%find_lang %{rname} --all-name --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post
scrollkeeper-update
%gconf_schema_install

%postun	-p /usr/bin/scrollkeeper-update

%files -f %{rname}.lang
%defattr(644,root,root,755)
%doc NEWS README
%attr(4754,root,adm) %{_libdir}/%{rname}
%{_sysconfdir}/gconf/schemas/*
%{_datadir}/%{rname}
%{_pixmapsdir}/*
%{_omf_dest_dir}/%{rname}
%{_libdir}/bonobo/servers/*
%{_datadir}/gnome-2.0/ui/GNOME_LinkMonitorApplet.xml
%{_datadir}/gnome/help/%{rname}/C/*
