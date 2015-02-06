Summary:	Nosefart player for Nintendo NES audio files
Name:		nosefart
Version:	2.9
Release:	2
License:	GPLv2+
Group:		Sound
Url:		http://nosefart.sourceforge.net/
Source0:	http://prdownloads.sourceforge.net/nosefart/%{name}-%{version}-mls.tar.bz2
Patch0:		nosefart-2.6-mls-desktopentry.patch
BuildRequires:	imagemagick
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gtk+-2.0)
Obsoletes:	xmms-nosefart < 2.7-3

%description
Nosefart plays .nsf audio files that were ripped from games for the Nintendo
Entertainment System.

%files
%doc README README.linux CHANGES
%{_bindir}/nosefart

#----------------------------------------------------------------------------

%package -n gnosefart
Summary:	Nosefart player for Nintendo NES audio files
Group:		Sound
Requires:	%{name} >= %{version}

%description -n gnosefart
Nosefart plays .nsf audio files that were ripped from games for the Nintendo
Entertainment System.

%files -n gnosefart
%doc README.xmms
%{_bindir}/gnosefart
%{_datadir}/applications/gnosefart.desktop
%{_datadir}/pixmaps/gnosefart.png
%{_liconsdir}/gnosefart.png
%{_iconsdir}/gnosefart.png
%{_miconsdir}/gnosefart.png

#----------------------------------------------------------------------------

%prep
%setup -q -n %{name}-%{version}-mls
ln -s gnosefart-1.5 src/gnosefart-1.4
%patch0 -p1

find . -perm 0640 | xargs chmod 0644
find . -name "Makefile*" -o -name "*.m4" -o -name "configure*" |xargs sed -i -e 's,configure.in,configure.ac,g'

%build
make clean
%make
cd src/gnosefart-*
rm -r autom4te.cache
rm install-sh missing mkinstalldirs
cp %{_datadir}/automake-*/mkinstalldirs .
autoreconf -fi
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

