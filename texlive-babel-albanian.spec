# revision 30254
# category Package
# catalog-ctan /macros/latex/contrib/babel-contrib/albanian
# catalog-date 2011-09-19 08:05:09 +0100
# catalog-license lppl
# catalog-version 1.0c
Name:		texlive-babel-albanian
Version:	1.0c
Release:	2
Summary:	Support for Albanian within babel
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/babel-contrib/albanian
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/babel-albanian.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/babel-albanian.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/babel-albanian.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides support for typesetting Albanian (as part
of the babel system).

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/generic/babel-albanian/albanian.ldf
%doc %{_texmfdistdir}/doc/generic/babel-albanian/albanian.pdf
#- source
%doc %{_texmfdistdir}/source/generic/babel-albanian/albanian.dtx
%doc %{_texmfdistdir}/source/generic/babel-albanian/albanian.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
