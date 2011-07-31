%define build_gnosefart 1

Name: nosefart
Summary: Nosefart player for Nintendo NES audio files
Version: 2.7
Release: %mkrel 2
License: GPLv2
Group: Sound
URL: http://nosefart.sourceforge.net/
Source0: http://prdownloads.sourceforge.net/nosefart/%name-%version-mls.tar.bz2
Patch: nosefart-2.6-mls-desktopentry.patch
Patch1: nosefart-2.7-makefile.patch
BuildRoot: %{_tmppath}/%{name}-buildroot
BuildRequires: xmms-devel
#BuildRequires: automake1.4

%description
Nosefart plays .nsf audio files that were ripped from games for the Nintendo
Entertainment System.

%package -n xmms-nosefart
Summary: XMMS plugin based on Nosefart for Nintendo NES audio files
Group: Sound
Requires: xmms

%description  -n xmms-nosefart
Nosefart plays .nsf audio files that were ripped from games for the Nintendo
Entertainment System.

%if %{build_gnosefart}
%package -n gnosefart
Summary: Nosefart player for Nintendo NES audio files
Group: Sound
Requires: %{name} >= %{version}
BuildRequires: ImageMagick
BuildRequires: gtk+2-devel

%description  -n gnosefart
Nosefart plays .nsf audio files that were ripped from games for the Nintendo
Entertainment System.
%endif

%prep
%setup -q -n %{name}-%{version}-mls
ln -s gnosefart-1.5 src/gnosefart-1.4
%patch -p1
%patch1 -p1
#cd src/gnosefart*
#ln -sf %{_datadir}/automake-1.4/install-sh .
#ln -sf %{_datadir}/automake-1.4/mkinstalldirs .

%build
make clean
%make
cd src/xmms
%configure2_5x
%make
%if %{build_gnosefart}
cd ../gnosefart-*
./autogen.sh
%configure2_5x
%make
%endif

%install
rm -rf %{buildroot}
make PREFIX=%{buildroot}%{_prefix} install
install -m 755 -D src/xmms/.libs/libnosefart.so %{buildroot}%{_libdir}/xmms/Input/libnosefart.so
%if %{build_gnosefart}
cd src/gnosefart-*
%makeinstall_std
mkdir -p %{buildroot}{%{_menudir},%{_liconsdir},%{_iconsdir},%{_miconsdir}}
cat > %{buildroot}%{_menudir}/gnosefart <<EOF 
?package(gnosefart):command="%{_bindir}/gnosefart" title="Gnosefart" longtitle="Nosefart - NSF Music Player" needs="X11" section="Multimedia/Sound" icon="gnosefart.png" mimetypes="audio/x-nsf" startup_notify="true" xdg="true"
EOF

#icons
ln -s %{_datadir}/pixmaps/gnosefart.png %{buildroot}/%{_liconsdir}/gnosefart.png
convert -scale 32x32 %{buildroot}%{_datadir}/pixmaps/gnosefart.png %{buildroot}%{_iconsdir}/gnosefart.png
convert -scale 16x16 %{buildroot}%{_datadir}/pixmaps/gnosefart.png %{buildroot}%{_miconsdir}/gnosefart.png
%endif

%clean
rm -rf %{buildroot}

%if %{build_gnosefart}
%if %mdkversion < 200900
%post -n gnosefart
%{update_menus}

%postun -n gnosefart
%{clean_menus}
%endif
%endif

%files
%defattr(-, root, root)
%doc README README.linux CHANGES
%{_bindir}/nosefart

%files -n xmms-nosefart
%defattr(-, root, root)
%doc README.xmms
%{_libdir}/xmms/Input/libnosefart.so

%if %{build_gnosefart}
%files -n gnosefart
%defattr(-, root, root)
%doc README.xmms
%{_bindir}/gnosefart
%{_datadir}/applications/gnosefart.desktop
%{_datadir}/pixmaps/gnosefart.png
%{_menudir}/gnosefart
%{_liconsdir}/gnosefart.png
%{_iconsdir}/gnosefart.png
%{_miconsdir}/gnosefart.png
%endif

