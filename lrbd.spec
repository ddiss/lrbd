#
# spec file for package lrbd
#
# Copyright (c) 2015 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/


Summary: lrbd
Name: lrbd
Version: 0.9.3
Release: 0
License: LGPL-2.1+ 
Group: System Environment/Base
Distribution: SUSE
URL: http://bugs.opensuse.org
Source0: lrbd-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-root
BuildArch: noarch
Requires: python-netifaces
Requires: targetcli
Summary: Configures iSCSI access to Ceph rbd images

%description
This utility creates, modifies and retrieves the configuration from Ceph for 
applying targetcli commands to a host.  

%prep


%build
%__tar xvzf %{SOURCE0}
%__rm -f lrbd/man/*.gz
%__gzip lrbd/man/lrbd.*

%install
%define _samples %{buildroot}%{_docdir}/%{name}/samples
mkdir -p %{buildroot}/var/adm/fillup-templates
mkdir -p %{buildroot}%{_unitdir}
mkdir -p %{buildroot}%{_docdir}/%{name}/samples
mkdir -p %{buildroot}%{_mandir}/man5
mkdir -p %{buildroot}%{_mandir}/man8
mkdir -p %{buildroot}%{_sbindir}

cd lrbd
install -m 555 lrbd %{buildroot}%{_sbindir}
install -m 644 man/lrbd.conf.5.gz %{buildroot}%{_mandir}/man5
install -m 644 man/lrbd.8.gz %{buildroot}%{_mandir}/man8

install -m 644 sysconfig/lrbd %{buildroot}/var/adm/fillup-templates/sysconfig.lrbd
install -m 644 systemd/lrbd.service %{buildroot}%{_unitdir}
ln -sf %{_sbindir}/service %{buildroot}%_sbindir/rclrbd

install -m 644 samples/acls+discovery.json  %{_samples}
install -m 644 samples/acls+discovery+mutual.json  %{_samples}
install -m 644 samples/acls.json  %{_samples}
install -m 644 samples/acls+mutual+discovery.json  %{_samples}
install -m 644 samples/acls+mutual+discovery+mutual.json  %{_samples}
install -m 644 samples/acls+mutual.json  %{_samples}
install -m 644 samples/complete.json  %{_samples}
install -m 644 samples/no_authentication+explicit.json  %{_samples}
install -m 644 samples/no_authentication.json  %{_samples}
install -m 644 samples/tpg+discovery.json  %{_samples}
install -m 644 samples/tpg+discovery+mutual.json  %{_samples}
install -m 644 samples/tpg.json  %{_samples}
install -m 644 samples/tpg+mutual+discovery.json  %{_samples}
install -m 644 samples/tpg+mutual+discovery+mutual.json  %{_samples}
install -m 644 samples/tpg+mutual.json  %{_samples}


%pre
%service_add_pre lrbd.service 

%post
%service_add_post lrbd.service 
%fillup_and_insserv

%preun
%service_del_preun lrbd.service 

%postun
%service_del_postun lrbd.service 

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(-,root,root)
/var/adm/fillup-templates/sysconfig.lrbd
%{_sbindir}/lrbd
%{_sbindir}/rclrbd
%{_mandir}/man5/lrbd.conf.5.gz
%{_mandir}/man8/lrbd.8.gz
%{_unitdir}/lrbd.service
%dir %attr(-, root, root) %{_docdir}/%{name}
%dir %attr(-, root, root) %{_docdir}/%{name}/samples
%{_docdir}/%{name}/samples/*

%changelog
