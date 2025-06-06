%define name SDL2_mixer
%define version 2.9.0
%define release 1

Summary: Simple DirectMedia Layer - Sample Mixer Library
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{version}.tar.gz
License: LGPL
Group: System Environment/Libraries
BuildRoot: /var/tmp/%{name}-buildroot
Prefix: %{_prefix}

%description
Due to popular demand, here is a simple multi-channel audio mixer.
It supports 4 channels of 16 bit stereo audio, plus a single channel
of music, mixed by the popular ModPlug, Timidity MIDI, Ogg Vorbis,
Tremor, and libmpg123 MP3 libraries.

%package devel
Summary: Libraries, includes and more to develop SDL applications.
Group: Development/Libraries
Requires: %{name}

%description devel
Due to popular demand, here is a simple multi-channel audio mixer.
It supports 4 channels of 16 bit stereo audio, plus a single channel
of music, mixed by the popular ModPlug, Timidity MIDI, Ogg Vorbis,
Tremor, and libmpg123 MP3 libraries.

%prep
%setup

%build
CFLAGS="$RPM_OPT_FLAGS" ./configure --prefix=%{prefix}
make

%install
rm -rf $RPM_BUILD_ROOT
make install prefix=$RPM_BUILD_ROOT/%{prefix}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README.txt CHANGES.txt LICENSE.txt
%{prefix}/lib/lib*.so.*

%files devel
%defattr(-,root,root)
%{prefix}/lib/lib*.a
%{prefix}/lib/lib*.la
%{prefix}/lib/lib*.so
%{prefix}/include/*/
%{prefix}/lib/pkgconfig/*.pc

%changelog
* Wed Jan 19 2000 Sam Lantinga
- converted to get package information from configure
* Sun Jan 16 2000 Hakan Tandogan <hakan@iconsult.com>
- initial spec file

