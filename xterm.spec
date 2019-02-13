Summary:	Terminal emulator for X
Summary(pl.UTF-8):	Emulator terminala dla X
Name:		xterm
Version:	344
Release:	1
License:	MIT
Group:		X11/Applications
Source0:	ftp://ftp.invisible-island.net/xterm/%{name}-%{version}.tgz
# Source0-md5:	dc3c0f7033fe4d605db21e239925d3e4
Source1:	XTerm.ad-pl
Source2:	%{name}.desktop
Source3:	%{name}.png
Source4:	%{name}.1x.ko
Patch0:		%{name}-tinfo.patch
URL:		http://invisible-island.net/xterm/
BuildRequires:	fontconfig-devel
BuildRequires:	libutempter-devel
BuildRequires:	ncurses-devel
BuildRequires:	pkgconfig
BuildRequires:	xorg-lib-libICE-devel
BuildRequires:	xorg-lib-libXaw-devel
BuildRequires:	xorg-lib-libXft-devel
BuildRequires:	xorg-lib-libXinerama-devel
BuildRequires:	xorg-lib-libXmu-devel
BuildRequires:	xorg-lib-libXpm-devel
BuildRequires:	xorg-lib-libXt-devel >= 1.0.0
Requires:	xorg-lib-libXt >= 1.0.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The xterm program is a terminal emulator for the X Window System. It
provides DEC VT102/VT220 (VTxxx) and Tektronix 4014 compatible
terminals for programs that cannot use the window system directly.

This version implements ISO/ANSI colors using the "new" color model
(i.e., background color erase). It also implements most of the control
sequences for VT220.

%description -l pl.UTF-8
Program xterm to emulator terminala dla X Window System. Udostępnia
terminale zgodne z DEC VT102/VT220 (VTxxx) oraz Tektronix 4014 dla
programów nie potrafiących używać bezpośrednio systemu okien.

Ta wersja implementuje kolory ISO/ANSI przy użyciu "nowego" modelu
kolorów (tzn. usuwania kolorem tła). Implementuje także większość
sekwencji sterujących VT220.

%prep
%setup -q
%patch0 -p1

%build
# don't run autoconf, modified version of autoconf is required
CPPFLAGS="-I/usr/include/ncurses %{rpmcppflags}"
# consider --enable-readline-mouse --enable-dabbrev --enable-screen-dumps --enable-regis-graphics
%configure \
	--enable-256-color \
	--enable-exec-xterm \
	--enable-wide-chars \
	--enable-sixel-graphics \
	--with-app-defaults=%{_datadir}/X11/app-defaults \
	--with-utempter

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

echo '.so xterm.1' > $RPM_BUILD_ROOT%{_mandir}/man1/uxterm.1

install -D xterm.appdata.xml $RPM_BUILD_ROOT%{_datadir}/appdata/xterm.appdata.xml

install -D %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/X11/pl/app-defaults/XTerm
install -D %{SOURCE2} $RPM_BUILD_ROOT%{_desktopdir}/xterm.desktop
install -D %{SOURCE3} $RPM_BUILD_ROOT%{_pixmapsdir}/xterm.png
install -D %{SOURCE4} $RPM_BUILD_ROOT%{_mandir}/ko/man1/xterm.1
echo '.so xterm.1' > $RPM_BUILD_ROOT%{_mandir}/ko/man1/uxterm.1

# cleanup unpackaged icons
%{__rm} $RPM_BUILD_ROOT%{_pixmapsdir}/{filled-xterm,mini.xterm,xterm-color,xterm}_*x*.xpm

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README README.i18n xterm.log.html
%attr(755,root,root) %{_bindir}/resize
%attr(755,root,root) %{_bindir}/xterm
%attr(755,root,root) %{_bindir}/uxterm
%attr(755,root,root) %{_bindir}/koi8rxterm
%{_datadir}/X11/app-defaults/UXTerm
%{_datadir}/X11/app-defaults/UXTerm-color
%{_datadir}/X11/app-defaults/XTerm
%{_datadir}/X11/app-defaults/XTerm-color
%{_datadir}/X11/app-defaults/KOI8RXTerm
%{_datadir}/X11/app-defaults/KOI8RXTerm-color
%lang(pl) %{_datadir}/X11/pl/app-defaults/XTerm
%{_datadir}/appdata/xterm.appdata.xml
%{_desktopdir}/xterm.desktop
%{_pixmapsdir}/xterm.png
%{_mandir}/man1/resize.1*
%{_mandir}/man1/xterm.1*
%{_mandir}/man1/uxterm.1*
%{_mandir}/man1/koi8rxterm.1*
%lang(ko) %{_mandir}/ko/man1/xterm.1*
%lang(ko) %{_mandir}/ko/man1/uxterm.1*
