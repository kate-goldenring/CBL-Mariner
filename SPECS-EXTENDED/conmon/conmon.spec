Vendor:         Microsoft Corporation
Distribution:   Mariner
%global with_debug 1
%global with_check 0

%if 0%{?with_debug}
%global _find_debuginfo_dwz_opts %{nil}
%global _dwz_low_mem_die_limit 0
%else
%global debug_package %{nil}
%endif

%global provider github
%global provider_tld com
%global project containers
%global repo conmon
# https://github.com/containers/conmon
%global import_path %{provider}.%{provider_tld}/%{project}/%{repo}
%global git0 https://%{import_path}

# Used for comparing with latest upstream tag
# to decide whether to autobuild (non-rawhide only)
%define built_tag v2.0.26
%define built_tag_strip %(b=%{built_tag}; echo ${b:1})
%define download_url %{git0}/archive/%{built_tag}.tar.gz

Name: %{repo}
Version: 2.0.26
Release: 3%{?dist}
Summary: OCI container runtime monitor
License: ASL 2.0
URL: %{git0}
Source0: %{download_url}#/%{name}-%{version}.tar.gz
BuildRequires: gcc
BuildRequires: git
BuildRequires: glib2-devel
BuildRequires: systemd-devel
BuildRequires: systemd-libs
BuildRequires: golang

BuildRequires: golang-github-cpuguy83-md2man



Requires: glib2
Requires: systemd-libs

%description
%{summary}.

%prep
%autosetup -Sgit -n %{name}-%{built_tag_strip}

%build
%{__make} DEBUGTAG=enable_debug

%install
GO_MD2MAN=go-md2man %{__make} PREFIX=%{buildroot}%{_prefix} DESTDIR=%{buildroot} docs
%{__make} PREFIX=%{buildroot}%{_prefix} install install.crio

#define license tag if not already defined
%{!?_licensedir:%global license %doc}

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_libexecdir}/crio/%{name}
%{_libexecdir}/crio/%{name}
%{_mandir}/man8/%{name}*.8*

%changelog
* Mon Nov 01 2021 Muhammad Falak <mwani@microsft.com> - 2.0.26-3
- Remove epoch

* Fri Oct 15 2021 Pawel Winogrodzki <pawelwi@microsoft.com> - 2:2.0.26-2
- Initial CBL-Mariner import from Fedora 32 (license: MIT).

* Wed Feb 03 2021 RH Container Bot <rhcontainerbot@fedoraproject.org> - 2:2.0.26-1
- autobuilt v2.0.26

* Wed Jan 20 2021 RH Container Bot <rhcontainerbot@fedoraproject.org> - 2:2.0.25-1
- autobuilt v2.0.25

* Thu Jan 14 2021 RH Container Bot <rhcontainerbot@fedoraproject.org> - 2:2.0.24-1
- autobuilt v2.0.24

* Thu Jan 14 2021 RH Container Bot <rhcontainerbot@fedoraproject.org> - 2:2.0.23-1
- autobuilt v2.0.23

* Thu Dec 17 2020 Peter Hunt <pehunt@redhat.com> - 2:2.0.22-2
- Update to use go-md2man and install man page

* Thu Dec 17 2020 RH Container Bot <rhcontainerbot@fedoraproject.org> - 2:2.0.22-1
- autobuilt v2.0.22

* Tue Sep 15 2020 Lokesh Mandvekar <lsm5@fedoraproject.org> - 2:2.0.21-2
- build v2.0.21 correctly

* Wed Sep  9 2020 RH Container Bot <rhcontainerbot@fedoraproject.org> - 2:2.0.21-1
- autobuilt v2.0.21

* Fri Sep 04 2020 Lokesh Mandvekar <lsm5@fedoraproject.org> - 2:2.0.20-3
- rebuild cause messed up changelog

* Wed Sep 02 2020 Lokesh Mandvekar <lsm5@fedoraproject.org> - 2:2.0.20-2
- Resolves: #1786090 - build with -g for debuginfo

