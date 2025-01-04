# Copyright 2025 Wong Hoi Sing Edison <hswong3i@pantarei-design.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

%global debug_package %{nil}

%global source_date_epoch_from_changelog 0

Name: python-text-unidecode
Epoch: 100
Version: 1.3
Release: 1%{?dist}
BuildArch: noarch
Summary: The most basic Text::Unidecode port
License: GPL-2.0-or-later
URL: https://github.com/kmike/text-unidecode/tags
Source0: %{name}_%{version}.orig.tar.gz
BuildRequires: fdupes
BuildRequires: python-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-setuptools

%description
text-unidecode is the most basic port of the Text::Unidecode Perl
library. There are other Python ports of Text::Unidecode (unidecode and
isounidecode). unidecode is GPL; isounidecode doesn’t support Python 3
and uses too much memory.

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .

%build
%py3_build

%install
%py3_install
find %{buildroot}%{python3_sitelib} -type f -name '*.pyc' -exec rm -rf {} \;
fdupes -qnrps %{buildroot}%{python3_sitelib}

%check

%if 0%{?suse_version} > 1500
%package -n python%{python3_version_nodots}-text-unidecode
Summary: The most basic Text::Unidecode port
Requires: python3
Provides: python3-text-unidecode = %{epoch}:%{version}-%{release}
Provides: python3dist(text-unidecode) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-text-unidecode = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(text-unidecode) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-text-unidecode = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(text-unidecode) = %{epoch}:%{version}-%{release}

%description -n python%{python3_version_nodots}-text-unidecode
text-unidecode is the most basic port of the Text::Unidecode Perl
library. There are other Python ports of Text::Unidecode (unidecode and
isounidecode). unidecode is GPL; isounidecode doesn’t support Python 3
and uses too much memory.

%files -n python%{python3_version_nodots}-text-unidecode
%license LICENSE
%{python3_sitelib}/*
%endif

%if !(0%{?suse_version} > 1500)
%package -n python3-text-unidecode
Summary: The most basic Text::Unidecode port
Requires: python3
Provides: python3-text-unidecode = %{epoch}:%{version}-%{release}
Provides: python3dist(text-unidecode) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-text-unidecode = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(text-unidecode) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-text-unidecode = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(text-unidecode) = %{epoch}:%{version}-%{release}

%description -n python3-text-unidecode
text-unidecode is the most basic port of the Text::Unidecode Perl
library. There are other Python ports of Text::Unidecode (unidecode and
isounidecode). unidecode is GPL; isounidecode doesn’t support Python 3
and uses too much memory.

%files -n python3-text-unidecode
%license LICENSE
%{python3_sitelib}/*
%endif

%changelog
