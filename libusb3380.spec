%define commit c83d1e93eb3a5b8b6a9db41c2613b206f344f825
%define major 0
%define libname %mklibname usb3380 %{major}
%define devname %mklibname -d usb3380

Name:           libusb3380
Version:        0.0.0+git.20190126
Release:        1.1
Summary:        USB3380 abstraction layer for libusb
License:        LGPL-2.1-only
Group:          Development/Libraries/C and C++
URL:            http://xtrx.io
#Git-Clone:     https://github.com/xtrx-sdr/libusb3380.git
Source0:	https://github.com/xtrx-sdr/libusb3380/archive/%{commit}.zip
Patch0:         libusb3380-cmake-fix-compiler-setup.patch
BuildRequires:  cmake
BuildRequires:  git-core
BuildRequires:  pkgconfig(libusb-1.0)

%description
USB3380 abstraction layer for libusb.

%package -n %{libname}
Summary:        USB3380 abstraction layer for libusb
Group:          System/Libraries

%description -n %{libname}
USB3380 abstraction layer for libusb.

%package -n	%{devname}
Summary:        Development files for libusb3380
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %{EVRD}
Requires:       pkgconfig(libusb-1.0)

%description -n	%{devname}
USB3380 abstraction layer for libusb.

This subpackage contains libraries and header files for developing
applications that want to make use of libusb3380.

%prep
%setup -q -n %{name}-%{commit}
%autopatch -p1

%build
export CFLAGS="%{optflags} -pthread"
%cmake
%make_build LIBS="-pthread"

%install
%make_install -C build

%files -n %{libname}
%{_libdir}/libusb3380.so.%{major}*

%files -n %{devname}
%license LICENSE
%doc README.md
%{_includedir}/libusb3380.h
%{_libdir}/libusb3380.so
%{_libdir}/pkgconfig/libusb3380.pc