* Tue Jul 28 2020 RH Container Bot <rhcontainerbot@fedoraproject.org> - 2:2.0.20-1
- autobuilt v2.0.20

* Wed Jul 15 2020 RH Container Bot <rhcontainerbot@fedoraproject.org> - 2:2.0.19-1
- autobuilt v2.0.19

* Mon Jun 15 2020 RH Container Bot <rhcontainerbot@fedoraproject.org> - 2:2.0.18-1
- autobuilt v2.0.18

* Tue May 26 2020 RH Container Bot <rhcontainerbot@fedoraproject.org> - 2:2.0.17-1
- autobuilt v2.0.17

* Mon May 25 2020 Lokesh Mandvekar <lsm5@fedoraproject.org> - 2:2.0.16-3
- depend on glib2

* Wed May 13 2020 Lokesh Mandvekar <lsm5@fedoraproject.org> - 2:2.0.16-2
- bump release tag for podman bodhi

* Wed May 13 2020 RH Container Bot <rhcontainerbot@fedoraproject.org> - 2:2.0.16-1
- autobuilt v2.0.16

* Thu Apr 02 2020 RH Container Bot <rhcontainerbot@fedoraproject.org> - 2:2.0.15-1
- autobuilt v2.0.15

* Fri Mar 20 2020 RH Container Bot <rhcontainerbot@fedoraproject.org> - 2:2.0.14-1
- autobuilt v2.0.14

* Tue Mar 17 2020 RH Container Bot <rhcontainerbot@fedoraproject.org> - 2:2.0.13-1
- autobuilt v2.0.13

* Tue Mar 17 2020 RH Container Bot <rhcontainerbot@fedoraproject.org> - 2:2.0.12-1
- autobuilt v2.0.12

* Fri Mar 13 2020 Lokesh Mandvekar <lsm5@fedoraproject.org> - 2:2.0.11-2
- update spec for autobuilds
- depend on systemd

* Tue Feb 11 2020 RH Container Bot <rhcontainerbot@fedoraproject.org> - 2:2.0.11-0.6.dev.git86aa80b
- autobuilt 86aa80b

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2:2.0.11-0.5.dev.git77f4a51
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jan 15 2020 RH Container Bot <rhcontainerbot@fedoraproject.org> - 2:2.0.11-0.4.dev.git77f4a51
- autobuilt 77f4a51

* Tue Jan 14 2020 RH Container Bot <rhcontainerbot@fedoraproject.org> - 2:2.0.11-0.3.dev.gitccfdbb6
- autobuilt ccfdbb6

* Sat Jan 11 2020 RH Container Bot <rhcontainerbot@fedoraproject.org> - 2:2.0.11-0.2.dev.git5039b44
- autobuilt 5039b44

* Wed Jan 08 2020 RH Container Bot <rhcontainerbot@fedoraproject.org> - 2:2.0.11-0.1.dev.gitad05887
- bump to 2.0.11
- autobuilt ad05887

* Tue Jan 07 2020 RH Container Bot <rhcontainerbot@fedoraproject.org> - 2:2.0.10-0.3.dev.git26f6817
- autobuilt 26f6817

* Tue Jan 07 2020 RH Container Bot <rhcontainerbot@fedoraproject.org> - 2:2.0.10-0.2.dev.git6e39a83
- autobuilt 6e39a83

* Mon Jan 06 2020 RH Container Bot <rhcontainerbot@fedoraproject.org> - 2:2.0.10-0.1.dev.gitb7bfc7b
- bump to 2.0.10
- autobuilt b7bfc7b

* Mon Jan 06 2020 RH Container Bot <rhcontainerbot@fedoraproject.org> - 2:2.0.9-0.3.dev.git1560392
- autobuilt 1560392

* Fri Dec 20 2019 RH Container Bot <rhcontainerbot@fedoraproject.org> - 2:2.0.9-0.2.dev.gitb17d81b
- autobuilt b17d81b

