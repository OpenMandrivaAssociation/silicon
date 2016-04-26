%define major 0
%define libsdatabase %mklibname sdatabase %{major}
%define libsidi %mklibname sidi %{major}
%define libsilicon %mklibname silicon %{major}
%define snap 20150413

Summary:	Disc burning and managing application
Name:		silicon
Version:	2.0.0
Release:	7.%{snap}.3
License:	GPLv3+
Group:		Archiving/Cd burning
Url:		https://github.com/realbardia/silicon
# git archive --format=tar --prefix=silicon-2.0.0-$(date +%Y%m%d)/ HEAD | xz -vf > silicon-2.0.0-$(date +%Y%m%d).tar.xz
Source0:	%{name}-%{version}-%{snap}.tar.xz
Source1:        Silicon-lang-ru.ts.tar.gz
Source2:        CMakeLists.txt.tar.gz
Source100:	silicon.rpmlintrc
Patch1:		silicon-2.0.0-qtlocalpeer.patch
BuildRequires:	cmake
BuildRequires:	qmake5
BuildRequires:	qt5-devel
BuildRequires:  qt5-linguist
BuildRequires:  qt5-linguist-tools
BuildRequires:	pkgconfig(Qt5Test)
BuildRequires:	pkgconfig(phonon)
BuildRequires:	pkgconfig(taglib)
# Extra BR needed for plugins check
BuildRequires:	cdrkit
BuildRequires:	cdrkit-genisoimage
BuildRequires:	dvd+rw-tools
BuildRequires:	fuse
BuildRequires:	fuseiso
BuildRequires:	mpg123
Requires:	cdrkit
Requires:	cdrkit-genisoimage
Requires:	dvd+rw-tools
Requires:	qt5-qtbase-database-plugin-mysql
Suggests:	%{name}-audio-disc
Suggests:	%{name}-converter
Suggests:	%{name}-copy-disc
Suggests:	%{name}-database
Suggests:	%{name}-data-disc
Suggests:	%{name}-disc-details
Suggests:	%{name}-disc-eraser
Suggests:	%{name}-disc-imaging
Suggests:	%{name}-disc-scanner
Suggests:	%{name}-image-burner
Suggests:	%{name}-library
Suggests:	%{name}-mounter
Suggests:	%{name}-sample-app
Suggests:	%{name}-script-runner
Suggests:	%{name}-themes
Suggests:	%{name}-plugin-audio-cd-record
Suggests:	%{name}-plugin-cd-record
Suggests:	%{name}-plugin-eraser
Suggests:	%{name}-plugin-fuseiso
Suggests:	%{name}-plugin-mkdiscfs
Suggests:	%{name}-plugin-mkisofs
Suggests:	%{name}-plugin-mpg123
Suggests:	%{name}-plugin-read-cd
Suggests:	%{name}-plugin-rootmount
Suggests:	%{name}-plugin-single-inner-dialog
Suggests:	%{name}-plugin-system-tray
Suggests:	%{name}-plugin-tagarg-audio-disc
Requires:	%{name}-plugin-udisks
Obsoletes:	silicon-limoo < %{EVRD}
Obsoletes:	silicon-tagarg-player < %{EVRD}
Obsoletes:	silicon-plugin-lyric-browser < %{EVRD}
Obsoletes:	silicon-plugin-now-playing < %{EVRD}
Obsoletes:	silicon-plugin-tagarg-audio-disc < %{EVRD}

%description
Silicon Empire is set of tools to Burn, Copy, Backup and Manage
your optical discs like CDs, DVDs and Blu-Rays.

