%define major 2
%define libsdatabase %mklibname SDataBase %{major}
%define libsidi %mklibname SiDi %{major}
%define libsiliconlib %mklibname SiliconLib %{major}

Summary:	Disc burning and managing application
Name:		silicon
Version:	2.0.0
Release:	6
License:	GPLv3+
Group:		Archiving/Cd burning
Url:		http://getsilicon.org
Source0:	http://getsilicon.org/download/%{name}_%{version}_source.tar.gz
Source1:        Silicon-lang-ru.ts.tar.gz
Source2:        CMakeLists.txt.tar.gz
Patch0:		silicon-1.8.1-splugin-lyricbrowser.patch
Patch1:		silicon-1.8.1-qtlocalpeer.patch
Patch2:		silicon-2.0.0-versioned-libraries.patch
Patch3:		0001-Move-to-sialan-labs-and-Ported-to-Qt5-completed.patch
Patch4:		0002-Debian-build-system-and-improvment-on-build-system.patch
BuildRequires:	cmake
BuildRequires:	qmake5
BuildRequires:	qt5-devel
BuildRequires:	pkgconfig(phonon)
BuildRequires:	pkgconfig(taglib)
# Extra BR needed for plugins check
BuildRequires:	cdrkit
BuildRequires:	cdrkit-genisoimage
BuildRequires:	dvd+rw-tools
BuildRequires:	fuse
BuildRequires:	fuseiso
BuildRequires:	mpg123
BuildRequires:	udisks
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
Suggests:	%{name}-limoo
Suggests:	%{name}-mounter
Suggests:	%{name}-sample-app
Suggests:	%{name}-script-runner
Suggests:	%{name}-tagarg-player
Suggests:	%{name}-themes
Suggests:	%{name}-plugin-audio-cd-record
Suggests:	%{name}-plugin-cd-record
Suggests:	%{name}-plugin-eraser
Suggests:	%{name}-plugin-fuseiso
Suggests:	%{name}-plugin-lyric-browser
Suggests:	%{name}-plugin-mkdiscfs
Suggests:	%{name}-plugin-mkisofs
Suggests:	%{name}-plugin-mpg123
Suggests:	%{name}-plugin-now-playing
Suggests:	%{name}-plugin-read-cd
Suggests:	%{name}-plugin-single-inner-dialog
Suggests:	%{name}-plugin-system-tray
Suggests:	%{name}-plugin-tagarg-audio-disc
Requires:	%{name}-plugin-udisks

%description
Silicon Empire is set of tools to Burn, Copy, Backup and Manage
your optical discs like CDs, DVDs and Blu-Rays.

%files
%doc README Authors
%{_bindir}/%{name}
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
%{_libdir}/libSDataBase.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{libsidi}
Summary:	Silicon shared library
Group:		System/Libraries

%description -n %{libsidi}
Silicon shared library.

%files -n %{libsidi}
%{_libdir}/libSiDi.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{libsiliconlib}
Summary:	Silicon shared library
Group:		System/Libraries

%description -n %{libsiliconlib}
Silicon shared library.

%files -n %{libsiliconlib}
%{_libdir}/libSiliconLib.so.%{major}*

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
%{_libdir}/%{name}/apps/libAudioDisc.so

#----------------------------------------------------------------------------

%package converter
Summary:	Silicon converter
Group:		Archiving/Cd burning
Requires:	%{name} = %{EVRD}

%description converter
Silicon application to convert your files to other supported formats.

%files converter
%{_libdir}/%{name}/apps/libConverter.so

#----------------------------------------------------------------------------

%package copy-disc
Summary:	Silicon copy disc
Group:		Archiving/Cd burning
Requires:	%{name} = %{EVRD}

%description copy-disc
Silicon application to copy a disc to another disc.

%files copy-disc
%{_libdir}/%{name}/apps/libCopyDisc.so

#----------------------------------------------------------------------------

%package database
Summary:	Silicon database
Group:		Archiving/Cd burning
Requires:	%{name} = %{EVRD}

%description database
Silicon application to show informations and indexed data that DiscScanner
stored into the Silicon DataBase.

%files database
%{_libdir}/%{name}/apps/libDataBase.so

#----------------------------------------------------------------------------

%package data-disc
Summary:	Silicon data disc
Group:		Archiving/Cd burning
Requires:	%{name} = %{EVRD}

%description data-disc
Silicon application to burn data discs or to create data images.

%files data-disc
%{_libdir}/%{name}/apps/libDataDisc.so

