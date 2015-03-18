Summary:	Tools for the Hughski Colorimeter
Summary(pl.UTF-8):	Narzędzia do kolorymetrów Hughski
Name:		colorhug-client
Version:	0.2.6
Release:	1
License:	GPL v2
Group:		Applications/System
Source0:	http://people.freedesktop.org/~hughsient/releases/%{name}-%{version}.tar.xz
# Source0-md5:	88561c9a89efbaec40f9628c13d458b3
Patch0:		%{name}-bashcomp.patch
URL:		http://hughski.com/
BuildRequires:	colord-devel >= 1.2.9
BuildRequires:	colord-gtk-devel >= 0.1.24
BuildRequires:	docbook-utils
BuildRequires:	gettext-tools >= 0.17
BuildRequires:	glib2-devel >= 1:2.31.10
BuildRequires:	gobject-introspection-devel >= 0.9.8
BuildRequires:	gtk+3-devel >= 3.11.2
BuildRequires:	intltool >= 0.50.0
BuildRequires:	lcms2-devel
BuildRequires:	libcanberra-gtk3-devel >= 0.10
BuildRequires:	libgusb-devel >= 0.2.2
BuildRequires:	libsoup-devel >= 2.4
BuildRequires:	pkgconfig
BuildRequires:	sqlite3-devel
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	colord-libs >= 1.2.9
Requires:	glib2 >= 1:2.31.10
Requires:	libgusb >= 0.2.2
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
Requires:	colord-gtk >= 0.1.24
Requires:	gtk+3 >= 3.11.2
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

%package -n bash-completion-colorhug
Summary:	Bash completion support for ColorHug console commands
Summary(pl.UTF-8):	Bashowe uzupełnianie składni dla poleceń terminalowych ColorHuga
Group:		Applications/Shells
Requires:	bash-completion >= 2.0
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description -n bash-completion-colorhug
Bash completion support for ColorHug console commands.

%description -n bash-completion-colorhug -l pl.UTF-8
Bashowe uzupełnianie składni dla poleceń terminalowych ColorHuga.

%prep
%setup -q
%patch0 -p1

%build
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-bash-completion=%{bash_compdir} \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

mv $RPM_BUILD_ROOT%{_localedir}/{cs_CZ,cs}
# replace de with more complete version from de_DE
%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/de
mv $RPM_BUILD_ROOT%{_localedir}/{de_DE,de}
mv $RPM_BUILD_ROOT%{_localedir}/{el_GR,el}
mv $RPM_BUILD_ROOT%{_localedir}/{es_ES,es}
mv $RPM_BUILD_ROOT%{_localedir}/{fr_FR,fr}
mv $RPM_BUILD_ROOT%{_localedir}/{it_IT,it}
mv $RPM_BUILD_ROOT%{_localedir}/{ja_JP,ja}
mv $RPM_BUILD_ROOT%{_localedir}/{nl_NL,nl}
# empty version of pl which already exists
%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/pl_PL
# just a copy of pt (only header differs)
%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/pt_PT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS NEWS README
%attr(755,root,root) %{_bindir}/colorhug
%attr(755,root,root) %{_bindir}/colorhug-cmd
%{_datadir}/glib-2.0/schemas/com.hughski.colorhug-client.gschema.xml
%{_mandir}/man1/colorhug-cmd.1*

%files gui
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/colorhug-backlight
%attr(755,root,root) %{_bindir}/colorhug-ccmx
%attr(755,root,root) %{_bindir}/colorhug-flash
%attr(755,root,root) %{_bindir}/colorhug-refresh
%{_datadir}/colorhug-client
%{_datadir}/appdata/com.hughski.ColorHug.Backlight.appdata.xml
%{_datadir}/appdata/com.hughski.ColorHug.CcmxLoader.appdata.xml
%{_datadir}/appdata/com.hughski.ColorHug.DisplayAnalysis.appdata.xml
%{_datadir}/appdata/com.hughski.ColorHug.FlashLoader.appdata.xml
%{_datadir}/help/C/colorhug-client
%{_desktopdir}/colorhug-docs.desktop
%{_desktopdir}/com.hughski.ColorHug.Backlight.desktop
%{_desktopdir}/com.hughski.ColorHug.CcmxLoader.desktop
%{_desktopdir}/com.hughski.ColorHug.DisplayAnalysis.desktop
%{_desktopdir}/com.hughski.ColorHug.FlashLoader.desktop
%{_iconsdir}/hicolor/*/apps/colorhug*.png
%{_iconsdir}/hicolor/*/apps/colorimeter-colorhug-inactive.png
%{_iconsdir}/hicolor/scalable/apps/colorhug.svg
%{_iconsdir}/hicolor/*x*/mimetypes/application-x-ccmx.png*
%{_iconsdir}/hicolor/scalable/mimetypes/application-x-ccmx.svg
%{_mandir}/man1/colorhug-backlight.1*
%{_mandir}/man1/colorhug-ccmx.1*
%{_mandir}/man1/colorhug-flash.1*
%{_mandir}/man1/colorhug-refresh.1*

%files -n bash-completion-colorhug
%defattr(644,root,root,755)
%{bash_compdir}/colorhug-cmd
