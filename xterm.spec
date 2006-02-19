Summary:	Terminal emulator for X
Summary(pl):	Emulator terminala dla X
Name:		xterm
Version:	208
Release:	2
License:	MIT
Group:		X11/Applications
Source0:	ftp://invisible-island.net/xterm/%{name}-%{version}.tgz
# Source0-md5:	a062d0b398918015d07c31ecdcc5111a
Source1:	XTerm.ad-pl
Source2:	xterm.desktop
Source3:	xterm.png
URL:		http://invisible-island.net/xterm/
BuildRequires:	ncurses-devel
BuildRequires:	utempter-devel
BuildRequires:	xorg-lib-libXaw-devel
BuildRequires:	xorg-lib-libXft-devel
Requires:	xorg-lib-libXt >= 1.0.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The xterm program is a terminal emulator for the X Window System. It
provides DEC VT102/VT220 (VTxxx) and Tektronix 4014 compatible
terminals for programs that cannot use the window system directly.

This version implements ISO/ANSI colors using the "new" color model
(i.e., background color erase). It also implements most of the control
sequences for VT220.

%description -l pl
Program xterm to emulator terminala dla X Window System. Udost�pnia
terminale zgodne z DEC VT102/VT220 (VTxxx) oraz Tektronix 4014 dla
program�w nie potrafi�cych u�ywa� bezpo�rednio systemu okien.

Ta wersja implementuje kolory ISO/ANSI przy u�yciu "nowego" modelu
kolor�w (tzn. usuwania kolorem t�a). Implementuje tak�e wi�kszo��
sekwencji steruj�cych VT220.

%prep
%setup -q

%build
%configure \
	--enable-256-color \
	--enable-wide-chars \
	--with-app-defaults=%{_datadir}/X11/app-defaults \
	--with-utempter

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

echo '.so xterm.1' > $RPM_BUILD_ROOT%{_mandir}/man1/uxterm.1

install -D %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/X11/pl/app-defaults/XTerm
install -D %{SOURCE2} $RPM_BUILD_ROOT%{_desktopdir}/xterm.desktop
install -D %{SOURCE3} $RPM_BUILD_ROOT%{_pixmapsdir}/xterm.png

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README README.i18n xterm.log.html
%attr(755,root,root) %{_bindir}/resize
%attr(755,root,root) %{_bindir}/xterm
%attr(755,root,root) %{_bindir}/uxterm
%{_datadir}/X11/app-defaults/UXTerm
%{_datadir}/X11/app-defaults/XTerm
%{_datadir}/X11/app-defaults/XTerm-color
# XXX: which package this dir should belong to?
%{_datadir}/X11/pl
%{_desktopdir}/xterm.desktop
%{_pixmapsdir}/xterm.png
%{_mandir}/man1/resize.1*
%{_mandir}/man1/xterm.1*
%{_mandir}/man1/uxterm.1*
