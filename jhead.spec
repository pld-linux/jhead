%define name		jhead
%define version		1.8
%define release		1

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Extracts the EXIF data from image files.
Summary(pl):    Wyci±ga dane EXIF z plików graficznych
Source0:	http://www.sentex.net/~mwandel/jhead/%{name}-%{version}.tar.gz
URL:		http://www.sentex.net/~mwandel/jhead/
License:	GPL
Group:		Applications/Graphics
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Requires:	ImageMagick

%description
Jhead extracts the EXIF data from image files which are usually
associated with Digital Cameras. Also provides makehtml. The latest
info and versions can be found at
http://www.sentex.net/~mwandel/jhead/.

%description(pl)
Jhead pozwala wyci±gn±æ dane EXIF ze zdjêæ zrobionych aparatami cyfrowymi.
Zawiera tak¿e makehtml. Ostatnia wersjê i najnowsze info mo¿na znale¶æ na
stronie http://www.sentex.net/~mwandel/jhead/

%prep
%setup -q -n %{name}-%{version}

%build

make

%install
rm -rf $RPM_BUILD_ROOT
%{__make} DESTDIR=%{buildroot}

install -d $RPM_BUILD_ROOT%{_bindir}
install -d $RPM_BUILD_ROOT%{_mandir}/man1
install ./jhead $RPM_BUILD_ROOT%{_bindir}
install ./makehtml $RPM_BUILD_ROOT%{_bindir}
# install player man page
install -d -m 755 %{buildroot}%{_mandir}/man1
install docs/jhead.1 %{buildroot}%{_mandir}/man1
install docs/makehtml.1 %{buildroot}%{_mandir}/man1

%postun

%clean
rm -rf %{buildroot}

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog COPYING README README.makehtml Usage.html
%attr(755,root,root) %{_bindir}/jhead
%attr(755,root,root) %{_bindir}/makehtml
%{_mandir}/man1/jhead.1.gz
%{_mandir}/man1/makehtml.1.gz
