Packaging for TeamCity
---------------------
Forced to use proprietary software without proper distribution packages? Fight back!

Create package for RHEL/CentOS
------------------------------
The spec file creates a rpm package from the Teamcity + Tomcat bundle. 

First download the bundle from jetbrains website e.g.
      
      wget http://download.jetbrains.com/teamcity/TeamCity-8.1.5.tar.gz
and put it into the SOURCES folder (normally ~/rpmbuild/SOURCES/).

Then run rpmbuild to build the package

      rpmbuild -ba teamcity.spec


Create package for Debian/Ubuntu
--------------------------------




License
-------
Teamcity has its own proprietary license but the packaging files are GPL-2 or (at your option) any later version.
 
