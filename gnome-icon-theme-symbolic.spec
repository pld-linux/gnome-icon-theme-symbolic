Summary:	Default symbolic icon themes for GNOME environment
Summary(pl.UTF-8):	Domyślne motywy ikon symbolicznych dla środowiska GNOME
Name:		gnome-icon-theme-symbolic
Version:	3.6.2
Release:	1
License:	GPL
Group:		Themes
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-icon-theme-symbolic/3.6/%{name}-%{version}.tar.xz
# Source0-md5:	5c6a3834d50a14ff3c6d65513ac36eb4
URL:		http://www.gnome.org/
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake >= 1:1.9
BuildRequires:	icon-naming-utils >= 0.8.7
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	rpmbuild(macros) >= 1.601
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires(post,postun):	gtk-update-icon-cache
Requires:	gnome-icon-theme >= 3.6.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Default symbolic icon themes for GNOME environment.

%description -l pl.UTF-8
Domyślne motywy ikon symbolicznych dla środowiska GNOME.

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	GTK_UPDATE_ICON_CACHE=/bin/true
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	install_sh="install -p" \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache gnome

%postun
%update_icon_cache gnome

%files
%defattr(644,root,root,755)
%doc AUTHORS README
%dir %{_iconsdir}/gnome/scalable
%dir %{_iconsdir}/gnome/scalable/actions
%dir %{_iconsdir}/gnome/scalable/apps
%dir %{_iconsdir}/gnome/scalable/categories
%dir %{_iconsdir}/gnome/scalable/devices
%dir %{_iconsdir}/gnome/scalable/emblems
%dir %{_iconsdir}/gnome/scalable/emotes
%dir %{_iconsdir}/gnome/scalable/mimetypes
%dir %{_iconsdir}/gnome/scalable/places
%dir %{_iconsdir}/gnome/scalable/status
%{_iconsdir}/gnome/scalable/*/*.svg
