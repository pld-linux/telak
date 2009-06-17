
Summary:	A program which displays pictures in root window
Summary(pl.UTF-8):	Program, który wyświetla obrazki w głównym oknie
Name:		telak
Version:	0.5
Release:	1
License:	GPL v2
Group:		X11/Applications/Multimedia
# git://git.naquadah.org/telak.git
Source0:	%{name}-%{version}.tar.lzma
# Source0-md5:	64c8be7214ca41b98180e7e81844cf10
URL:		http://git.naquadah.org/?p=telak.git;a=summary
BuildRequires:	curl-devel
BuildRequires:	imlib2-devel
BuildRequires:	libgcrypt-devel
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-proto-xproto-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Telak is a program which displays pictures in root window. It can
display content of local file, or download image via http. Telak can
be configured to refetch picture every n seconds, so it can be used to
display image from webcam.

%description -l pl.UTF-8
Telak to program wyświetlający obrazki na głównym oknie X Window.
Telak może wyświetlać zawartość lokalnego pliku, lub pobierać plik ze
zdalnej lokalizacji przez http. Program może zostać tak
skonfigurowany, żeby ponownie pobierał plik w zadanych odstępach
czasu. Dzięki temu może być użyty do wyświetlania obrazu z kamery
internetowej.

%prep
%setup -q

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README telakrc.sample
%attr(755,root,root) %{_bindir}/telak
%{_mandir}/man1/telak.1*
