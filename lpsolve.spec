Name:      lpsolve
Summary:   A Mixed Integer Linear Programming (MILP) solver
Version:   5.5.0.15
Release:   2%{?dist}
Source:    http://downloads.sourceforge.net/lpsolve/lp_solve_%{version}_source.tar.gz
Group:     System Environment/Libraries
URL:       http://sourceforge.net/projects/lpsolve
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
License:   LGPLv2+

Patch0:    lpsolve-5.5.0.11.cflags.patch

%description
Mixed Integer Linear Programming (MILP) solver lpsolve solves pure linear,
(mixed) integer/binary, semi-continuous and special ordered sets (SOS) models.

%package devel
Requires: lpsolve = %{version}-%{release}
Summary: Files for developing with lpsolve
Group: Development/Libraries

%description devel
Includes and definitions for developing with lpsolve 

%prep
%setup -q -n lp_solve_5.5
%patch0 -p1 -b .cflags.patch
#sparc and s390 need -fPIC  lets sed it                                              
%ifarch sparcv9 sparc64 s390 s390x                                                   
sed -i -e 's|-fpic|-fPIC|g' Makefile*                                                
sed -i -e 's|-fpic|-fPIC|g' lpsolve55/ccc                                            
%endif 

%build
cd lpsolve55
sh -x ccc
rm bin/ux*/liblpsolve55.a
cd ../lp_solve
sh -x ccc

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir} $RPM_BUILD_ROOT%{_libdir} $RPM_BUILD_ROOT%{_includedir}/lpsolve
install -m 755 \
        lp_solve/bin/ux*/lp_solve $RPM_BUILD_ROOT%{_bindir}
install -m 755 \
        lpsolve55/bin/ux*/liblpsolve55.so $RPM_BUILD_ROOT%{_libdir}
install -m 644 \
        lp*.h $RPM_BUILD_ROOT%{_includedir}/lpsolve

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc README.txt ./bfp/bfp_LUSOL/LUSOL/LUSOL_LGPL.txt ./bfp/bfp_LUSOL/LUSOL/LUSOL_README.txt ./bfp/bfp_LUSOL/LUSOL/LUSOL-overview.txt
%{_bindir}/lp_solve
%{_libdir}/*.so

%files devel
%defattr(-,root,root,-)
%{_includedir}/lpsolve

%changelog
* Wed Jan 06 2010 Caolán McNamara <caolanm@redhat.com> - 5.5.0.15-2
- Resolves: rhbz#552883 update upstream source

* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 5.5.0.15-1.1
- Rebuilt for RHEL 6

* Sat Sep 12 2009 Caolán McNamara <caolanm@redhat.com> - 5.5.0.15-1
- latest version

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.5.0.14-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.5.0.14-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Feb 23 2009 Caolán McNamara <caolanm@redhat.com> - 5.5.0.14-2
- defuzz patch

* Mon Feb 02 2009 Caolán McNamara <caolanm@redhat.com> - 5.5.0.14-1
- latest version

* Fri Jan 02 2009 Dennis Gilmore <dennis@ausil.us> - 5.5.0.13-2
- use -fPIC on sparc and s390 arches

* Mon Aug 04 2008 Caolan McNamara <caolanm@redhat.com> - 5.5.0.13-1
- latest version

* Sat Aug 02 2008 Caolan McNamara <caolanm@redhat.com> - 5.5.0.12-2
- Mar 20 upstream tarball now differs from Mar 14 tarball

* Fri Mar 14 2008 Caolan McNamara <caolanm@redhat.com> - 5.5.0.12-1
- latest version

* Wed Feb 20 2008 Caolan McNamara <caolanm@redhat.com> - 5.5.0.11-1
- initial version
