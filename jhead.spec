Summary:	Extracts the EXIF data from image files
Summary(pl):	Narzêdzie wyci±gaj±ce dane EXIF z plików graficznych
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
Jhead to sterowane z linii poleceñ narzêdzie do wyci±gania ustawieñ
aparatu z plików w formacie Exif u¿ywanego przez wiele aparatów
cyfrowych. Obs³uguje wiele ró¿nych myl±cych sposobów, w jakie mog± byæ
wyra¿one informacje i wy¶wietla je jako F-stop, szybko¶æ przys³ony
itp. Umo¿liwia tak¿e zmniejszenie rozmiaru pliku JPEG bez utraty
informacji poprzez usuwanie miniaturek wstawianych przez aparaty do
nag³ówka Exif. Jest to tak¿e prosty program, z którego mo¿na przekleiæ
kod w celu obs³ugi formatu Exif we w³asnym programie. Wiele projektów,
w tym PHP, u¿y³o kodu z tego narzêdzia.

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
