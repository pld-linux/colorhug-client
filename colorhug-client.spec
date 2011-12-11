Summary:	Tools for the Hughski Colorimeter
Summary(pl.UTF-8):	Narzędzia do kolorymetrów Hughski
Name:		colorhug-client
Version:	0.1.2
Release:	1
License:	GPL v2
Group:		Applications/System
Source0:	http://people.freedesktop.org/~hughsient/releases/%{name}-%{version}.tar.xz
# Source0-md5:	9e5c3174e5820edca23a864d2194019d
URL:		http://hughski.com/
BuildRequires:	colord-devel >= 0.1.15
BuildRequires:	glib2-devel >= 1:2.28.0
BuildRequires:	gettext-devel >= 0.17
BuildRequires:	gtk+3-devel >= 3.0.0
BuildRequires:	intltool >= 0.35.0
BuildRequires:	lcms2-devel
BuildRequires:	libgusb-devel >= 0.1.2
BuildRequires:	libsoup-devel >= 2.4
BuildRequires:	pkgconfig
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
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
Requires:	colord >= 0.1.15
Requires:	gtk+3 >= 3.0.0

%description gui
The Hughski ColorHug colorimeter is a low cost open-source hardware
sensor used to calibrate screens.

This package includes the GUI client tools which allow the user to
access the sensor.

%description gui -l pl.UTF-8
Hughski ColorHug to niskobudżetowy kolorymetr z sensorem sprzętowym,
mający otwarte źródła, służący do kalibrowania ekranów.

Ten pakiet zawiera graficzne narzędzia klienckia pozwalające
operować sensorem.

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

# empty for now
#find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
# -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS NEWS README
%attr(755,root,root) %{_bindir}/colorhug
%attr(755,root,root) %{_bindir}/colorhug-inhx32-to-bin

%files gui
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/colorhug-ccmx
%attr(755,root,root) %{_bindir}/colorhug-flash
%attr(755,root,root) %{_bindir}/colorhug-gui
%{_datadir}/colorhug-client
%{_desktopdir}/colorhug-ccmx.desktop
%{_desktopdir}/colorhug-flash.desktop
%{_iconsdir}/hicolor/*/apps/colorhug.png
%{_iconsdir}/hicolor/scalable/apps/colorhug.svg
%{_mandir}/man1/colorhug-flash.1*

%files -n bash-completion-colorhug
%defattr(644,root,root,755)
/etc/bash_completion.d/colorhug-completion.bash
