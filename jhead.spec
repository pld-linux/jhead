Summary:	Extracts the EXIF data from image files
Summary(pl.UTF-8):	Narzędzie wyciągające dane EXIF z plików graficznych
Name:		jhead
Version:	2.6
Release:	1
License:	GPL
Group:		Applications/Graphics
Source0:	http://www.sentex.net/~mwandel/jhead/%{name}-%{version}.tar.gz
# Source0-md5:	fa3f1d3243fab7bc3b81688a3f2eec25
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

%description -l pl.UTF-8
Jhead to sterowane z linii poleceń narzędzie do wyciągania ustawień
aparatu z plików w formacie Exif używanego przez wiele aparatów
cyfrowych. Obsługuje wiele różnych mylących sposobów, w jakie mogą być
wyrażone informacje i wyświetla je jako F-stop, szybkość przysłony
itp. Umożliwia także zmniejszenie rozmiaru pliku JPEG bez utraty
informacji poprzez usuwanie miniaturek wstawianych przez aparaty do
nagłówka Exif. Jest to także prosty program, z którego można przekleić
kod w celu obsługi formatu Exif we własnym programie. Wiele projektów,
w tym PHP, użyło kodu z tego narzędzia.

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
