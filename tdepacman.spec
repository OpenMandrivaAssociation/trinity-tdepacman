#
# Please submit bugfixes or comments via http://www.trinitydesktop.org/
#

# Default version for this component
%define tde_pkg tdepacman
%if "%{?tde_version}" == ""
%define tde_version 14.1.5
%endif

# TDE specific building variables
%define tde_prefix /opt/trinity
%define tde_bindir %{tde_prefix}/bin
%define tde_confdir %{_sysconfdir}/trinity
%define tde_datadir %{tde_prefix}/share
%define tde_docdir %{tde_datadir}/doc
%define tde_includedir %{tde_prefix}/include
%define tde_libdir %{tde_prefix}/%{_lib}
%define tde_mandir %{tde_datadir}/man
%define tde_appdir %{tde_datadir}/applications

%define tde_tdeappdir %{tde_appdir}/tde
%define tde_tdedocdir %{tde_docdir}/tde
%define tde_tdeincludedir %{tde_includedir}/tde
%define tde_tdelibdir %{tde_libdir}/trinity

%define _docdir %{tde_docdir}

%if 0%{?mdkversion}
%undefine __brp_remove_la_files
%define dont_remove_libtool_files 1
%define _disable_rebuild_configure 1
%endif

# fixes error: Empty %files file …/debugsourcefiles.list
%define _debugsource_template %{nil}

%define tarball_name %{tde_pkg}-trinity
%global toolchain %(readlink /usr/bin/cc)


Name:			trinity-%{tde_pkg}
Summary:		A pacman game for the Trinity Desktop
Version:		0.3.2
Release:		%{?tde_version}_%{?!preversion:1}%{?preversion:0_%{preversion}}%{?dist}

License:		GPLv2+
Group:			Applications/Utilities

Vendor:			Trinity Project
Packager:		Francois Andriot <francois.andriot@free.fr>
URL:			http://www.trinitydesktop.org/

Source0:		https://mirror.ppa.trinitydesktop.org/trinity/releases/R%{tde_version}/main/applications/games/%{tarball_name}-%{tde_version}%{?preversion:~%{preversion}}.tar.xz

BuildRequires:  cmake make
BuildRequires:	trinity-tqtinterface-devel >= %{tde_version}
BuildRequires:	trinity-arts-devel >= 1:1.5.10
BuildRequires:	trinity-tdelibs-devel >= %{tde_version}
BuildRequires:	trinity-tdebase-devel >= %{tde_version}
BuildRequires:	trinity-tdegames-devel >= %{tde_version}
BuildRequires:	desktop-file-utils

BuildRequires:	gettext

BuildRequires:	trinity-tde-cmake >= %{tde_version}
%if "%{?toolchain}" != "clang"
BuildRequires:	gcc-c++
%endif
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

%if 0%{?suse_version} || 0%{?pclinuxos}
%debug_package
%endif


%prep
%autosetup -n %{tarball_name}-%{tde_version}%{?preversion:~%{preversion}}


%build
unset QTDIR QTINC QTLIB
export PATH="%{tde_bindir}:${PATH}"
export PKG_CONFIG_PATH="%{tde_libdir}/pkgconfig"

if ! rpm -E %%cmake|grep -e 'cd build\|cd ${CMAKE_BUILD_DIR:-build}'; then
  %__mkdir_p build
  cd build
fi

%cmake \
  -DCMAKE_BUILD_TYPE="RelWithDebInfo" \
  -DCMAKE_C_FLAGS="${RPM_OPT_FLAGS}" \
  -DCMAKE_CXX_FLAGS="${RPM_OPT_FLAGS}" \
  -DCMAKE_SKIP_RPATH=OFF \
  -DCMAKE_SKIP_INSTALL_RPATH=OFF \
  -DCMAKE_INSTALL_RPATH="%{tde_libdir}" \
  -DCMAKE_VERBOSE_MAKEFILE=ON \
  -DWITH_GCC_VISIBILITY=OFF \
  \
  -DCMAKE_INSTALL_PREFIX=%{tde_prefix} \
  -DSHARE_INSTALL_PREFIX=%{tde_datadir} \
  -DDATA_INSTALL_DIR=%{tde_datadir}/apps \
  -DLIB_INSTALL_DIR=%{tde_libdir} \
  -DBUILD_ALL=ON \
  ..

%__make %{?_smp_mflags}


%install
export PATH="%{tde_bindir}:${PATH}"
%__make install DESTDIR=%{buildroot} -C build

%find_lang %{tde_pkg}


%files -f %{tde_pkg}.lang
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING README.md TODO
%{tde_bindir}/tdepacman
%{tde_tdeappdir}/tdepacman.desktop
%{tde_datadir}/apps/tdepacman/
%dir %{tde_datadir}/config
%{tde_datadir}/config/tdepacmanrc
%lang(de) %{tde_tdedocdir}/HTML/de/tdepacman/
%{tde_tdedocdir}/HTML/en/tdepacman/
%{tde_datadir}/icons/hicolor/16x16/apps/tdepacman.png
%{tde_datadir}/icons/hicolor/32x32/apps/tdepacman.png
%{tde_datadir}/icons/locolor/16x16/apps/tdepacman.png
%{tde_datadir}/icons/locolor/32x32/apps/tdepacman.png
%{tde_mandir}/man1/tdepacman.1*

