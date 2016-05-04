Summary: Ceph Jewel packages from the CentOS Storage SIG repository
Name: centos-release-ceph-jewel
Version: 1.0
Release: 1%{?dist}
License: GPLv2
URL: http://wiki.centos.org/SpecialInterestGroup/Storage
Source0: CentOS-Ceph-Jewel.repo

BuildArch: noarch

# This provides the public key to verify the RPMs
Requires: centos-release-storage-common

# Users can install centos-release-ceph to get the latest
Provides: centos-release-ceph = 10.2
Conflicts: centos-release-ceph < 10.2
Obsoletes: centos-release-ceph < 10.2

%description
yum configuration for Ceph Jewel as delivered via the CentOS Storage SIG.

%install
install -D -m 644 %{SOURCE0} %{buildroot}%{_sysconfdir}/yum.repos.d/CentOS-Ceph-Jewel.repo

%files
%defattr(-,root,root)
%config(noreplace) %{_sysconfdir}/yum.repos.d/CentOS-Ceph-Jewel.repo

%changelog
* Wed May 04 2016 François Cami <fcami@fedoraproject.org> - 1.0-1
- Initial version based on Hammer.

