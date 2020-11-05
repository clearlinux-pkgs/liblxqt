#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xBE793007AD22DF7E (tsujan2000@gmail.com)
#
Name     : liblxqt
Version  : 0.16.0
Release  : 7
URL      : https://github.com/lxqt/liblxqt/releases/download/0.16.0/liblxqt-0.16.0.tar.xz
Source0  : https://github.com/lxqt/liblxqt/releases/download/0.16.0/liblxqt-0.16.0.tar.xz
Source1  : https://github.com/lxqt/liblxqt/releases/download/0.16.0/liblxqt-0.16.0.tar.xz.asc
Summary  : No detailed summary available
Group    : Development/Tools
License  : LGPL-2.1
Requires: liblxqt-bin = %{version}-%{release}
Requires: liblxqt-data = %{version}-%{release}
Requires: liblxqt-lib = %{version}-%{release}
Requires: liblxqt-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : kwindowsystem-dev
BuildRequires : libX11-dev libICE-dev libSM-dev libXau-dev libXcomposite-dev libXcursor-dev libXdamage-dev libXdmcp-dev libXext-dev libXfixes-dev libXft-dev libXi-dev libXinerama-dev libXi-dev libXmu-dev libXpm-dev libXrandr-dev libXrender-dev libXres-dev libXScrnSaver-dev libXt-dev libXtst-dev libXv-dev libXxf86misc-dev libXxf86vm-dev
BuildRequires : libqtxdg-dev
BuildRequires : lxqt-build-tools
BuildRequires : polkit-dev
BuildRequires : polkit-qt-dev
BuildRequires : qtbase-dev mesa-dev

%description
# liblxqt
## Overview
`liblxqt` represents the core library of LXQt providing essential functionality
needed by nearly all of its components.

%package bin
Summary: bin components for the liblxqt package.
Group: Binaries
Requires: liblxqt-data = %{version}-%{release}
Requires: liblxqt-license = %{version}-%{release}

%description bin
bin components for the liblxqt package.


%package data
Summary: data components for the liblxqt package.
Group: Data

%description data
data components for the liblxqt package.


%package dev
Summary: dev components for the liblxqt package.
Group: Development
Requires: liblxqt-lib = %{version}-%{release}
Requires: liblxqt-bin = %{version}-%{release}
Requires: liblxqt-data = %{version}-%{release}
Provides: liblxqt-devel = %{version}-%{release}
Requires: liblxqt = %{version}-%{release}

%description dev
dev components for the liblxqt package.


%package lib
Summary: lib components for the liblxqt package.
Group: Libraries
Requires: liblxqt-data = %{version}-%{release}
Requires: liblxqt-license = %{version}-%{release}

%description lib
lib components for the liblxqt package.


%package license
Summary: license components for the liblxqt package.
Group: Default

%description license
license components for the liblxqt package.


%prep
%setup -q -n liblxqt-0.16.0
cd %{_builddir}/liblxqt-0.16.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1604538789
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1604538789
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/liblxqt
cp %{_builddir}/liblxqt-0.16.0/COPYING %{buildroot}/usr/share/package-licenses/liblxqt/7fab4cd4eb7f499d60fe183607f046484acd6e2d
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/lxqt-backlight_backend

