%global debug_package %{nil}

Name:    mytetra
Version: 1.44.28
Release: 0%{?dist}
License: GPLv3
Group:   System/X11/Utilities
Summary: Personal manager for information accumulation
URL:     https://github.com/xintrea/mytetra_dev
Source0: %{url}/archive/v.%{version}.tar.gz

BuildRequires: gcc-c++
BuildRequires: qt5-qtbase-devel >= 5.2
BuildRequires: qt5-qtsvg-devel >= 5.2

%description
MyTetra is a full-featured, open source, cross-platform note 
manager (PIM-manager) used to collect and accumulate various 
kinds of information. All entries (notes, articles) are organized 
in a tree structure, as well as supplied with keywords tags that 
allow you to quickly find the right entries. Links between records, 
attachments, encryption, detailed search, synchronization, copying 
from the browser, one of the best visual WYSIWYG text editors - all 
this is in the PIM-manager MyTetra. It is powerful program for data 
memorization and structuring notes.

Features:
  * Infinite ramify tree for notes group
  * Arbitrary sorted notes at his branch
  * Arbitrary sorted branches at parent branch
  * Copy/Paste for notes and branches
  * Clickable tags
  * Customizable trash for recovery lost data
  * WYSIWYG editor
  * Notes encryption by RC5-32/12/16 + PBKDF2
  * Synchronization over any cloud storage system or version 
    control system (i.e. Git on GitHub.com)
  * History navigation
  * etc.

%prep
%setup -q -c -n %{name}-%{version}

%build
cd %{name}_dev-v.%{version}
sed -ri 's|/usr/local/bin|%{_bindir}|' mytetra.pro
qmake-qt5 mytetra.pro \
  QMAKE_CFLAGS="%{optflags}" \
  QMAKE_CXXFLAGS="%{optflags}" \
  QMAKE_LDFLAGS="-Wl,--as-needed -Wl,--strip-all" PREFIX=%{_prefix}
make

%install
cd %{name}_dev-v.%{version}
make install INSTALL_ROOT=%{buildroot}

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/*
%{_datadir}/applications/mytetra.desktop
%{_datadir}/icons/hicolor/48x48/apps/mytetra.png
%{_datadir}/icons/hicolor/scalable/apps/mytetra.svg
%dir /usr/share/icons/hicolor/
%dir /usr/share/icons/hicolor/48x48/
%dir /usr/share/icons/hicolor/48x48/apps/
%dir /usr/share/icons/hicolor/scalable/
%dir /usr/share/icons/hicolor/scalable/apps/

%changelog
