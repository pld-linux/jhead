Summary:	Extracts the EXIF data from image files
Summary(pl):	Narzêdzie wyci±gaj±ce dane EXIF z plików graficznych
Name:		jhead
Version:	2.0
Release:	2
License:	GPL
Group:		Applications/Graphics
Source0:	http://www.sentex.net/~mwandel/jhead/%{name}-%{version}.tar.gz
# Source0-md5:	0fa7c878390b5019b017f3c5d087a35e
URL:		http://www.sentex.net/~mwandel/jhead/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Jhead extracts the EXIF data from image files which are usually
associated with Digital Cameras.

%description -l pl
Jhead pozwala wyci±gn±æ dane EXIF ze zdjêæ zrobionych aparatami
cyfrowymi.

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
