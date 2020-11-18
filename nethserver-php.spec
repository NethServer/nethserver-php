Summary: NethServer generic PHP configuration
Name: nethserver-php
Version: 1.3.0
Release: 1%{?dist}
License: GPL
Source: %{name}-%{version}.tar.gz
BuildArch: noarch
URL: %{url_prefix}/%{name} 

Requires: nethserver-base
Requires: php-common
Requires: php, php-xml, php-intl

BuildRequires: nethserver-devtools

%description
Set global php.ini directives from NethServer Configuration database.

%prep
%setup

%build
perl createlinks

%install
rm -rf %{buildroot}
(cd root   ; find . -depth -print | cpio -dump %{buildroot})
%{genfilelist} %{buildroot} > %{name}-%{version}-%{release}-filelist

%files -f %{name}-%{version}-%{release}-filelist
%defattr(-,root,root)
%doc COPYING
%dir %{_nseventsdir}/%{name}-update
%attr(0644,root,root) %ghost %{_sysconfdir}/php.d/nethserver.ini

%changelog
* Wed Nov 18 2020 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.3.0-1
- New NethServer 7.9.2009 defaults - NethServer/dev#6320

* Wed Dec 11 2019 Stephane de Labrusse <stephdl@de-labrusse.fr> - 1.2.1-1
- Change PHP-FPM version in Web server app - NethServer/dev#5912
- Automated RPM builds - NethServer/dev#5393

* Thu Jul 07 2016 Stefano Fancello <stefano.fancello@nethesis.it> - 1.2.0-1
- First NS7 release

* Tue Mar 03 2015 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.1.2-1
- Set PHP default timezone from system timezone - Enhancement #3068 [NethServer]
- nethserver-devbox replacements - Feature #3009 [NethServer]

* Wed Feb 05 2014 Davide Principi <davide.principi@nethesis.it> - 1.1.1-1.ns6
- Rebuild for 6.5 beta3

* Tue Apr 30 2013 Davide Principi <davide.principi@nethesis.it> - 1.1.0-1.ns6
- Full automatic package install/upgrade/uninstall support #1870

* Tue Mar 19 2013 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.0.0-2.ns6
- Update spec URL
