#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Spiffy
%define	pnam	Spiffy
Summary:	Spiffy Perl Interface Framework For You
Summary(pl):	Spiffy - szkielet interfejsu perlowego dla Ciebie
Name:		perl-Spiffy
Version:	0.15
Release:	1
# Same as Perl
License:	GPL or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/I/IN/INGY/%{pnam}-%{version}.tar.gz
# Source0-md5:	e49cd985891b3f032e5d19fd5e386593
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
interfejsu perlowego dla Ciebie) to metodologia i szkielet interfejsu
modu�u Perla. Jest to klasa bazowa do implementowania innych modu��w
Perla przy u�yciu ulubionych sztuczek autora.

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
