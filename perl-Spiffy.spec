#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Spiffy
%define	pnam	Spiffy
Summary:	Spiffy - Spiffy Perl Interface Framework For You
Summary(pl):	Spiffy - szkielet interfejsu perlowego dla ciebie
Name:		perl-Spiffy
Version:	0.20
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/I/IN/INGY/%{pnam}-%{version}.tar.gz
# Source0-md5:	da0e2c24599cdfcbebf881f19eee7c9f
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
"Spiffy" is a Perl module interface methodology and framework. It is
a base class for implementing other Perl modules using author's
favorite tricks.

%description -l pl
"Spiffy" (Spiffy Perl Interface Framework For You, czyli szkielet
interfejsu perlowego dla ciebie) to metodologia i szkielet interfejsu
modu³u Perla. Jest to klasa bazowa do implementowania innych modu³ów
Perla przy u¿yciu ulubionych sztuczek autora.

%prep
%setup -q -n %{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Spiffy.pm
%{_mandir}/man3/Spiffy*
