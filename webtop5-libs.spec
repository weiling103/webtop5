%define webtop_version rc4

Summary: WebTop5 libs
Name: webtop5-libs
Version: 1.0.0
Release: 1%{?dist}
License: GPL
URL: %{url_prefix}/%{name} 
Source0: %{name}-%{version}.tar.gz
Source1: http://www.sonicle.com/nethesis/webtop5/nethesis-webtop5-%{webtop_version}.zip
Source2: http://www.sonicle.com/nethesis/webtop5/postgresql-8.0-312.jdbc3.jar
BuildArch: noarch
Conflicts: webtop4-libs

BuildRequires: unzip

%description
NethServer WebTop 5 libraries

%prep
%setup

%build
mkdir -p root/var/lib/tomcats/webtop/webapps/webtop
mkdir -p root/usr/share/java/tomcat
mv %{SOURCE2} root/usr/share/java/tomcat
unzip %{SOURCE1}
unzip webtop5.war \
 *jar \
 -x *sonicle*.jar \
 -x *webtop*.jar \
 -d root/var/lib/tomcats/webtop/webapps/webtop

%install
rm -rf %{buildroot}
(cd root; find . -depth -print | cpio -dump %{buildroot})

%post

%preun

%files
%defattr(-,root,root)
/var/lib/tomcats/webtop/webapps/webtop/*
/usr/share/java/tomcat/postgresql-8.0-312.jdbc3.jar

%changelog
* Wed Mar 08 2017 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.0.0-1
- First WebTop5 release - NethServer/dev#5225

