Summary:	Extracts the EXIF data from image files
Summary(pl):	Narzêdzie wyci±gaj±ce dane EXIF z plików graficznych
Name:		jhead
Version:	2.2
Release:	3.1
License:	GPL
Group:		Applications/Graphics
Source0:	http://www.sentex.net/~mwandel/jhead/%{name}-%{version}.tar.gz
# Source0-md5:	ba88cad2deaa40d7c1caadc518bcb7e7
URL:		http://www.sentex.net/~mwandel/jhead/
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

%prep
%setup -q

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

install -D jhead $RPM_BUILD_ROOT%{_bindir}/%{name}
install -D jhead.1.gz $RPM_BUILD_ROOT%{_mandir}/man1/%{name}.1.gz

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc changes.txt usage.html readme.txt
%attr(755,root,root) %{_bindir}/jhead
%{_mandir}/man1/*
