#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-doMPI
Version  : 0.2.2
Release  : 52
URL      : https://cran.r-project.org/src/contrib/doMPI_0.2.2.tar.gz
Source0  : https://cran.r-project.org/src/contrib/doMPI_0.2.2.tar.gz
Summary  : Foreach Parallel Adaptor for the Rmpi Package
Group    : Development/Tools
License  : GPL-2.0
Requires: R-Rmpi
Requires: R-foreach
Requires: R-iterators
Requires: openmpi
BuildRequires : R-Rmpi
BuildRequires : R-foreach
BuildRequires : R-iterators
BuildRequires : buildreq-R
BuildRequires : openmpi-dev
BuildRequires : openssh

%description
the Rmpi package.

%prep
%setup -q -c -n doMPI
cd %{_builddir}/doMPI

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1641002686

%install
export SOURCE_DATE_EPOCH=1641002686
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library doMPI
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library doMPI
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library doMPI
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc doMPI || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/doMPI/DESCRIPTION
/usr/lib64/R/library/doMPI/INDEX
/usr/lib64/R/library/doMPI/Meta/Rd.rds
/usr/lib64/R/library/doMPI/Meta/demo.rds
/usr/lib64/R/library/doMPI/Meta/features.rds
/usr/lib64/R/library/doMPI/Meta/hsearch.rds
/usr/lib64/R/library/doMPI/Meta/links.rds
/usr/lib64/R/library/doMPI/Meta/nsInfo.rds
/usr/lib64/R/library/doMPI/Meta/package.rds
/usr/lib64/R/library/doMPI/Meta/vignette.rds
/usr/lib64/R/library/doMPI/NAMESPACE
/usr/lib64/R/library/doMPI/NEWS
/usr/lib64/R/library/doMPI/R/doMPI
/usr/lib64/R/library/doMPI/R/doMPI.rdb
/usr/lib64/R/library/doMPI/R/doMPI.rdx
/usr/lib64/R/library/doMPI/RMPIworker.R
/usr/lib64/R/library/doMPI/benchmarks/bootstrapMPI.R
/usr/lib64/R/library/doMPI/benchmarks/matmul.R
/usr/lib64/R/library/doMPI/benchmarks/rforest.R
/usr/lib64/R/library/doMPI/demo/sincMPI.R
/usr/lib64/R/library/doMPI/doc/doMPI.R
/usr/lib64/R/library/doMPI/doc/doMPI.Rnw
/usr/lib64/R/library/doMPI/doc/doMPI.pdf
/usr/lib64/R/library/doMPI/doc/index.html
/usr/lib64/R/library/doMPI/examples/arima.R
/usr/lib64/R/library/doMPI/examples/bootMPI.R
/usr/lib64/R/library/doMPI/examples/clusterexport.R
/usr/lib64/R/library/doMPI/examples/clusterexport2.R
/usr/lib64/R/library/doMPI/examples/file.R
/usr/lib64/R/library/doMPI/examples/file2.R
/usr/lib64/R/library/doMPI/examples/initEnvir.R
/usr/lib64/R/library/doMPI/examples/iplot.R
/usr/lib64/R/library/doMPI/examples/matmul.R
/usr/lib64/R/library/doMPI/examples/nested.R
/usr/lib64/R/library/doMPI/examples/pi.R
/usr/lib64/R/library/doMPI/examples/pi2.R
/usr/lib64/R/library/doMPI/examples/plots.R
/usr/lib64/R/library/doMPI/examples/prng.R
/usr/lib64/R/library/doMPI/examples/prng2.R
/usr/lib64/R/library/doMPI/examples/resample.R
/usr/lib64/R/library/doMPI/examples/rforest.R
/usr/lib64/R/library/doMPI/examples/sincMPI.R
/usr/lib64/R/library/doMPI/help/AnIndex
/usr/lib64/R/library/doMPI/help/aliases.rds
/usr/lib64/R/library/doMPI/help/doMPI.rdb
/usr/lib64/R/library/doMPI/help/doMPI.rdx
/usr/lib64/R/library/doMPI/help/paths.rds
/usr/lib64/R/library/doMPI/html/00Index.html
/usr/lib64/R/library/doMPI/html/R.css
