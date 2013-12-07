Name:		silicon
Version:	1.8.1
Release:	3
Group:		Archiving/Cd burning
License:	GPLv3
Url:		http://getsilicon.org
Source0:	http://getsilicon.org/download/%{name}-%{version}-src.tar.gz
Summary:	Disc burning application
Patch0:		%{name}-1.8.1-splugin-lyricbrowser.patch
Patch1:		%{name}-1.8.1-qtlocalpeer.patch

BuildRequires:	cmake
BuildRequires:	qt4-devel
BuildRequires:	taglib-devel
BuildRequires:	pkgconfig(libmpg123)
BuildRequires:	mpg123
BuildRequires:	pkgconfig(phonon)
BuildRequires:	cdrkit
BuildRequires:	polkit
BuildRequires:	dvd+rw-tools

Requires:	cdrkit
Requires:	cdrkit-genisoimage
Requires:	mpg123
Requires:	dvd+rw-tools

%description
Silicon Empire is set of tools to Burn, Copy, Backup and Manage 
your optical discs like CDs, DVDs and Blu-Rays. 

%prep
%setup -q -n %{name}-%{version}-src
%patch0 -p1 -b .lbnetwork
%patch1 -p1 -b .unistd

%build
%cmake_qt4
%make

%install
%makeinstall_std -C build

desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

