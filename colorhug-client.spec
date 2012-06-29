Summary:	Tools for the Hughski Colorimeter
Summary(pl.UTF-8):	Narzędzia do kolorymetrów Hughski
Name:		colorhug-client
Version:	0.1.10
Release:	2
License:	GPL v2
Group:		Applications/System
Source0:	http://people.freedesktop.org/~hughsient/releases/%{name}-%{version}.tar.xz
# Source0-md5:	ec1914a8cd5754e17093c1973158e345
URL:		http://hughski.com/
BuildRequires:	colord-devel >= 0.1.20
BuildRequires:	gettext-devel >= 0.17
BuildRequires:	glib2-devel >= 1:2.28.0
BuildRequires:	gobject-introspection-devel >= 0.9.8
BuildRequires:	gtk+3-devel >= 3.0.0
BuildRequires:	intltool >= 0.35.0
BuildRequires:	lcms2-devel
BuildRequires:	libcanberra-gtk3-devel >= 0.10
BuildRequires:	libgusb-devel >= 0.1.2
BuildRequires:	libsoup-devel >= 2.4
BuildRequires:	pkgconfig
BuildRequires:	sqlite3-devel
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	%{name}-libs = %{version}-%{release}
Requires:	glib2 >= 1:2.28.0
Requires:	libgusb >= 0.1.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# why programs are installed to libexecdir in the first place?
%define		_libexecdir	%{_bindir}

%description
The Hughski ColorHug colorimeter is a low cost open-source hardware
sensor used to calibrate screens.

This package includes the client tools which allows the user to
upgrade the firmware on the sensor or to access the sensor from
command line scripts.

%description -l pl.UTF-8
Hughski ColorHug to niskobudżetowy kolorymetr z sensorem sprzętowym,
mający otwarte źródła, służący do kalibrowania ekranów.

Ten pakiet zawiera narzędzia klienckie pozwalające uaktualniać
firmware sensora oraz operować sensorem z linii poleceń.

%package gui
Summary:	GUI tools for the Hughski Colorimeter
Summary(pl.UTF-8):	Graficzne narzędzia do kolorymetrów Hughski
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}
Requires:	colord >= 0.1.20
Requires:	gtk+3 >= 3.0.0
Requires:	libcanberra-gtk3 >= 0.10

%description gui
The Hughski ColorHug colorimeter is a low cost open-source hardware
sensor used to calibrate screens.

This package includes the GUI client tools which allow the user to
access the sensor.

%description gui -l pl.UTF-8
Hughski ColorHug to niskobudżetowy kolorymetr z sensorem sprzętowym,
mający otwarte źródła, służący do kalibrowania ekranów.

Ten pakiet zawiera graficzne narzędzia klienckia pozwalające operować
sensorem.

%package libs
Summary:	Library for Hughski Colorimeter
Summary(pl.UTF-8):	Biblioteka do kolorymetrów Hughski
Group:		Libraries

%description libs
Library for Hughski Colorimeter.

%description libs -l pl.UTF-8
Biblioteka do kolorymetrów Hughski.

%package devel
Summary:	Header files for ColorHug library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki ColorHug
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}

%description devel
Header files for ColorHug library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki ColorHug.

%package static
Summary:	Static ColorHug library
Summary(pl.UTF-8):	Statyczna biblioteka ColorHug
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static ColorHug library.

%description static -l pl.UTF-8
Statyczna biblioteka ColorHug.

%package -n bash-completion-colorhug
Summary:	Bash completion support for ColorHug console commands
Summary(pl.UTF-8):	Bashowe uzupełnianie składni dla poleceń terminalowych ColorHuga
Group:		Applications/Shells
Requires:	bash-completion

%description -n bash-completion-colorhug
Bash completion support for ColorHug console commands.

%description -n bash-completion-colorhug -l pl.UTF-8
Bashowe uzupełnianie składni dla poleceń terminalowych ColorHuga.

%prep
%setup -q

%build
%configure \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# remove empty de locale
%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/de
mv $RPM_BUILD_ROOT%{_localedir}/{cs_CZ,cs}
mv $RPM_BUILD_ROOT%{_localedir}/{de_DE,de}
mv $RPM_BUILD_ROOT%{_localedir}/{el_GR,el}
mv $RPM_BUILD_ROOT%{_localedir}/{es_ES,es}
mv $RPM_BUILD_ROOT%{_localedir}/{fr_FR,fr}
mv $RPM_BUILD_ROOT%{_localedir}/{it_IT,it}
mv $RPM_BUILD_ROOT%{_localedir}/{ja_JP,ja}
mv $RPM_BUILD_ROOT%{_localedir}/{nl_NL,nl}
mv $RPM_BUILD_ROOT%{_localedir}/{pt_PT,pt}
# empty version of pl which already exists
%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/pl_PL
# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libcolorhug.la

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS NEWS README
%attr(755,root,root) %{_bindir}/colorhug
%attr(755,root,root) %{_bindir}/colorhug-cmd
%attr(755,root,root) %{_bindir}/colorhug-inhx32-to-bin
%{_datadir}/glib-2.0/schemas/com.hughski.colorhug-client.gschema.xml
%{_mandir}/man1/colorhug-cmd.1*

%files gui
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/colorhug-ccmx
%attr(755,root,root) %{_bindir}/colorhug-flash
%{_datadir}/colorhug-client
%{_desktopdir}/colorhug-ccmx.desktop
%{_desktopdir}/colorhug-flash.desktop
%{_iconsdir}/hicolor/*/apps/colorhug*.png
%{_iconsdir}/hicolor/*/apps/colorimeter-colorhug-inactive.png
%{_iconsdir}/hicolor/scalable/apps/colorhug.svg
%{_iconsdir}/hicolor/*/mimetypes/application-x-ccmx.png
%{_iconsdir}/hicolor/scalable/mimetypes/application-x-ccmx.svg
%{_mandir}/man1/colorhug-flash.1*
%{_mandir}/man1/colorhug-ccmx.1*

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libcolorhug.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libcolorhug.so.1
%{_libdir}/girepository-1.0/ColorHug-1.0.typelib

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libcolorhug.so
%{_includedir}/libcolorhug
%{_datadir}/gir-1.0/ColorHug-1.0.gir
%{_pkgconfigdir}/colorhug.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libcolorhug.a

%files -n bash-completion-colorhug
%defattr(644,root,root,755)
/etc/bash_completion.d/colorhug-cmd-completion.bash
