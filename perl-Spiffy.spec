#
# Conditional build:
%bcond_without	tests	# unit tests
#
%define		pdir	Spiffy
%define		pnam	Spiffy
Summary:	Spiffy - Spiffy Perl Interface Framework For You
Summary(pl.UTF-8):	Spiffy - szkielet interfejsu perlowego dla ciebie
Name:		perl-Spiffy
Version:	0.46
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	https://www.cpan.org/modules/by-authors/id/I/IN/INGY/%{pnam}-%{version}.tar.gz
# Source0-md5:	2ec7007c111a6bc2775bb7c57673a24b
URL:		https://metacpan.org/dist/Spiffy
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
"Spiffy" is a Perl module interface methodology and framework. It is a
base class for implementing other Perl modules using author's favorite
tricks.

%description -l pl.UTF-8
"Spiffy" (Spiffy Perl Interface Framework For You, czyli szkielet
interfejsu perlowego dla ciebie) to metodologia i szkielet interfejsu
modułu Perla. Jest to klasa bazowa do implementowania innych modułów
Perla przy użyciu ulubionych sztuczek autora.

%prep
%setup -q -n %{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{perl_vendorlib}/Spiffy.pod
rm -f $RPM_BUILD_ROOT%{perl_vendorarch}/auto/Spiffy/.packlist

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Spiffy.pm
%{perl_vendorlib}/Spiffy
%{_mandir}/man3/Spiffy*.3pm*