%files
%doc README Authors
%{_bindir}/%{name}
%{_libdir}/libSDataBase.so
%{_libdir}/libSiDi.so
%{_libdir}/libSiliconLib.so
%{_datadir}/applications/silicon.desktop
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/%{name}/languages/*

#-----------------------------------------------------

%package	audio-disc
Summary:	Silicon audio disc
Group:		Archiving/Cd burning
Requires:	%{name} = %{version}-%{release}

%description	audio-disc
Silicon application to create Audio discs:
* CDs
* DVDs
* Blu-Rays

%files		audio-disc
%{_libdir}/%{name}/apps/libAudioDisc.so

#-----------------------------------------------------

%package	converter
Summary:	Silicon converter
Group:		Archiving/Cd burning
Requires:	%{name} = %{version}-%{release}

%description	converter
Silicon application to convert your files to other
supported formats.

%files		converter
%{_libdir}/%{name}/apps/libConverter.so

#-----------------------------------------------------

%package	copy-disc
Summary:	Silicon copy disc
Group:		Archiving/Cd burning
Requires:	%{name} = %{version}-%{release}

%description	copy-disc
Silicon application to copy a disc to another disc.

%files		copy-disc
%{_libdir}/%{name}/apps/libCopyDisc.so

#-----------------------------------------------------

%package	database
Summary:	Silicon database
Group:		Archiving/Cd burning
Requires:	%{name} = %{version}-%{release}

%description	database
Silicon application to show informations and indexed data
that DiscScanner stored into the Silicon DataBase.

%files		database
%{_libdir}/%{name}/apps/libDataBase.so

#-----------------------------------------------------

%package	data-disc
Summary:	Silicon data disc
Group:		Archiving/Cd burning
Requires:	%{name} = %{version}-%{release}

%description	data-disc
Silicon application to burn data discs or to create data images.

%files		data-disc
%{_libdir}/%{name}/apps/libDataDisc.so

#-----------------------------------------------------

%package	disc-details
Summary:	Silicon disc details
Group:		Archiving/Cd burning
Requires:	%{name} = %{version}-%{release}

%description	disc-details
Silicon application to show disc, image or database disc details.

%files		disc-details
%{_libdir}/%{name}/apps/libDiscDetails.so

#-----------------------------------------------------

%package	disc-eraser
Summary:	Silicon disc eraser
Group:		Archiving/Cd burning
Requires:	%{name} = %{version}-%{release}

%description	disc-eraser
Silicon application to erase rw discs.

%files		disc-eraser
%{_libdir}/%{name}/apps/libDiscEraser.so

#-----------------------------------------------------

%package        disc-imaging
Summary:        Silicon disc imaging
Group:          Archiving/Cd burning
Requires:       %{name} = %{version}-%{release}

%description    disc-imaging
Silicon application to create images of your discs.

%files          disc-imaging
%{_libdir}/%{name}/apps/libDiscImaging.so

#-----------------------------------------------------

%package        disc-scanner
Summary:        Silicon disc scanner
Group:          Archiving/Cd burning
Requires:       %{name} = %{version}-%{release}

%description    disc-scanner
Silicon application to collect data from your discs to the
Silicon DataBase.

%files          disc-scanner
%{_libdir}/%{name}/apps/libDiscScanner.so

#-----------------------------------------------------

%package        image-burner
Summary:        Silicon app image burner
Group:          Archiving/Cd burning
Requires:       %{name} = %{version}-%{release}

%description    image-burner
Silicon application to burn a images to discs.

%files          image-burner
%{_libdir}/%{name}/apps/libImageBurner.so

#-----------------------------------------------------

%package        library
Summary:        Silicon app library
Group:          Archiving/Cd burning
Requires:       %{name} = %{version}-%{release}

%description    library
Silicon application to manage your iso images in a classic way.

%files          library
%{_libdir}/%{name}/apps/libLibrary.so

#-----------------------------------------------------

%package        limoo
Summary:        Silicon app limoo
Group:          Archiving/Cd burning
Requires:       %{name} = %{version}-%{release}

%description    limoo
Silicon application - Limoo image viewer.

%files          limoo
%{_libdir}/%{name}/apps/libLimoo.so

#-----------------------------------------------------

%package        mounter
Summary:        Silicon app mounter
Group:          Archiving/Cd burning
Requires:       %{name} = %{version}-%{release}

%description    mounter
Silicon application to mount/umount images easily.

%files          mounter
%{_libdir}/%{name}/apps/libMounter.so

#-----------------------------------------------------

%package        sample-app
Summary:        Silicon sample app
Group:          Archiving/Cd burning
Requires:       %{name} = %{version}-%{release}

%description    sample-app
Silicon sample application

%files          sample-app
%{_libdir}/%{name}/apps/libSampleApp.so

#-----------------------------------------------------

%package        script-runner
Summary:        Silicon app script runner
Group:          Archiving/Cd burning
Requires:       %{name} = %{version}-%{release}

%description    script-runner
%{summary}

%files          script-runner
%{_libdir}/%{name}/apps/libScriptRunner.so

#-----------------------------------------------------

%package        tagarg-player
Summary:        Silicon app tagarg player
Group:          Archiving/Cd burning
Requires:       %{name} = %{version}-%{release}

%description    tagarg-player
Silicon music player.

%files          tagarg-player
%{_libdir}/%{name}/apps/libTagargPlayer.so

#-----------------------------------------------------

%package	themes
Summary:	Silicon themes
Group:		Archiving/Cd burning
Requires:	%{name} = %{version}-%{release}

%description	themes
%{summary}

%files		themes
%{_datadir}/%{name}/themes/*

#-----------------------------------------------------

%package	plugin-lyric-browser
Summary:	Silicon lyric browser plugin
Group:		Archiving/Cd burning
Requires:	%{name} = %{version}-%{release}

%description	plugin-lyric-browser
%{summary}

%files		plugin-lyric-browser
%{_libdir}/%{name}/plugins/libLyricBrowser.so

#-----------------------------------------------------

%package	plugin-now-playing
Summary:	Silicon now playing plugin
Group:		Archiving/Cd burning
Requires:	%{name} = %{version}-%{release}

%description	plugin-now-playing
%{summary}

%files		plugin-now-playing
%{_libdir}/%{name}/plugins/libNowPlaying.so

#-----------------------------------------------------

%package	plugin-single-inner-dialog
Summary:	Silicon single inner dialog plugin
Group:		Archiving/Cd burning
Requires:	%{name} = %{version}-%{release}

%description	plugin-single-inner-dialog
%{summary}

%files		plugin-single-inner-dialog
%{_libdir}/%{name}/plugins/libSingleInnerDialog*.so

#-----------------------------------------------------

%package	plugin-system-tray
Summary:	Silicon system tray plugin
Group:		Archiving/Cd burning
Requires:	%{name} = %{version}-%{release}

%description	plugin-system-tray
%{summary}

%files		plugin-system-tray
%{_libdir}/%{name}/plugins/libSystemTray.so

#-----------------------------------------------------

%package	plugin-tagarg-audio-disc
Summary:	Silicon tagarg audio disc plugin
Group:		Archiving/Cd burning
Requires:	%{name} = %{version}-%{release}

%description	plugin-tagarg-audio-disc
%{summary}

%files		plugin-tagarg-audio-disc
%{_libdir}/%{name}/plugins/libTagargAudioDisc.so

#-----------------------------------------------------

%package	plugin-mpg123-audio-disc
Summary:	Silicon mpg123 audio disc plugin
Group:		Archiving/Cd burning
Requires:	%{name} = %{version}-%{release}

%description	plugin-mpg123-audio-disc
%{summary}

%files		plugin-mpg123-audio-disc
%{_libdir}/%{name}/plugins/libmpg123.so

#-----------------------------------------------------

%package	plugin-audio-cd-record
Summary:	CD record plugin
Group:		Archiving/Cd burning
Requires:	%{name} = %{version}-%{release}

%description	plugin-audio-cd-record
%{summary}

%files		plugin-audio-cd-record
%{_libdir}/%{name}/plugins/libAudioCdRecord.so
%{_libdir}/%{name}/plugins/libCdRecord.so
%{_libdir}/%{name}/plugins/libReadCd.so


#-----------------------------------------------------

%package	plugin-polkit-mount-root
Summary:	Polkit mount plugin
Group:		Archiving/Cd burning
Requires:	%{name} = %{version}-%{release}

%description	plugin-polkit-mount-root
%{summary}

%files		plugin-polkit-mount-root
%{_bindir}/%{name}_rootmount
%{_libdir}/%{name}/plugins/libRootMount.so

#-----------------------------------------------------

%package	plugin-cd-dvd-eraser
Summary:	CD and DVD eraser plugin
Group:		Archiving/Cd burning
Requires:	%{name} = %{version}-%{release}

%description	plugin-cd-dvd-eraser
%{summary}

%files		plugin-cd-dvd-eraser
%{_libdir}/%{name}/plugins/libMkIsoFs.so
%{_libdir}/%{name}/plugins/libMkDiscFs.so
%{_libdir}/%{name}/plugins/libEraser.so
