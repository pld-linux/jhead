Summary:	Extracts the EXIF data from image files
Summary(pl):	Narzêdzie wyci±gaj±ce dane EXIF z plików graficznych
Name:		jhead
Version:	1.8
Release:	1
License:	GPL
Group:		Applications/Graphics
Source0:	http://www.sentex.net/~mwandel/jhead/%{name}-%{version}.tar.gz
# Source0-md5:	f9963dad3fd17ed4dcd7f706d0603213
URL:		http://www.sentex.net/~mwandel/jhead/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Jhead extracts the EXIF data from image files which are usually
associated with Digital Cameras. Also provides makehtml. The latest
info and versions can be found at
http://www.sentex.net/~mwandel/jhead/.

%description -l pl
Jhead pozwala wyci±gn±æ dane EXIF ze zdjêæ zrobionych aparatami
cyfrowymi. Zawiera tak¿e makehtml. Ostatnia wersjê i najnowsze
informacje mo¿na znale¶æ na stronie
http://www.sentex.net/~mwandel/jhead/.

%prep
%setup -q

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install jhead $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc changes.txt usage.html
%attr(755,root,root) %{_bindir}/jhead
