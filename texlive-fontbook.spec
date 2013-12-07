# revision 23608
# category Package
# catalog-ctan /macros/xetex/latex/fontbook
# catalog-date 2011-08-17 19:15:50 +0200
# catalog-license lppl1.3
# catalog-version 0.2
Name:		texlive-fontbook
Version:	0.2
Release:	5
Summary:	Generate a font book
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/xetex/latex/fontbook
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fontbook.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fontbook.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fontbook.source.tar.xz
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
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.2-2
+ Revision: 752009
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 0.2-1
+ Revision: 718479
- texlive-fontbook
- texlive-fontbook
- texlive-fontbook

