%define Product PlonePAS
%define product plonepas
%define name    zope-%{Product}
%define version 3.0
%define release %mkrel 1

%define zope_minver	2.7
%define plone_minver	2.0
%define zope_home	%{_prefix}/lib/zope
%define software_home	%{zope_home}/lib/python

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	This product adapts the PluggableAuthService for use by Plone
License:	GPL
Group:		System/Servers
URL:        http://plone.org/products/%{product}
Source:     http://plone.org/products/%{product}/releases/%{version}/%{Product}-%{version}.tar.gz
Requires:	zope >= %{zope_minver}
Requires:	plone >= %{plone_minver}
BuildArch:  noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}

%description
This product adapts the PluggableAuthService for use by Plone. PAS is a
UserFolder replacement that allows any part of its functionality to be augmented
or replaced by simple plugins. The architecture allows for customizers to adapt
any aspect of membership?memberdata, groups, roles, user, authentication
strategy and many other aspects of user data source integration. It is also
shared between Zope Corp. products, CPS and now Plone.

%prep
%setup -c -q

%build
# Not much, eh? :-)


%install
%{__rm} -rf %{buildroot}
%{__mkdir_p} %{buildroot}/%{software_home}/Products
%{__cp} -a %{Product} %{buildroot}%{software_home}/Products


%clean
%{__rm} -rf %{buildroot}

%post
if [ "`%{_prefix}/bin/zopectl status`" != "daemon manager not running" ] ; then
	service zope restart
fi

%postun
if [ -f "%{_prefix}/bin/zopectl" ] && [ "`%{_prefix}/bin/zopectl status`" != "daemon manager not running" ] ; then
	service zope restart
fi

%files
%defattr(-,root,root)
%{software_home}/Products/*
