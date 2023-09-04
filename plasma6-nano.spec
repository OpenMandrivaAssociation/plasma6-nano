%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)
%define git 20230902

Name:		plasma6-nano
Version:	5.240.0
Release:	%{?git:0.%{git}.}1
Summary:	Plasma interface for embedded devices
%if 0%{?git:1}
Source0:	https://invent.kde.org/plasma/plasma-nano/-/archive/master/plasma-nano-master.tar.bz2#/plasma-nano-%{git}.tar.bz2
%else
Source0:	http://download.kde.org/%{stable}/plasma/%(echo %{version} |cut -d. -f1-3)/%{name}-%{version}.tar.xz
%endif
License:	GPLv2/LGPLv2/LGPLv2.1
Group:		Graphical desktop/KDE
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt6)
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6Gui)
BuildRequires:	cmake(Qt6Quick)
BuildRequires:	cmake(Qt6Qml)
BuildRequires:	cmake(Qt6Svg)
BuildRequires:	cmake(Qt6Test)
BuildRequires:	cmake(KF6Plasma)
BuildRequires:	cmake(KF6WindowSystem)
BuildRequires:	cmake(KF6Wayland)
BuildRequires:	cmake(KF6I18n)
BuildRequires:	cmake(KF6Svg)
BuildRequires:	cmake(KF6Service)
BuildRequires:	cmake(KF6ItemModels)
BuildRequires:	plasma6-xdg-desktop-portal-kde

%description
Plasma interface for embedded devices.

%prep
%autosetup -p1 -n plasma-nano-%{?git:master}%{!?git:%{version}}
%cmake \
	-DBUILD_QCH:BOOL=ON \
	-DBUILD_WITH_QT6:BOOL=ON \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build
%find_lang plasma-nano --all-name --with-html

%files -f plasma-nano.lang
%{_qtdir}/qml/org/kde/plasma/private/nanoshell
%{_datadir}/plasma/packages/org.kde.plasma.nano.desktoptoolbox
%{_datadir}/plasma/shells/org.kde.plasma.nano
%{_datadir}/metainfo/org.kde.plasma.nano.desktoptoolbox.appdata.xml
