%define name oggfwd
%define version 0.2
%define release %mkrel 1

Summary: Simple icecast 2 client to stream a ogg stream from stdin
Name: %{name}
Version: %{version}
Release: %{release}
# taken from debian, as there is no upstream tarball
Source0: %{name}_%{version}.orig.tar.gz
License: GPLv2
Group: TODO
Url: http://v2v.cc/~j/oggfwd/
BuildRoot: %{_tmppath}/%{name}-buildroot

%description
TODO
%prep
%setup -q

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

