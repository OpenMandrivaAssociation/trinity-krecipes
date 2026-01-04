%bcond clang 1

# TDE variables
%define tde_epoch 2
%if "%{?tde_version}" == ""
%define tde_version 14.1.5
%endif
%define pkg_rel 5

%define tde_pkg krecipes

%define tde_prefix /opt/trinity

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


Source0:		https://mirror.ppa.trinitydesktop.org/trinity/releases/R%{tde_version}/main/applications/misc/%{tarball_name}-%{tde_version}%{?preversion:~%{preversion}}.tar.xz

BuildSystem:    cmake

BuildOption:    -DCMAKE_BUILD_TYPE="RelWithDebInfo"
BuildOption:    -DCMAKE_INSTALL_PREFIX=%{tde_prefix}
BuildOption:    -DCONFIG_INSTALL_DIR=%{_sysconfdir}/trinity
BuildOption:    -DINCLUDE_INSTALL_DIR=%{tde_prefix}/include/tde
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
export PATH="%{tde_prefix}/bin:${PATH}"
export PKG_CONFIG_PATH="%{tde_prefix}/%{_lib}/pkgconfig"


%install -a
# Remove unwanted pixmaps
%__rm -rf "%{buildroot}%{tde_prefix}/share/pixmaps/"

# Removes duplicate files
%fdupes "%{buildroot}%{tde_prefix}/share"


%files 
%defattr(-,root,root,-)
%{tde_prefix}/bin/krecipes
%{tde_prefix}/share/applications/tde/krecipes.desktop
%{tde_prefix}/share/apps/krecipes/
%{tde_prefix}/share/locale/
%{tde_prefix}/share/icons/crystalsvg/*/mimetypes/krecipes_file.png
%{tde_prefix}/share/icons/hicolor/*/apps/krecipes.png
%{tde_prefix}/share/mimelnk/application/x-krecipes-backup.desktop
%{tde_prefix}/share/mimelnk/application/x-krecipes-recipes.desktop
%lang(da) %{tde_prefix}/share/doc/tde/HTML/da/
%lang(en) %{tde_prefix}/share/doc/tde/HTML/en/
%lang(es) %{tde_prefix}/share/doc/tde/HTML/es/
%lang(et) %{tde_prefix}/share/doc/tde/HTML/et/
%lang(pt) %{tde_prefix}/share/doc/tde/HTML/pt/
%lang(sv) %{tde_prefix}/share/doc/tde/HTML/sv/
%{tde_prefix}/share/man/man1/krecipes.1*

