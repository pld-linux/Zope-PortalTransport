%define		zope_subname	PortalTransport
Summary:	Provides a subscription service for CMF
Summary(pl):	Produkt dodaj±cy mo¿liwo¶æ subskrypcji dla us³ug CMF
Name:		Zope-%{zope_subname}
Version:	1.1
Release:	4
License:	GPL
Group:		Development/Tools
Source0:	http://dl.sourceforge.net/collective/%{zope_subname}-%{version}.tar.gz
# Source0-md5:	a461fbee5442e1d29af623a9d9bcbfbb
Patch0:		%{name}-Interface.patch
URL:		http://sourceforge.net/projects/collective/
Requires(post,postun):	/usr/sbin/installzopeproduct
BuildRequires:	python
%pyrequires_eq	python-modules
Requires:	Zope
Requires:	Zope-CMF >= 1:1.4.2
Requires:	Zope-CMFPlone >= 2.0
Requires:	Zope-archetypes >= 1.2.5
Requires:	Zope-stripogram
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PortalTransport provides a subscription service for CMF.

%description -l pl
PortalTransport jest produktem dodaj±cym mo¿liwo¶æ subskrypcji dla
us³ug CMF.

%prep
%setup -q -n %{zope_subname}
%patch0 -p1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/%{name}

cp -af {Bouncers,Extensions,i18n,interfaces,skins,zpt,*.py,*.gif,VERSION.txt} \
	$RPM_BUILD_ROOT%{_datadir}/%{name}

%py_comp $RPM_BUILD_ROOT%{_datadir}/%{name}
%py_ocomp $RPM_BUILD_ROOT%{_datadir}/%{name}

# find $RPM_BUILD_ROOT -type f -name "*.py" -exec rm -rf {} \;;

%clean
rm -rf $RPM_BUILD_ROOT

%post
/usr/sbin/installzopeproduct %{_datadir}/%{name} %{zope_subname}
if [ -f /var/lock/subsys/zope ]; then
	/etc/rc.d/init.d/zope restart >&2
fi

%postun
if [ "$1" = "0" ]; then
	/usr/sbin/installzopeproduct -d %{zope_subname}
	if [ -f /var/lock/subsys/zope ]; then
		/etc/rc.d/init.d/zope restart >&2
	fi
fi

%files
%defattr(644,root,root,755)
%doc CHANGES.txt README.txt CREDITS.txt TODO
%{_datadir}/%{name}