#----------------------------------------------------------------------------

%package disc-details
Summary:	Silicon disc details
Group:		Archiving/Cd burning
Requires:	%{name} = %{EVRD}

%description disc-details
Silicon application to show disc, image or database disc details.

%files disc-details
%{_libdir}/%{name}/apps/libDiscDetails.so

#----------------------------------------------------------------------------

%package disc-eraser
Summary:	Silicon disc eraser
Group:		Archiving/Cd burning
Requires:	%{name} = %{EVRD}

%description disc-eraser
Silicon application to erase rw discs.

%files disc-eraser
%{_libdir}/%{name}/apps/libDiscEraser.so

#----------------------------------------------------------------------------

%package disc-imaging
Summary:	Silicon disc imaging
Group:		Archiving/Cd burning
Requires:	%{name} = %{EVRD}

%description disc-imaging
Silicon application to create images of your discs.

%files disc-imaging
%{_libdir}/%{name}/apps/libDiscImaging.so

#----------------------------------------------------------------------------

%package disc-scanner
Summary:	Silicon disc scanner
Group:		Archiving/Cd burning
Requires:	%{name} = %{EVRD}

%description disc-scanner
Silicon application to collect data from your discs to the
Silicon DataBase.

%files disc-scanner
%{_libdir}/%{name}/apps/libDiscScanner.so

#----------------------------------------------------------------------------

%package image-burner
Summary:	Silicon image burner
Group:		Archiving/Cd burning
Requires:	%{name} = %{EVRD}

%description image-burner
Silicon application to burn a images to discs.

%files image-burner
%{_libdir}/%{name}/apps/libImageBurner.so

#----------------------------------------------------------------------------

%package library
Summary:	Silicon library
Group:		Archiving/Cd burning
Requires:	%{name} = %{EVRD}

%description library
Silicon application to manage your iso images in a classic way.

%files library
%{_libdir}/%{name}/apps/libLibrary.so

#----------------------------------------------------------------------------

%package limoo
Summary:	Silicon Limoo
Group:		Archiving/Cd burning
Requires:	%{name} = %{EVRD}

%description limoo
Silicon application - Limoo image viewer.

%files limoo
%{_libdir}/%{name}/apps/libLimoo.so

#----------------------------------------------------------------------------

%package mounter
Summary:	Silicon mounter
Group:		Archiving/Cd burning
Requires:	%{name} = %{EVRD}

%description mounter
Silicon application to mount/umount images easily.

%files mounter
%{_libdir}/%{name}/apps/libMounter.so

#----------------------------------------------------------------------------

%package sample-app
Summary:	Silicon sample app
Group:		Archiving/Cd burning
Requires:	%{name} = %{EVRD}

%description sample-app
Silicon sample application.

%files sample-app
%{_libdir}/%{name}/apps/libSampleApp.so

#----------------------------------------------------------------------------

%package script-runner
Summary:	Silicon script runner
Group:		Archiving/Cd burning
Requires:	%{name} = %{EVRD}

%description script-runner
Silicon application to run scripts.

%files script-runner
%{_libdir}/%{name}/apps/libScriptRunner.so

#----------------------------------------------------------------------------

%package tagarg-player
Summary:	Silicon app tagarg player
Group:		Archiving/Cd burning
Requires:	%{name} = %{EVRD}

%description tagarg-player
Silicon music player.

%files tagarg-player
%{_libdir}/%{name}/apps/libTagargPlayer.so

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
%{_libdir}/%{name}/plugins/libAudioCdRecord.so

#----------------------------------------------------------------------------

%package plugin-cd-record
Summary:	Silicon CD record plugin
Group:		Archiving/Cd burning
Requires:	%{name} = %{EVRD}

%description plugin-cd-record
Silicon CD record plugin.

Copy Disc to Disc or Burn Images to Discsr using CdRecord/Wodim.

%files plugin-cd-record
%{_libdir}/%{name}/plugins/libCdRecord.so

#----------------------------------------------------------------------------

%package plugin-eraser
Summary:	Silicon eraser plugin
Group:		Archiving/Cd burning
Requires:	%{name} = %{EVRD}

%description plugin-eraser
Silicon eraser plugin.

Erase Optical discs using dvd+rw-tools and cdrecord.

%files plugin-eraser
%{_libdir}/%{name}/plugins/libEraser.so

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
%{_libdir}/%{name}/plugins/libFUseIso.so

#----------------------------------------------------------------------------

