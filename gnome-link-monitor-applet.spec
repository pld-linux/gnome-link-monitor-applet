# TODO:
# - pl .desktop desc
#
%define		rname link-monitor-applet
Summary:	GNOME notification area link monitor
Summary(pl):	Monitor ³±cza dla obszaru powiadomieñ GNOME
Name:		gnome-link-monitor-applet
Version:	1.1
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://savannah.nongnu.org/download/link-monitor/%{rname}-%{version}.tar.gz
# Source0-md5:	ea9e59ad0991eebea85af0432bbbb93d
URL:		http://www.nongnu.org/link-monitor-applet/
BuildRequires:	autoconf
BuildRequires:	automake
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

%description -l pl
Link Monitor Applet to aplet panelu GNOME wy¶wietlaj±cy czas podró¿y
do jednego lub wiêkszej liczby hostów w postaci wykresu s³upkowego.
Mo¿liwo¶ci obejmuj± pe³n± obs³ugê ICMP i ICMPv6, konfigurowaln± skalê
i opó¼nienia oraz zgodno¶æ z HIG 2.0.

%prep
%setup -q -n %{rname}-%{version}

%build
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
install -d $RPM_BUILD_ROOT%{_datadir}/gnome/help

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1

mv $RPM_BUILD_ROOT%{_datadir}/help/* $RPM_BUILD_ROOT%{_datadir}/gnome/help

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
