Name:		nosefart
Summary:	Nosefart player for Nintendo NES audio files
Version:	2.7
Release:	3
License:	GPLv2
Group:		Sound
URL: 		http://nosefart.sourceforge.net/
Source0:	http://prdownloads.sourceforge.net/nosefart/%name-%version-mls.tar.bz2
Patch0:		nosefart-2.6-mls-desktopentry.patch
Patch1:		nosefart-2.7-makefile.patch
BuildRequires:	imagemagick
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gtk+-2.0)
Obsoletes:	xmms-nosefart < 2.7-3

%description
Nosefart plays .nsf audio files that were ripped from games for the Nintendo
Entertainment System.

%package -n gnosefart
Summary:	Nosefart player for Nintendo NES audio files
Group:		Sound
Requires:	%{name} >= %{version}

%description  -n gnosefart
Nosefart plays .nsf audio files that were ripped from games for the Nintendo
Entertainment System.

%prep
%setup -q -n %{name}-%{version}-mls
ln -s gnosefart-1.5 src/gnosefart-1.4
%patch0 -p1
%patch1 -p1

%build
make clean
%make
cd src/gnosefart-*
./autogen.sh
%configure2_5x
%make

%install
make PREFIX=%{buildroot}%{_prefix} install
cd src/gnosefart-*
%makeinstall_std
mkdir -p %{buildroot}{%{_liconsdir},%{_iconsdir},%{_miconsdir}}

#icons
ln -s %{_datadir}/pixmaps/gnosefart.png %{buildroot}/%{_liconsdir}/gnosefart.png
convert -scale 32x32 %{buildroot}%{_datadir}/pixmaps/gnosefart.png %{buildroot}%{_iconsdir}/gnosefart.png
convert -scale 16x16 %{buildroot}%{_datadir}/pixmaps/gnosefart.png %{buildroot}%{_miconsdir}/gnosefart.png

%files
%doc README README.linux CHANGES
%{_bindir}/nosefart

%files -n gnosefart
%doc README.xmms
%{_bindir}/gnosefart
%{_datadir}/applications/gnosefart.desktop
%{_datadir}/pixmaps/gnosefart.png
%{_liconsdir}/gnosefart.png
%{_iconsdir}/gnosefart.png
%{_miconsdir}/gnosefart.png


%changelog
* Sun Jul 31 2011 Andrey Bondrov <abondrov@mandriva.org> 2.7-2mdv2012.0
+ Revision: 692564
- Drop deprecated menu
- Add patch 1 to fix build in 2011
- imported package nosefart


* Sun Jul 24 2011 Andrey Bondrov <bondrov@math.dvgu.ru> 2.7-2mdv2011.0
- Import from PLF
- Remove PLF reference

* Sun Feb 10 2008 Götz Waschk <goetz@zarb.org> 2.7-1plf2008.1
- new version

* Wed Jan 23 2008 Götz Waschk <goetz@zarb.org> 2.6-3plf2008.1
- fix plf reason
- fix desktop entry

* Wed Aug  2 2006 Götz Waschk <goetz@zarb.org> 2.6-2plf2007.0
- xdg menu

* Fri Sep 23 2005 GÃ¶tz Waschk <goetz@zarb.org> 2.6-1plf
- New release 2.6

* Tue Sep 20 2005 Götz Waschk <goetz@zarb.org> 2.5-1plf
- New release 2.5

* Wed Sep 14 2005 Götz Waschk <goetz@zarb.org> 2.4-1plf
- spec fixes
- New release 2.4

* Tue Aug 31 2004 Götz Waschk <goetz@zarb.org> 2.2-1plf
- new version

* Sat Apr 24 2004 Götz Waschk <goetz@plf.zarb.org> 2.1-1plf
- disable gnosefart on mdk 9.1 (autotools problem)
- add gnosefart menu entry
- gnosefart 1.0
- New release 2.1

* Tue Apr 20 2004 Götz Waschk <goetz@plf.zarb.org> 2.0-3plf
- gnosefart requries nosefart

* Mon Apr 19 2004 Götz Waschk <goetz@plf.zarb.org> 2.0-2plf
- split out xmms plugin and gnosefart
- fix gnosefart buildrequires

* Sat Apr 17 2004 Götz Waschk <goetz@plf.zarb.org> 2.0-1plf
- add gnosefart
- fix description
- new version

* Tue Mar 23 2004 Götz Waschk <goetz@plf.zarb.org> 1.92j-1plf
- new version

* Tue Oct 28 2003 Götz Waschk <goetz@plf.zarb.org> 1.92i-1plf
- initial package
