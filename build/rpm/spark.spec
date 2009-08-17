Name: Spark
Summary: Spark RPM-Paket
Version: %{SPARK_VERSION}
Release: 1
License: GPL
Group: misc/Spark
Source: %{SPARK_SOURCE}
Source1: jre-dist.tar.gz
BuildRoot: %{_tmppath}/build-root-%{name}
Packager: igniterealtime.org
Distribution: Linux
Prefix: /usr/share
Url: http://www.igniterealtime.org/downloads/source.jsp

%define prefix /usr/share
%define homedir %{prefix}/spark

%description
Instant Messenger

%prep
%setup -q spark_src

%build
cd build
ant jar
cd ..


%install
# Prep the install location.
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{prefix}

# Copy over the main install tree.
cp -R target/build $RPM_BUILD_ROOT%{homedir}

mkdir -p $RPM_BUILD_ROOT/usr/bin/

#pushd $RPM_BUILD_ROOT%{homedir}
cd $RPM_BUILD_ROOT%{homedir}
gzip -cd %{SOURCE1} | tar xvf -
#popd

echo "#!/bin/bash" > $RPM_BUILD_ROOT/usr/bin/spark
echo "SPARKDIR=/usr/share/spark/" >> $RPM_BUILD_ROOT/usr/bin/spark
echo "/usr/share/spark/jre/bin/java -Dappdir=\$SPARKDIR -cp \$SPARKDIR/lib/log4j.jar:\$SPARKDIR/lib/fmj.jar:\$SPARKDIR/lib/startup.jar:\$SPARKDIR/lib/linux/jdic.jar:\$SPARKDIR/resources org.jivesoftware.launcher.Startup" >> $RPM_BUILD_ROOT/usr/bin/spark

chmod -R 755 $RPM_BUILD_ROOT/usr/bin/spark

rm -r $RPM_BUILD_ROOT/usr/share/spark/lib/windows

# Force a happy exit even if openfire condrestart script didn't exit cleanly.
exit 0


%files
%dir /usr/bin/spark
%dir /usr/share/spark/bin
%dir /usr/share/spark
%dir /usr/share/spark/xtra
/usr/share/spark/bin/*
%dir /usr/share/spark/documentation/
/usr/share/spark/documentation/*
%dir /usr/share/spark/documentation/images/
/usr/share/spark/documentation/images/*
%dir  /usr/share/spark/lib
/usr/share/spark/lib/activation.jar
/usr/share/spark/lib/asterisk-im-client.jar
/usr/share/spark/lib/base.jar
/usr/share/spark/lib/dom4j.jar
/usr/share/spark/lib/fmj.jar
/usr/share/spark/lib/i4jruntime.jar
%dir /usr/share/spark/lib/linux/
/usr/share/spark/lib/linux/jdic.jar
/usr/share/spark/lib/linux/libjdic.so
/usr/share/spark/lib/linux/libmozembed-linux-gtk1.2.so
/usr/share/spark/lib/linux/libmozembed-linux-gtk2.so
/usr/share/spark/lib/linux/libtray.so
/usr/share/spark/lib/linux/libcivil.so
/usr/share/spark/lib/linux/mozembed-linux-gtk1.2
%dir /usr/share/spark/lib/mac/
/usr/share/spark/lib/mac/JavaSoundStream.fix.jar
/usr/share/spark/lib/mac/libSystemUtilities.jnilib
/usr/share/spark/lib/smack.jar
/usr/share/spark/lib/smackx-debug.jar
/usr/share/spark/lib/smackx.jar
/usr/share/spark/lib/spark.jar
/usr/share/spark/lib/startup.jar
/usr/share/spark/lib/swingx.jar
/usr/share/spark/lib/synthetica.jar
/usr/share/spark/lib/syntheticaBlueMoon.jar
/usr/share/spark/lib/systeminfo.jar
/usr/share/spark/lib/xpp.jar
/usr/share/spark/lib/xstream.jar
/usr/share/spark/lib/lti-civil.jar
/usr/share/spark/lib/log4j.jar
%dir /usr/share/spark/logs/
%doc /usr/share/spark/logs/error.log
%dir /usr/share/spark/plugins/
/usr/share/spark/plugins/idlelinux.jar
/usr/share/spark/plugins/jingle.jar
/usr/share/spark/plugins/jniwrapper.jar
/usr/share/spark/plugins/spelling-plugin.jar
/usr/share/spark/plugins/flashing.jar
%dir /usr/share/spark/resources/
/usr/share/spark/resources/Info.plist
/usr/share/spark/resources/jniwrap.dll
/usr/share/spark/resources/jniwrap.lic
%dir /usr/share/spark/resources/sounds/
/usr/share/spark/resources/sounds/bell.wav
/usr/share/spark/resources/sounds/chat_request.wav
/usr/share/spark/resources/sounds/incoming.wav
/usr/share/spark/resources/sounds/outgoing.wav
/usr/share/spark/resources/sounds/presence_changed.wav
/usr/share/spark/resources/startup.sh
/usr/share/spark/resources/systeminfo.dll
%dir /usr/share/spark/xtra/emoticons/ 
/usr/share/spark/xtra/emoticons/Default.adiumemoticonset.zip
/usr/share/spark/xtra/emoticons/GTalk.AdiumEmoticonset.zip
/usr/share/spark/xtra/emoticons/POPO.adiumemoticonset.zip
/usr/share/spark/xtra/emoticons/sparkEmoticonSet.zip
%{homedir}/jre


