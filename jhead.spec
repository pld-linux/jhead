Summary:	Extracts the EXIF data from image files
Summary(pl):	Narz�dzie wyci�gaj�ce dane EXIF z plik�w graficznych
Name:		jhead
Version:	2.7
Release:	1
License:	GPL
Group:		Applications/Graphics
Source0:	http://www.sentex.net/~mwandel/jhead/%{name}-%{version}.tar.gz
# Source0-md5:	be10a197a8858de5d86ae89219e806fb
URL:		http://www.sentex.net/~mwandel/jhead/
Patch0:		%{name}-make.patch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Jhead is a command line driven utility for extracting digital camera
settings from the Exif format files used by many digital cameras. It
handles the various confusing ways these can be expressed, and
displays them as F-stop, shutter speed, etc. It is also able to reduce
the size of digital camera JPEGs without loss of information, by
deleting integral thumbnails that digital cameras put into the Exif
header. If you need to add Exif support to a program, this is a simple
program to cut and paste from. Many projects, including PHP, have
reused code from this utility.

%description -l pl
Jhead to sterowane z linii polece� narz�dzie do wyci�gania ustawie�
aparatu z plik�w w formacie Exif u�ywanego przez wiele aparat�w
cyfrowych. Obs�uguje wiele r�nych myl�cych sposob�w, w jakie mog� by�
wyra�one informacje i wy�wietla je jako F-stop, szybko�� przys�ony
itp. Umo�liwia tak�e zmniejszenie rozmiaru pliku JPEG bez utraty
informacji poprzez usuwanie miniaturek wstawianych przez aparaty do
nag��wka Exif. Jest to tak�e prosty program, z kt�rego mo�na przeklei�
kod w celu obs�ugi formatu Exif we w�asnym programie. Wiele projekt�w,
w tym PHP, u�y�o kodu z tego narz�dzia.

%prep
%setup -q
%patch0 -p0

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_mandir}/man1

install -D jhead $RPM_BUILD_ROOT%{_bindir}/%{name}
gzip -dc jhead.1.gz >$RPM_BUILD_ROOT%{_mandir}/man1/%{name}.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc changes.txt usage.html readme.txt
%attr(755,root,root) %{_bindir}/jhead
%{_mandir}/man1/*