* Fri Dec 13 2019 RH Container Bot <rhcontainerbot@fedoraproject.org> - 2:2.0.9-0.1.dev.gitc2e2e67
- bump to 2.0.9
- autobuilt c2e2e67

* Fri Dec 13 2019 RH Container Bot <rhcontainerbot@fedoraproject.org> - 2:2.0.8-0.2.dev.gitc8f7443
- autobuilt c8f7443

* Thu Dec 12 2019 RH Container Bot <rhcontainerbot@fedoraproject.org> - 2:2.0.8-0.1.dev.git036ff29
- bump to 2.0.8
- autobuilt 036ff29

* Thu Dec 12 2019 RH Container Bot <rhcontainerbot@fedoraproject.org> - 2:2.0.7-0.3.dev.git4100fb2
- autobuilt 4100fb2

* Thu Dec 12 2019 RH Container Bot <rhcontainerbot@fedoraproject.org> - 2:2.0.7-0.2.dev.git95ed45a
- autobuilt 95ed45a

* Wed Dec 11 2019 RH Container Bot <rhcontainerbot@fedoraproject.org> - 2:2.0.7-0.1.dev.git8ba9575
- bump to 2.0.7
- autobuilt 8ba9575

* Wed Dec 11 2019 RH Container Bot <rhcontainerbot@fedoraproject.org> - 2:2.0.6-0.2.dev.gitba14d9c
- autobuilt ba14d9c

* Tue Dec 10 2019 RH Container Bot <rhcontainerbot@fedoraproject.org> - 2:2.0.6-0.1.dev.gitbc9e976
- bump to 2.0.6
- autobuilt bc9e976

* Tue Dec 10 2019 RH Container Bot <rhcontainerbot@fedoraproject.org> - 2:2.0.5-0.2.dev.gitc792503
- autobuilt c792503

* Mon Dec 09 2019 RH Container Bot <rhcontainerbot@fedoraproject.org> - 2:2.0.5-0.1.dev.gitfd5ac47
- bump to 2.0.5
- autobuilt fd5ac47

* Mon Dec 02 2019 RH Container Bot <rhcontainerbot@fedoraproject.org> - 2:2.0.4-0.3.dev.gitdf8c6aa
- autobuilt df8c6aa

* Fri Nov 29 2019 RH Container Bot <rhcontainerbot@fedoraproject.org> - 2:2.0.4-0.2.dev.git42bce45
- autobuilt 42bce45

* Mon Nov 11 2019 RH Container Bot <rhcontainerbot@fedoraproject.org> - 2:2.0.4-0.1.dev.gitf6d23b5
- bump to 2.0.4
- autobuilt f6d23b5

* Mon Nov 11 2019 RH Container Bot <rhcontainerbot@fedoraproject.org> - 2:2.0.3-0.3.dev.git098fcce
- autobuilt 098fcce

* Thu Nov 07 2019 RH Container Bot <rhcontainerbot@fedoraproject.org> - 2:2.0.3-0.2.dev.git002da25
- autobuilt 002da25

* Mon Oct 21 2019 Lokesh Mandvekar <lsm5@fedoraproject.org> - 2:2.0.3-0.1.dev.gitbc758d8
- built commit bc758d8

* Wed Sep 25 2019 Lokesh Mandvekar <lsm5@fedoraproject.org> - 2:2.0.2-0.1.dev.git422ce21
- build latest upstream master

* Tue Sep 10 2019 Lokesh Mandvekar <lsm5@fedoraproject.org> - 2:2.0.0-2
- remove BR: go-md2man since no manpages yet

* Tue Sep 10 2019 Lokesh Mandvekar <lsm5@fedoraproject.org> - 2:2.0.0-1
- bump to v2.0.0

* Fri May 31 2019 Lokesh Mandvekar <lsm5@fedoraproject.org> - 2:0.2.0-1
- initial package
