# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.27
# 

Name:       ktextwidgets

# >> macros
# << macros

Summary:    KDE Frameworks 5 Tier 3 addon with text widgets
Version:    5.3.0
Release:    1
Group:      System/Base
License:    GPLv2+
URL:        http://www.kde.org
Source0:    %{name}-%{version}.tar.xz
Source100:  ktextwidgets.yaml
Source101:  ktextwidgets-rpmlintrc
Requires:   kf5-filesystem
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Xml)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5Concurrent)
BuildRequires:  pkgconfig(Qt5Test)
BuildRequires:  kf5-rpm-macros
BuildRequires:  extra-cmake-modules
BuildRequires:  kcompletion-devel
BuildRequires:  kconfig-devel
BuildRequires:  kconfigwidgets-devel
BuildRequires:  ki18n-devel
BuildRequires:  kiconthemes-devel
BuildRequires:  kservice-devel
BuildRequires:  kwidgetsaddons-devel
BuildRequires:  kwindowsystem-devel
BuildRequires:  sonnet-devel

%description
KDE Frameworks 5 Tier 3 addon with text widgets.


%package devel
Summary:    Development files for %{name}
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}
Requires:   kcompletion-devel
Requires:   kconfig-devel
Requires:   kconfigwidgets-devel
Requires:   ki18n-devel
Requires:   kiconthemes-devel
Requires:   kservice-devel
Requires:   kwidgetsaddons-devel
Requires:   kwindowsystem-devel
Requires:   sonnet-devel

%description devel
The %{name}-devel package contains the files necessary to develop applications
that use %{name}.


%prep
%setup -q -n %{name}-%{version}

# >> setup
# << setup

%build
# >> build pre
%kf5_make
# << build pre



# >> build post
# << build post

%install
rm -rf %{buildroot}
# >> install pre
%kf5_make_install
# << install pre

# >> install post
# << install post

%files
%defattr(-,root,root,-)
%doc COPYING.LIB README.md
%{_kf5_libdir}/libKF5TextWidgets.so.*
%{_kf5_servicetypesdir}/*.desktop
# >> files
# << files

%files devel
%defattr(-,root,root,-)
%{_kf5_includedir}/ktextwidgets_version.h
%{_kf5_includedir}/KTextWidgets
%{_kf5_libdir}/libKF5TextWidgets.so
%{_kf5_cmakedir}/KF5TextWidgets
%{_kf5_mkspecsdir}/qt_KTextWidgets.pri
# >> files devel
# << files devel
