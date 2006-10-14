Summary:	Terminal emulator for X
Summary(pl):	Emulator terminala dla X
Name:		xterm
Version:	221
Release:	1
License:	MIT
Group:		X11/Applications
Source0:	ftp://invisible-island.net/xterm/%{name}-%{version}.tgz
# Source0-md5:	dbda54660a275225a418825742b9961f
Source1:	XTerm.ad-pl
Source2:	xterm.desktop
Source3:	xterm.png
Source4:	xterm.1x.ko
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
Program xterm to emulator terminala dla X Window System. Udostêpnia
terminale zgodne z DEC VT102/VT220 (VTxxx) oraz Tektronix 4014 dla
programów nie potrafi±cych u¿ywaæ bezpo¶rednio systemu okien.

Ta wersja implementuje kolory ISO/ANSI przy u¿yciu "nowego" modelu
kolorów (tzn. usuwania kolorem t³a). Implementuje tak¿e wiêkszo¶æ
sekwencji steruj±cych VT220.

%prep
%setup -q

%build
%configure \
	--enable-256-color \
	--enable-wide-chars \
	--with-app-defaults=%{_datadir}/X11/app-defaults \
	--with-utempter

%{__make} \
	EXTRA_LOADFLAGS="-ltinfo"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

echo '.so xterm.1' > $RPM_BUILD_ROOT%{_mandir}/man1/uxterm.1

install -D %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/X11/pl/app-defaults/XTerm
install -D %{SOURCE2} $RPM_BUILD_ROOT%{_desktopdir}/xterm.desktop
install -D %{SOURCE3} $RPM_BUILD_ROOT%{_pixmapsdir}/xterm.png
install -D %{SOURCE4} $RPM_BUILD_ROOT%{_mandir}/ko/man1/xterm.1
echo '.so xterm.1' > $RPM_BUILD_ROOT%{_mandir}/ko/man1/uxterm.1

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
%lang(pl) %{_datadir}/X11/pl/app-defaults/XTerm
%{_desktopdir}/xterm.desktop
%{_pixmapsdir}/xterm.png
%{_mandir}/man1/resize.1*
%{_mandir}/man1/xterm.1*
%{_mandir}/man1/uxterm.1*
%lang(ko) %{_mandir}/ko/man1/xterm.1*
%lang(ko) %{_mandir}/ko/man1/uxterm.1*
