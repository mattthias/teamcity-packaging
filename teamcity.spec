Summary: Jetbrains TeamCity ci server with bundled tomcat
Name: teamcity
Version: 8.0.5
Release: 1%{?dist}
SOURCE0: TeamCity-%{version}.tar.gz

License: proprietary
Group: Development/System
BuildArch: noarch

%description -n teamcity
TeamCity ci server with bundled tomcat

%define _binaries_in_noarch_packages_terminate_build   0

%prep
%setup -n TeamCity

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/opt/teamcity/
cp -a * $RPM_BUILD_ROOT/opt/teamcity

%clean
rm -rf $RPM_BUILD_ROOT

%files -n teamcity
/opt/teamcity/*

%changelog
* Wed Nov 20 2013 Matthias Schmitz <matthias@sigxcpu.org>
- Update packaging to TeamCity 8.0.5 

* Sun Oct 20 2013 Matthias Schmitz <matthias@sigxcpu.org>
- Inital creation of spec

