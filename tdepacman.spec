%bcond clang 1

# Default version for this component
%define tde_pkg tdepacman
%if "%{?tde_version}" == ""
%define tde_version 14.1.5
%endif
%define pkg_rel 2

# TDE specific building variables
%define tde_prefix /opt/trinity


%undefine __brp_remove_la_files
%define dont_remove_libtool_files 1
%define _disable_rebuild_configure 1

# fixes error: Empty %files file …/debugsourcefiles.list
%define _debugsource_template %{nil}

%define tarball_name %{tde_pkg}-trinity


Name:			trinity-%{tde_pkg}
Summary:		A pacman game for the Trinity Desktop
Version:		0.3.2
Release:		%{?tde_version}_%{?!preversion:%{pkg_rel}}%{?preversion:0_%{preversion}}%{?dist}

License:		GPLv2+
Group:			Applications/Utilities


URL:			http://www.trinitydesktop.org/

Source0:		https://mirror.ppa.trinitydesktop.org/trinity/releases/R%{tde_version}/main/applications/games/%{tarball_name}-%{tde_version}%{?preversion:~%{preversion}}.tar.xz

BuildSystem:    cmake

BuildOption:    -DCMAKE_BUILD_TYPE="RelWithDebInfo"
BuildOption:    -DCMAKE_INSTALL_PREFIX=%{tde_prefix}
BuildOption:    -DSHARE_INSTALL_PREFIX=%{tde_prefix}/share
BuildOption:    -DDATA_INSTALL_DIR=%{tde_prefix}/share/apps
BuildOption:    -DBUILD_ALL=ON

BuildRequires:	trinity-tqtinterface-devel >= %{tde_version}
BuildRequires:	trinity-arts-devel >= 1:1.5.10
BuildRequires:	trinity-tdelibs-devel >= %{tde_version}
BuildRequires:	trinity-tdebase-devel >= %{tde_version}
BuildRequires:	trinity-tdegames-devel >= %{tde_version}
BuildRequires:	desktop-file-utils

BuildRequires:	gettext

BuildRequires:	trinity-tde-cmake >= %{tde_version}

%{!?with_clang:BuildRequires:	gcc-c++}

BuildRequires:	pkgconfig
BuildRequires:	libtool

BuildRequires:  pkgconfig(xrender)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(ice)
BuildRequires:  pkgconfig(sm)


%description
Pacman is a legendary game with an enthusiastic following from around 
the world. Since its introduction in 1980, Pacman's image has been 
splashed across magazine covers, television screens, T-shirts, and 
bumper stickers. Created by Japan's Namco, and distributed in the 
United States by Bally, Pacman is an icon of 1980's popular culture


%conf -p
unset QTDIR QTINC QTLIB
export PATH="%{tde_prefix}/bin:${PATH}"
export PKG_CONFIG_PATH="%{tde_prefix}/%{_lib}/pkgconfig"

%install -a
%find_lang %{tde_pkg}


%files -f %{tde_pkg}.lang
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING README.md TODO
%{tde_prefix}/bin/tdepacman
%{tde_prefix}/share/applications/tde/tdepacman.desktop
%{tde_prefix}/share/apps/tdepacman/
%dir %{tde_prefix}/share/config
%{tde_prefix}/share/config/tdepacmanrc
%lang(de) %{tde_prefix}/share/doc/tde/HTML/de/tdepacman/
%{tde_prefix}/share/doc/tde/HTML/en/tdepacman/
%{tde_prefix}/share/icons/hicolor/16x16/apps/tdepacman.png
%{tde_prefix}/share/icons/hicolor/32x32/apps/tdepacman.png
%{tde_prefix}/share/icons/locolor/16x16/apps/tdepacman.png
%{tde_prefix}/share/icons/locolor/32x32/apps/tdepacman.png
%{tde_prefix}/share/man/man1/tdepacman.1*

