%global gemdir %(ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%global gemname torpedo
%global gemversion 1.0.13

Name:		rubygem-torpedo
Version:	1.0.19
Release:	1%{?dist}
Summary:	Fast Ruby integration tests for OpenStack.

License:	GPL
URL:		https://github.com/dprince/torpedo
Source0:	torpedo-1.0.19.tar.gz
BuildArch: 	noarch

BuildRequires:	rubygems
Requires:	rubygems

%description
Fire when ready. Fast Ruby integration tests for OpenStack.

%prep
%setup -q -n %{gemname}-%{version}


%build
rm -rf %{buildroot}
gem build %{gemname}.gemspec


%install
gem install --local --install-dir %{buildroot}%{gemdir} --force %{gemname}-%{gemversion}.gem


%files
%doc
%{gemdir}/gems/%{gemname}-%{gemversion}/
%{gemdir}/cache/%{gemname}-%{gemversion}.gem
%{gemdir}/specifications/%{gemname}-%{gemversion}.gemspec


%changelog
* Wed Apr 10 2013 Nuno Santos <nsantos@redhat.com> - 1.0.19-1
- Initial package