%files
%doc README
%{_bindir}/%{name}
%{_bindir}/%{name}_rootmount
%{_datadir}/applications/silicon.desktop
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/%{name}/languages/*

#----------------------------------------------------------------------------

%package -n %{libsdatabase}
Summary:	Silicon shared library
Group:		System/Libraries
Requires:	qt5-qtbase-database-plugin-sqlite

%description -n %{libsdatabase}
Silicon shared library.

%files -n %{libsdatabase}
%{_libdir}/libsdatabase.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{libsidi}
Summary:	Silicon shared library
Group:		System/Libraries

%description -n %{libsidi}
Silicon shared library.

%files -n %{libsidi}
%{_libdir}/libsidi.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{libsilicon}
Summary:	Silicon shared library
Group:		System/Libraries

%description -n %{libsilicon}
Silicon shared library.

%files -n %{libsilicon}
%{_libdir}/libsilicon.so.%{major}*

#----------------------------------------------------------------------------

%package audio-disc
Summary:	Silicon audio disc
Group:		Archiving/Cd burning
Requires:	%{name} = %{EVRD}

%description audio-disc
Silicon application to create Audio discs:
* CDs
* DVDs
* Blu-Rays

%files audio-disc
%{_libdir}/%{name}/apps/libaudiodisc.so*

#----------------------------------------------------------------------------

%package converter
Summary:	Silicon converter
Group:		Archiving/Cd burning
Requires:	%{name} = %{EVRD}

%description converter
Silicon application to convert your files to other supported formats.

%files converter
%{_libdir}/%{name}/apps/libConverter.so*

#----------------------------------------------------------------------------

%package copy-disc
Summary:	Silicon copy disc
Group:		Archiving/Cd burning
Requires:	%{name} = %{EVRD}

%description copy-disc
Silicon application to copy a disc to another disc.

%files copy-disc
%{_libdir}/%{name}/apps/libCopyDisc.so*

#----------------------------------------------------------------------------

%package database
Summary:	Silicon database
Group:		Archiving/Cd burning
Requires:	%{name} = %{EVRD}

%description database
Silicon application to show informations and indexed data that DiscScanner
stored into the Silicon DataBase.

%files database
%{_libdir}/%{name}/apps/libDataBase.so*

#----------------------------------------------------------------------------

%package data-disc
Summary:	Silicon data disc
Group:		Archiving/Cd burning
Requires:	%{name} = %{EVRD}

%description data-disc
Silicon application to burn data discs or to create data images.

%files data-disc
%{_libdir}/%{name}/apps/libdatadisc.so*

#----------------------------------------------------------------------------

%package disc-details
Summary:	Silicon disc details
Group:		Archiving/Cd burning
Requires:	%{name} = %{EVRD}

%description disc-details
Silicon application to show disc, image or database disc details.

%files disc-details
%{_libdir}/%{name}/apps/libDiscDetails.so*

#----------------------------------------------------------------------------

%package disc-eraser
Summary:	Silicon disc eraser
Group:		Archiving/Cd burning
Requires:	%{name} = %{EVRD}

%description disc-eraser
Silicon application to erase rw discs.

%files disc-eraser
%{_libdir}/%{name}/apps/libDiscEraser.so*

#----------------------------------------------------------------------------

%package disc-imaging
Summary:	Silicon disc imaging
Group:		Archiving/Cd burning
Requires:	%{name} = %{EVRD}

%description disc-imaging
Silicon application to create images of your discs.

%files disc-imaging
%{_libdir}/%{name}/apps/libDiscImaging.so*

#----------------------------------------------------------------------------

%package disc-scanner
Summary:	Silicon disc scanner
Group:		Archiving/Cd burning
Requires:	%{name} = %{EVRD}

%description disc-scanner
Silicon application to collect data from your discs to the
Silicon DataBase.

%files disc-scanner
%{_libdir}/%{name}/apps/libDiscScanner.so*

#----------------------------------------------------------------------------

%package image-burner
Summary:	Silicon image burner
Group:		Archiving/Cd burning
Requires:	%{name} = %{EVRD}

%description image-burner
Silicon application to burn a images to discs.

%files image-burner
%{_libdir}/%{name}/apps/libImageBurner.so*

#----------------------------------------------------------------------------

%package library
Summary:	Silicon library
Group:		Archiving/Cd burning
Requires:	%{name} = %{EVRD}

%description library
Silicon application to manage your iso images in a classic way.

%files library
%{_libdir}/%{name}/apps/libLibrary.so*

#----------------------------------------------------------------------------

%package mounter
Summary:	Silicon mounter
Group:		Archiving/Cd burning
Requires:	%{name} = %{EVRD}

%description mounter
Silicon application to mount/umount images easily.

%files mounter
%{_libdir}/%{name}/apps/libMounter.so*

#----------------------------------------------------------------------------

%package sample-app
Summary:	Silicon sample app
Group:		Archiving/Cd burning
Requires:	%{name} = %{EVRD}

%description sample-app
Silicon sample application.

%files sample-app
%{_libdir}/%{name}/apps/libsampleApp.so*

#----------------------------------------------------------------------------

%package script-runner
Summary:	Silicon script runner
Group:		Archiving/Cd burning
Requires:	%{name} = %{EVRD}

%description script-runner
Silicon application to run scripts.

%files script-runner
%{_libdir}/%{name}/apps/libScriptRunner.so*

#----------------------------------------------------------------------------

%package themes
Summary:	Silicon themes
Group:		Archiving/Cd burning
Requires:	%{name} = %{EVRD}

%description themes
Silicon themes.

%files themes
%{_datadir}/%{name}/themes/*

#----------------------------------------------------------------------------

%package plugin-audio-cd-record
Summary:	Silicon Audio CD record plugin
Group:		Archiving/Cd burning
Requires:	%{name} = %{EVRD}
Requires:	mpg123

%description plugin-audio-cd-record
Silicon Audio CD record plugin.

Burn Audio-Discs using AudioCdRecord/Wodim.

%files plugin-audio-cd-record
%{_libdir}/%{name}/plugins/libAudioCdRecord.so*

#----------------------------------------------------------------------------

%package plugin-cd-record
Summary:	Silicon CD record plugin
Group:		Archiving/Cd burning
Requires:	%{name} = %{EVRD}

%description plugin-cd-record
Silicon CD record plugin.

Copy Disc to Disc or Burn Images to Discsr using CdRecord/Wodim.

%files plugin-cd-record
%{_libdir}/%{name}/plugins/libCdRecord.so*

#----------------------------------------------------------------------------

%package plugin-eraser
Summary:	Silicon eraser plugin
Group:		Archiving/Cd burning
Requires:	%{name} = %{EVRD}

%description plugin-eraser
Silicon eraser plugin.

Erase Optical discs using dvd+rw-tools and cdrecord.

%files plugin-eraser
%{_libdir}/%{name}/plugins/libEraser.so*

#----------------------------------------------------------------------------

%package plugin-fuseiso
Summary:	Silicon fuseiso plugin
Group:		Archiving/Cd burning
Requires:	%{name} = %{EVRD}
Requires:	fuse
Requires:	fuseiso

%description plugin-fuseiso
Silicon fuseiso plugin.

Mount Disc images using FUseIso.

%files plugin-fuseiso
%{_libdir}/%{name}/plugins/libFUseIso.so*

#----------------------------------------------------------------------------

%package plugin-mkdiscfs
Summary:	Silicon MkDiscFs plugin
Group:		Archiving/Cd burning
Requires:	%{name} = %{EVRD}

%description plugin-mkdiscfs
Silicon MkDiscFs plugin.

Burn Data Discs using MkIsoFs and CdRecord.

%files plugin-mkdiscfs
%{_libdir}/%{name}/plugins/libMkDiscFs.so*

#----------------------------------------------------------------------------

%package plugin-mkisofs
Summary:	Silicon MkIsoFs plugin
Group:		Archiving/Cd burning
Requires:	%{name} = %{EVRD}

%description plugin-mkisofs
Silicon MkIsoFs plugin.

Create Iso Images using MkIsoFs.

%files plugin-mkisofs
%{_libdir}/%{name}/plugins/libMkIsoFs.so*

#----------------------------------------------------------------------------

%package plugin-mpg123
Summary:	Silicon mpg123 plugin
Group:		Archiving/Cd burning
Requires:	%{name} = %{EVRD}
Requires:	mpg123

%description plugin-mpg123
Silicon mpg123 plugin.

It's used to convert mpeg formats.

%files plugin-mpg123
%{_libdir}/%{name}/plugins/libmpg123.so*

#----------------------------------------------------------------------------

%package plugin-read-cd
Summary:	Silicon read CD plugin
Group:		Archiving/Cd burning
Requires:	%{name} = %{EVRD}

%description plugin-read-cd
Silicon read CD plugin.

Read Discs using ReadCd/Readom.

%files plugin-read-cd
%{_libdir}/%{name}/plugins/libReadCd.so*

#----------------------------------------------------------------------------

%package plugin-rootmount
Summary:        Silicon root mount plugin
Group:          Archiving/Cd burning
Requires:       %{name} = %{EVRD}

%description plugin-rootmount
Silicon root mount plugin.

%files plugin-rootmount
%{_libdir}/%{name}/plugins/libRootMount.so*

#----------------------------------------------------------------------------

%package plugin-single-inner-dialog
Summary:	Silicon single inner dialog plugin
Group:		Archiving/Cd burning
Requires:	%{name} = %{EVRD}

%description plugin-single-inner-dialog
Silicon single inner dialog plugin.

Show Dialogs in Single and Animation Window.

%files plugin-single-inner-dialog
%{_libdir}/%{name}/plugins/libSingleInnerDialog.so*

#----------------------------------------------------------------------------

%package plugin-system-tray
Summary:	Silicon system tray plugin
Group:		Archiving/Cd burning
Requires:	%{name} = %{EVRD}

%description plugin-system-tray
Silicon system tray plugin.

%files plugin-system-tray
%{_libdir}/%{name}/plugins/libSystemTray.so*

#----------------------------------------------------------------------------

%package plugin-udisks
Summary:	Silicon UDisks plugin
Group:		Archiving/Cd burning
Requires:	%{name} = %{EVRD}
Requires:	udisks2

%description plugin-udisks
Silicon UDisks plugin.

Detect Devices using UDisks.

%files plugin-udisks
%{_libdir}/%{name}/plugins/libUDisksDeviceNotifier.so*

#----------------------------------------------------------------------------

%prep
%setup -qn %{name}-%{version}-%{snap}
%apply_patches

#pushd src/Silicon/locale
#tar -xvzf %{SOURCE1}
#popd

#pushd src/Silicon
#tar -xvzf %{SOURCE2}
#popd

%build
%qmake_qt5
%make -j1

%install
rm -Rf %{buildroot}/*
mkdir -p %{buildroot}/usr

mkdir -p %{buildroot}/%{_libdir}

cp -Rp ../build/lib/* %{buildroot}/%{_libdir}
cp -Rp ../build/bin %{buildroot}/%{_prefix}
cp -Rp ../build/share %{buildroot}/%{_prefix}

mkdir -p %{buildroot}/%{_datadir}/pixmaps/
mv %{buildroot}/usr/share/silicon/icons/silicon.png %{buildroot}/%{_datadir}/pixmaps/

mkdir -p %{buildroot}/%{_datadir}/applications
cp Silicon/files/Silicon.desktop %{buildroot}/%{_datadir}/applications/silicon.desktop

rm -f %{buildroot}%{_libdir}/%{name}/plugins/libSingleInnerDialogQML.so
rm -f %{buildroot}%{_libdir}/%{name}/plugins/libHal*

#321 in contrib and not maintained
rm -f %{buildroot}%{_libdir}/%{name}/plugins/libmpg321*

rm -f %{buildroot}%{_libdir}/libsdatabase.so
rm -f %{buildroot}%{_libdir}/libsidi.so
rm -f %{buildroot}%{_libdir}/libsilicon.so
