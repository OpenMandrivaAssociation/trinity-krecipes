%bcond clang 1

# TDE variables
%define tde_epoch 2
%if "%{?tde_version}" == ""
%define tde_version 14.1.5
%endif
%define pkg_rel 2

%define tde_pkg krecipes
%define tde_prefix /opt/trinity
%define tde_bindir %{tde_prefix}/bin
%define tde_datadir %{tde_prefix}/share
%define tde_docdir %{tde_datadir}/doc
%define tde_includedir %{tde_prefix}/include
%define tde_libdir %{tde_prefix}/%{_lib}
%define tde_mandir %{tde_datadir}/man
%define tde_tdeappdir %{tde_datadir}/applications/tde
%define tde_tdedocdir %{tde_docdir}/tde
%define tde_tdeincludedir %{tde_includedir}/tde
%define tde_tdelibdir %{tde_libdir}/trinity

%undefine __brp_remove_la_files
%define dont_remove_libtool_files 1
%define _disable_rebuild_configure 1

# fixes error: Empty %files file …/debugsourcefiles.list
%define _debugsource_template %{nil}

%define tarball_name %{tde_pkg}-trinity


Name:		trinity-%{tde_pkg}
Epoch:		%{tde_epoch}
Version:	1.0beta2
Release:	%{?tde_version}_%{?!preversion:%{pkg_rel}}%{?preversion:0_%{preversion}}%{?dist}
Summary:	Recipes manager for TDE
Group:		Applications/Utilities
URL:		http://www.trinitydesktop.org/

License:	GPLv2+

#Vendor:		Trinity Desktop
#Packager:	Francois Andriot <francois.andriot@free.fr>

Prefix:		%{tde_prefix}

Source0:		https://mirror.ppa.trinitydesktop.org/trinity/releases/R%{tde_version}/main/applications/misc/%{tarball_name}-%{tde_version}%{?preversion:~%{preversion}}.tar.xz

BuildSystem:    cmake
BuildOption:    -DCMAKE_BUILD_TYPE="RelWithDebInfo"
BuildOption:    -DCMAKE_SKIP_RPATH=OFF
BuildOption:    -DCMAKE_SKIP_INSTALL_RPATH=OFF
BuildOption:    -DCMAKE_BUILD_WITH_INSTALL_RPATH=ON
BuildOption:    -DCMAKE_INSTALL_RPATH="%{tde_libdir}"
BuildOption:    -DCMAKE_NO_BUILTIN_CHRPATH=ON
BuildOption:    -DBIN_INSTALL_DIR=%{tde_bindir}
BuildOption:    -DCONFIG_INSTALL_DIR="%{tde_confdir}"
BuildOption:    -DINCLUDE_INSTALL_DIR=%{tde_tdeincludedir}
BuildOption:    -DLIB_INSTALL_DIR=%{tde_libdir}
BuildOption:    -DSHARE_INSTALL_PREFIX=%{tde_datadir}
BuildOption:    -DWITH_ALL_OPTIONS=ON -DBUILD_ALL=ON

BuildRequires:	trinity-tdelibs-devel >= %{tde_version}
BuildRequires:	desktop-file-utils
BuildRequires:	gettext

%{!?with_clang:BuildRequires:	gcc-c++}

BuildRequires:	pkgconfig
BuildRequires:	fdupes

# MYSQL support
BuildRequires:	pkgconfig(mariadb)

# POSTGRESQL support
BuildRequires:	pkgconfig(libpq)

# SQLITE3 support
BuildRequires:  pkgconfig(sqlite3)

BuildRequires:  pkgconfig(xrender)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(ice)
BuildRequires:  pkgconfig(sm)


%description
Krecipes is a TDE application designed to manage recipes. It can help you to
do your shopping list, search through your recipes to find what you can do
with available ingredients and a diet helper. It can also import or export
recipes from files in various format (eg RecipeML or Meal-Master) or from
databases.


%conf -p
unset QTDIR QTINC QTLIB
export PATH="%{tde_bindir}:${PATH}"
export PKG_CONFIG_PATH="%{tde_libdir}/pkgconfig"


%install -a
# Remove unwanted pixmaps
%__rm -rf "%{buildroot}%{tde_datadir}/pixmaps/"

# Removes duplicate files
%fdupes "%{buildroot}%{tde_datadir}"


%files 
%defattr(-,root,root,-)
%{tde_bindir}/krecipes
%{tde_tdeappdir}/krecipes.desktop
%{tde_datadir}/apps/krecipes/
%{tde_datadir}/locale/
%{tde_datadir}/icons/crystalsvg/*/mimetypes/krecipes_file.png
%{tde_datadir}/icons/hicolor/*/apps/krecipes.png
%{tde_datadir}/mimelnk/application/x-krecipes-backup.desktop
%{tde_datadir}/mimelnk/application/x-krecipes-recipes.desktop
%lang(da) %{tde_tdedocdir}/HTML/da/
%lang(en) %{tde_tdedocdir}/HTML/en/
%lang(es) %{tde_tdedocdir}/HTML/es/
%lang(et) %{tde_tdedocdir}/HTML/et/
%lang(pt) %{tde_tdedocdir}/HTML/pt/
%lang(sv) %{tde_tdedocdir}/HTML/sv/
%{tde_mandir}/man1/krecipes.1*

