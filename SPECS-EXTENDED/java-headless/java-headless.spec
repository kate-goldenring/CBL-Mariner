Summary:      Meta package for java-headless
Name:         java-headless
Version:      11.0.13
Release:      1%{?dist}
License:      Public Domain
Vendor:       Microsoft Corporation
URL:          http://www.linuxfromscratch.org
Distribution: Mariner
Requires:     msopenjdk-11

%description
Meta package

%prep
%build
%install

%files

%changelog
* Mon Sep 28 2020 Thomas Crain <v-ruyche@microsoft.com> - 11.0.13-1
- Add folders and symlinks for .dwz files.