%files data
%defattr(-,root,root,-)
/usr/share/lxqt/power.conf
/usr/share/lxqt/translations/liblxqt/liblxqt_ar.qm
/usr/share/lxqt/translations/liblxqt/liblxqt_arn.qm
/usr/share/lxqt/translations/liblxqt/liblxqt_ast.qm
/usr/share/lxqt/translations/liblxqt/liblxqt_bg.qm
/usr/share/lxqt/translations/liblxqt/liblxqt_ca.qm
/usr/share/lxqt/translations/liblxqt/liblxqt_cs.qm
/usr/share/lxqt/translations/liblxqt/liblxqt_cy.qm
/usr/share/lxqt/translations/liblxqt/liblxqt_da.qm
/usr/share/lxqt/translations/liblxqt/liblxqt_de.qm
/usr/share/lxqt/translations/liblxqt/liblxqt_el.qm
/usr/share/lxqt/translations/liblxqt/liblxqt_en_GB.qm
/usr/share/lxqt/translations/liblxqt/liblxqt_eo.qm
/usr/share/lxqt/translations/liblxqt/liblxqt_es.qm
/usr/share/lxqt/translations/liblxqt/liblxqt_es_VE.qm
/usr/share/lxqt/translations/liblxqt/liblxqt_eu.qm
/usr/share/lxqt/translations/liblxqt/liblxqt_fi.qm
/usr/share/lxqt/translations/liblxqt/liblxqt_fr.qm
/usr/share/lxqt/translations/liblxqt/liblxqt_gl.qm
/usr/share/lxqt/translations/liblxqt/liblxqt_he.qm
/usr/share/lxqt/translations/liblxqt/liblxqt_hr.qm
/usr/share/lxqt/translations/liblxqt/liblxqt_hu.qm
/usr/share/lxqt/translations/liblxqt/liblxqt_ia.qm
/usr/share/lxqt/translations/liblxqt/liblxqt_id.qm
/usr/share/lxqt/translations/liblxqt/liblxqt_it.qm
/usr/share/lxqt/translations/liblxqt/liblxqt_ja.qm
/usr/share/lxqt/translations/liblxqt/liblxqt_ko.qm
/usr/share/lxqt/translations/liblxqt/liblxqt_lt.qm
/usr/share/lxqt/translations/liblxqt/liblxqt_lv.qm
/usr/share/lxqt/translations/liblxqt/liblxqt_nb_NO.qm
/usr/share/lxqt/translations/liblxqt/liblxqt_nl.qm
/usr/share/lxqt/translations/liblxqt/liblxqt_pl.qm
/usr/share/lxqt/translations/liblxqt/liblxqt_pt.qm
/usr/share/lxqt/translations/liblxqt/liblxqt_pt_BR.qm
/usr/share/lxqt/translations/liblxqt/liblxqt_ro_RO.qm
/usr/share/lxqt/translations/liblxqt/liblxqt_ru.qm
/usr/share/lxqt/translations/liblxqt/liblxqt_sk_SK.qm
/usr/share/lxqt/translations/liblxqt/liblxqt_sl.qm
/usr/share/lxqt/translations/liblxqt/liblxqt_sr@latin.qm
/usr/share/lxqt/translations/liblxqt/liblxqt_sr_RS.qm
/usr/share/lxqt/translations/liblxqt/liblxqt_th_TH.qm
/usr/share/lxqt/translations/liblxqt/liblxqt_tr.qm
/usr/share/lxqt/translations/liblxqt/liblxqt_uk.qm
/usr/share/lxqt/translations/liblxqt/liblxqt_zh_CN.qm
/usr/share/lxqt/translations/liblxqt/liblxqt_zh_TW.qm
/usr/share/polkit-1/actions/org.lxqt.backlight.pkexec.policy

%files dev
%defattr(-,root,root,-)
/usr/include/lxqt/LXQt/Application
/usr/include/lxqt/LXQt/AutostartEntry
/usr/include/lxqt/LXQt/Backlight
/usr/include/lxqt/LXQt/ConfigDialog
/usr/include/lxqt/LXQt/ConfigDialogCmdLineOptions
/usr/include/lxqt/LXQt/Globals
/usr/include/lxqt/LXQt/GridLayout
/usr/include/lxqt/LXQt/HtmlDelegate
/usr/include/lxqt/LXQt/Notification
/usr/include/lxqt/LXQt/PageSelectWidget
/usr/include/lxqt/LXQt/PluginInfo
/usr/include/lxqt/LXQt/Power
/usr/include/lxqt/LXQt/PowerManager
/usr/include/lxqt/LXQt/ProgramFinder
/usr/include/lxqt/LXQt/RotatedWidget
/usr/include/lxqt/LXQt/ScreenSaver
/usr/include/lxqt/LXQt/Settings
/usr/include/lxqt/LXQt/SingleApplication
/usr/include/lxqt/LXQt/Translator
/usr/include/lxqt/LXQt/lxqtapplication.h
/usr/include/lxqt/LXQt/lxqtautostartentry.h
/usr/include/lxqt/LXQt/lxqtbacklight.h
/usr/include/lxqt/LXQt/lxqtconfigdialog.h
/usr/include/lxqt/LXQt/lxqtconfigdialogcmdlineoptions.h
/usr/include/lxqt/LXQt/lxqtglobals.h
/usr/include/lxqt/LXQt/lxqtgridlayout.h
/usr/include/lxqt/LXQt/lxqthtmldelegate.h
/usr/include/lxqt/LXQt/lxqtnotification.h
/usr/include/lxqt/LXQt/lxqtpageselectwidget.h
/usr/include/lxqt/LXQt/lxqtplugininfo.h
/usr/include/lxqt/LXQt/lxqtpower.h
/usr/include/lxqt/LXQt/lxqtpowermanager.h
/usr/include/lxqt/LXQt/lxqtprogramfinder.h
/usr/include/lxqt/LXQt/lxqtrotatedwidget.h
/usr/include/lxqt/LXQt/lxqtscreensaver.h
/usr/include/lxqt/LXQt/lxqtsettings.h
/usr/include/lxqt/LXQt/lxqtsingleapplication.h
/usr/include/lxqt/LXQt/lxqttranslator.h
/usr/lib64/liblxqt.so
/usr/lib64/pkgconfig/lxqt.pc
/usr/share/cmake/lxqt/lxqt-config-version.cmake
/usr/share/cmake/lxqt/lxqt-config.cmake
/usr/share/cmake/lxqt/lxqt-targets-relwithdebinfo.cmake
/usr/share/cmake/lxqt/lxqt-targets.cmake

%files lib
%defattr(-,root,root,-)
/usr/lib64/liblxqt.so.0
/usr/lib64/liblxqt.so.0.16.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/liblxqt/7fab4cd4eb7f499d60fe183607f046484acd6e2d
