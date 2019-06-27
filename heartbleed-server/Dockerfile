FROM ubuntu:trusty

RUN apt-get update
RUN apt-get -y install python python-pip
RUN apt-get install -y wget

#get Ubuntu trusty version of OpenSSL & libssl from the Debian snapshots
RUN wget http://snapshot.debian.org/archive/debian/20140106T220635Z/pool/main/o/openssl/openssl_1.0.1f-1_amd64.deb -O /tmp/openssl_1.0.1f-1_amd64.deb
RUN wget http://snapshot.debian.org/archive/debian/20140106T220635Z/pool/main/o/openssl/libssl1.0.0_1.0.1f-1_amd64.deb -O /tmp/libssl1.0.0_1.0.1f-1_amd64.deb

#install these versions of OpenSSL
RUN dpkg -i /tmp/libssl1.0.0_1.0.1f-1_amd64.deb
RUN dpkg -i /tmp/openssl_1.0.1f-1_amd64.deb

#adds the snakeoil self signed certificate
RUN apt-get -y install ssl-cert

#install apache and wsgi to host the Flask app
RUN apt-get -y install apache2 libapache2-mod-wsgi

#Simple Flask based webapp
RUN mkdir -p /srv/www/app

#copy files over
ADD app /srv/www/app

#install Flask and related modules
RUN pip install Flask Flask-Login Flask-WTF

#copy conf files for our new app over to Apache's conf
ADD conf /etc/apache2/sites-available

#enable various Apache modules
RUN a2enmod wsgi
RUN a2enmod ssl
RUN a2enmod rewrite

#disable default sites and use our app
RUN a2dissite 000-default
RUN a2dissite default-ssl
RUN a2ensite server
RUN a2ensite server-ssl

WORKDIR /srv/www/app

EXPOSE 80
EXPOSE 443

CMD ["/usr/sbin/apachectl","-DFOREGROUND"]
