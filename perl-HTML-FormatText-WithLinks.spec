#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	HTML
%define		pnam	FormatText-WithLinks
%include	/usr/lib/rpm/macros.perl
Summary:	HTML::FormatText::WithLinks - HTML to text conversion with links as footnotes
Summary(pl.UTF-8):	HTML::FormatText::WithLinks - konwersja HTML-a do tekstu z odnośnikami jako przypisami
Name:		perl-HTML-FormatText-WithLinks
Version:	0.14
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/HTML/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	264a1436883d20b81e669c65a1f97367
URL:		http://search.cpan.org/dist/HTML-FormatText-WithLinks/
BuildRequires:	perl-Module-Build
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-HTML-Format >= 2
BuildRequires:	perl-HTML-Tree
BuildRequires:	perl-Test-Simple
BuildRequires:	perl-URI
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
HTML::FormatText::WithLinks takes HTML and turns it into plain text
but prints all the links in the HTML as footnotes. By default, it
attempts to mimic the format of the lynx text based web browser's
--dump option.

%description -l pl.UTF-8
HTML::FormatText::WithLinks przyjmuje HTML i zamienia go na zwykły
tekst, ale wypisuje wszystkie odnośniki z HTML-a jako przypisy.
Domyślnie próbuje naśladować format opcji --dump tekstowej
przeglądarki lynx.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Build.PL \
	destdir=$RPM_BUILD_ROOT \
	installdirs=vendor
./Build

%{?with_tests:./Build test}

%install
rm -rf $RPM_BUILD_ROOT

./Build install

install -d $RPM_BUILD_ROOT%{_examplesdir}
cp -a examples $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorlib}/HTML/FormatText/WithLinks.pm
%{_mandir}/man3/HTML::FormatText::WithLinks.3pm*
%{_examplesdir}/%{name}-%{version}
