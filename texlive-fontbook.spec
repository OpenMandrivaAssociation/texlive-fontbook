Name:		texlive-fontbook
Version:	23608
Release:	2
Summary:	Generate a font book
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/xetex/latex/fontbook
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fontbook.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fontbook.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fontbook.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides a means of producing a 'book' of font
samples (for evaluation, etc.).

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/xelatex/fontbook/fontbook.sty
%doc %{_texmfdistdir}/doc/xelatex/fontbook/README
%doc %{_texmfdistdir}/doc/xelatex/fontbook/fontbook-freefonts.pdf
%doc %{_texmfdistdir}/doc/xelatex/fontbook/fontbook-freefonts.tex
%doc %{_texmfdistdir}/doc/xelatex/fontbook/fontbook.pdf
#- source
%doc %{_texmfdistdir}/source/xelatex/fontbook/fontbook.dtx
%doc %{_texmfdistdir}/source/xelatex/fontbook/fontbook.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
