Summary:	Terminal emulator for X
Summary(pl):	Emulator terminala dla X
Name:		xterm
Version:	207
Release:	1
License:	MIT
Group:		X11/Applications
Source0:	ftp://invisible-island.net/xterm/%{name}-%{version}.tgz
# Source0-md5:	3de8a3756c284a46a08c6d0308909486
URL:		http://invisible-island.net/xterm/
BuildRequires:	ncurses-devel
BuildRequires:	utempter-devel
BuildRequires:	xorg-lib-libXaw-devel
BuildRequires:	xorg-lib-libXft-devel
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
	--with-app-defaults=%{_libdir}/X11/app-defaults \
	--with-utempter

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

echo '.so xterm.1' > $RPM_BUILD_ROOT%{_mandir}/man1/uxterm.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README README.i18n xterm.log.html
%attr(755,root,root) %{_bindir}/resize
%attr(755,root,root) %{_bindir}/xterm
%attr(755,root,root) %{_bindir}/uxterm
%{_libdir}/X11/app-defaults/*
%{_mandir}/man1/resize.1*
%{_mandir}/man1/xterm.1*
%{_mandir}/man1/uxterm.1*