%package plugin-lyric-browser
Summary:	Silicon lyric browser plugin
Group:		Archiving/Cd burning
Requires:	%{name} = %{EVRD}
Requires:	%{name}-tagarg-player = %{EVRD}

%description plugin-lyric-browser
Silicon lyric browser plugin.

%files plugin-lyric-browser
%{_libdir}/%{name}/plugins/libLyricBrowser.so

#----------------------------------------------------------------------------

%package plugin-mkdiscfs
Summary:	Silicon MkDiscFs plugin
Group:		Archiving/Cd burning
Requires:	%{name} = %{EVRD}

%description plugin-mkdiscfs
Silicon MkDiscFs plugin.

Burn Data Discs using MkIsoFs and CdRecord.

%files plugin-mkdiscfs
%{_libdir}/%{name}/plugins/libMkDiscFs.so

#----------------------------------------------------------------------------

%package plugin-mkisofs
Summary:	Silicon MkIsoFs plugin
Group:		Archiving/Cd burning
Requires:	%{name} = %{EVRD}

%description plugin-mkisofs
Silicon MkIsoFs plugin.

Create Iso Images using MkIsoFs.

%files plugin-mkisofs
%{_libdir}/%{name}/plugins/libMkIsoFs.so

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
%{_libdir}/%{name}/plugins/libmpg123.so

#----------------------------------------------------------------------------

%package plugin-now-playing
Summary:	Silicon now playing plugin
Group:		Archiving/Cd burning
Requires:	%{name} = %{EVRD}
Requires:	%{name}-tagarg-player = %{EVRD}

%description plugin-now-playing
Silicon now playing plugin.

%files plugin-now-playing
%{_libdir}/%{name}/plugins/libNowPlaying.so

#----------------------------------------------------------------------------

%package plugin-read-cd
Summary:	Silicon read CD plugin
Group:		Archiving/Cd burning
Requires:	%{name} = %{EVRD}

%description plugin-read-cd
Silicon read CD plugin.

Read Discs using ReadCd/Readom.

%files plugin-read-cd
%{_libdir}/%{name}/plugins/libReadCd.so

#----------------------------------------------------------------------------

%package plugin-single-inner-dialog
Summary:	Silicon single inner dialog plugin
Group:		Archiving/Cd burning
Requires:	%{name} = %{EVRD}

%description plugin-single-inner-dialog
Silicon single inner dialog plugin.

Show Dialogs in Single and Animation Window.

%files plugin-single-inner-dialog
%{_libdir}/%{name}/plugins/libSingleInnerDialog.so

#----------------------------------------------------------------------------

%package plugin-system-tray
Summary:	Silicon system tray plugin
Group:		Archiving/Cd burning
Requires:	%{name} = %{EVRD}

%description plugin-system-tray
Silicon system tray plugin.

%files plugin-system-tray
%{_libdir}/%{name}/plugins/libSystemTray.so

#----------------------------------------------------------------------------

%package plugin-tagarg-audio-disc
Summary:	Silicon tagarg audio disc plugin
Group:		Archiving/Cd burning
Requires:	%{name} = %{EVRD}

%description plugin-tagarg-audio-disc
Silicon tagarg audio disc plugin.

Add an audio-disc widget to player.

%files plugin-tagarg-audio-disc
%{_libdir}/%{name}/plugins/libTagargAudioDisc.so

#----------------------------------------------------------------------------

%package plugin-udisks
Summary:	Silicon UDisks plugin
Group:		Archiving/Cd burning
Requires:	%{name} = %{EVRD}
Requires:	udisks

%description plugin-udisks
Silicon UDisks plugin.

Detect Devices using UDisks.

%files plugin-udisks
%{_libdir}/%{name}/plugins/libUDisks.so

#----------------------------------------------------------------------------

%prep
%setup -qn %{name}-empire
%patch0 -p1 -b .lbnetwork~
%patch1 -p1 -b .unistd~
%patch2 -p1 -b .sonames~

pushd src/Silicon/locale
tar -xvzf %{SOURCE1}
popd

pushd src/Silicon
tar -xvzf %{SOURCE2}
popd

%build
cd src
%cmake_qt5
%make

%install
cd src
%makeinstall_std -C build

rm -f %{buildroot}%{_libdir}/%{name}/plugins/libSingleInnerDialogQML.so
rm -f %{buildroot}%{_libdir}/libSDataBase.so
rm -f %{buildroot}%{_libdir}/libSiDi.so
rm -f %{buildroot}%{_libdir}/libSiliconLib.so
