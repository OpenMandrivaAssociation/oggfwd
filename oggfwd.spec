%define name oggfwd
%define version 0.2
%define release 4

Summary: Simple icecast 2 client to stream a ogg stream from stdin
Name: %{name}
Version: %{version}
Release: %{release}
# taken from debian, as there is no upstream tarball
Source0: %{name}_%{version}.orig.tar.gz
# patch taken from debian
Patch0: oggfwd-0.2-overlinking.patch 
License: GPLv2
Group: Video
Url: http://v2v.cc/~j/oggfwd/
BuildRoot: %{_tmppath}/%{name}-buildroot
BuildRequires: libshout-devel
 
%description
Simple icecast2 client that send the stream read from stdin.

%prep
%setup -q
%patch0 -p0

%build
make

%install
rm -rf $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT/%_bindir/
cp oggfwd $RPM_BUILD_ROOT/%_bindir/ 

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README ChangeLog
%_bindir/oggfwd



%changelog
* Tue May 03 2011 Michael Scherer <misc@mandriva.org> 0.2-3mdv2011.0
+ Revision: 664793
- rebuild old package

  + Oden Eriksson <oeriksson@mandriva.com>
    - the mass rebuild of 2010.0 packages

* Sat Jun 13 2009 Michael Scherer <misc@mandriva.org> 0.2-1mdv2010.0
+ Revision: 385645
- add patch for overlinking, taken from debian
- add description and group
- import oggfwd


