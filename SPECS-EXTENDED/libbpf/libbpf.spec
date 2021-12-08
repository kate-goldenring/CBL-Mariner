Vendor:         Microsoft Corporation
Distribution:   Mariner
%global githubname   libbpf
%global githubver    0.0.7
%global githubfull   %{githubname}-%{githubver}

Name:           %{githubname}
Version:        %{githubver}
Release:        3%{?dist}
Summary:        Libbpf library

License:        LGPLv2 or BSD
URL:            https://github.com/%{githubname}/%{githubname}
Source:         https://github.com/%{githubname}/%{githubname}/archive/v%{githubver}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  gcc elfutils-libelf-devel elfutils-devel


%description
A mirror of bpf-next linux tree bpf-next/tools/lib/bpf directory plus its
supporting header files. The version of the package reflects the version of
ABI.

%package devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       kernel-headers >= 5.4.0-0.rc6.git0.1
Requires:       zlib

%description devel
The %{name}-devel package contains libraries header files for
developing applications that use %{name}

%package static
Summary: Static library for libbpf development
Requires: %{name}-devel = %{version}-%{release}

%description static
The %{name}-static package contains static library for
developing applications that use %{name}

%global make_flags DESTDIR=%{buildroot} OBJDIR=%{_builddir} CFLAGS="%{build_cflags} -fPIC" LDFLAGS="%{build_ldflags} -Wl,--no-as-needed" LIBDIR=/%{_libdir} NO_PKG_CONFIG=1

%prep
%autosetup -n %{githubfull}

%build
%make_build -C ./src %{make_flags}

%install
%make_install -C ./src %{make_flags}

%files
%{_libdir}/libbpf.so.%{version}
%{_libdir}/libbpf.so.0

%files devel
%{_libdir}/libbpf.so
%{_includedir}/bpf/
%{_libdir}/pkgconfig/libbpf.pc

%files static
%{_libdir}/libbpf.a

%changelog
* Mon Nov 01 2021 Muhammad Falak <mwani@microsft.com> - 0.0.7-3
- Remove epoch

* Fri Oct 15 2021 Pawel Winogrodzki <pawelwi@microsoft.com> - 2:0.0.7-2
- Initial CBL-Mariner import from Fedora 32 (license: MIT).

* Sun May 10 2020 Jiri Olsa <jolsa@redhat.com> - 2:0.0.7-1
- release 0.0.7

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2:0.0.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan 2 2020 Jiri Olsa <jolsa@redhat.com> - 0.0.6-2
- release 0.0.6-2, build server issues

* Mon Dec 30 2019 Jiri Olsa <jolsa@redhat.com> - 0.0.6-1
- release 0.0.6

* Thu Nov 28 2019 Jiri Olsa <jolsa@redhat.com> - 0.0.5-3
- release 0.0.5

* Fri Nov 22 2019 Jiri Olsa <jolsa@redhat.com> - 0.0.3-3
- Revert to 0.0.3 version and adjust kernel-headers dependency (BZ#1755317)

* Tue Nov 12 2019 Jiri Olsa <jolsa@redhat.com> - 0.0.5-2
- Add kernel-headers dependency

* Thu Oct 03 2019 Jiri Olsa <jolsa@redhat.com> - 0.0.5-1
- release 0.0.5

* Wed Sep 25 2019 Jiri Olsa <jolsa@redhat.com> - 0.0.3-2
- Fix libelf linking (BZ#1755317)

* Fri Sep 13 2019 Jiri Olsa <jolsa@redhat.com> - 0.0.3-1
- Initial release
