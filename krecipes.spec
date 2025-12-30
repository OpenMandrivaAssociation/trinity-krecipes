%bcond clang 1

# TDE variables
%define tde_epoch 2
%if "%{?tde_version}" == ""
%define tde_version 14.1.5
%endif
%define pkg_rel 3

%define tde_pkg krecipes


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

Prefix:		/opt/trinity

Source0:		https://mirror.ppa.trinitydesktop.org/trinity/releases/R%{tde_version}/main/applications/misc/%{tarball_name}-%{tde_version}%{?preversion:~%{preversion}}.tar.xz

BuildSystem:    cmake
BuildOption:    -DCMAKE_BUILD_TYPE="RelWithDebInfo"
BuildOption:    -DCMAKE_SKIP_RPATH=OFF
BuildOption:    -DCMAKE_SKIP_INSTALL_RPATH=OFF
BuildOption:    -DCMAKE_BUILD_WITH_INSTALL_RPATH=ON
BuildOption:    -DCMAKE_INSTALL_RPATH=%{prefix}/%{_lib}
BuildOption:    -DBIN_INSTALL_DIR=%{prefix}/bin
BuildOption:    -DCONFIG_INSTALL_DIR=%{_sysconfdir}/trinity
BuildOption:    -DINCLUDE_INSTALL_DIR=%{prefix}/include/tde
BuildOption:    -DLIB_INSTALL_DIR=%{prefix}/%{_lib}
BuildOption:    -DSHARE_INSTALL_PREFIX=%{prefix}/share
BuildOption:    -DWITH_ALL_OPTIONS=ON -DBUILD_ALL=ON
BuildOption:    -DWITH_GCC_VISIBILITY=%{!?with_clang:ON}%{?with_clang:OFF}

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
export PATH="%{prefix}/bin:${PATH}"
export PKG_CONFIG_PATH="%{prefix}/%{_lib}/pkgconfig"


%install -a
# Remove unwanted pixmaps
%__rm -rf "%{buildroot}%{prefix}/share/pixmaps/"

# Removes duplicate files
%fdupes "%{buildroot}%{prefix}/share"


%files 
%defattr(-,root,root,-)
%{prefix}/bin/krecipes
%{prefix}/share/applications/tde/krecipes.desktop
%{prefix}/share/apps/krecipes/
%{prefix}/share/locale/
%{prefix}/share/icons/crystalsvg/*/mimetypes/krecipes_file.png
%{prefix}/share/icons/hicolor/*/apps/krecipes.png
%{prefix}/share/mimelnk/application/x-krecipes-backup.desktop
%{prefix}/share/mimelnk/application/x-krecipes-recipes.desktop
%lang(da) %{prefix}/share/doc/tde/HTML/da/
%lang(en) %{prefix}/share/doc/tde/HTML/en/
%lang(es) %{prefix}/share/doc/tde/HTML/es/
%lang(et) %{prefix}/share/doc/tde/HTML/et/
%lang(pt) %{prefix}/share/doc/tde/HTML/pt/
%lang(sv) %{prefix}/share/doc/tde/HTML/sv/
%{prefix}/share/man/man1/krecipes.1*

