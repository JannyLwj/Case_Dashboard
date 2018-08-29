FROM centos:7
MAINTAINER JANNY

RUN yum -y update;yum clean all
RUN yum install -y httpd
RUN yum install -y openssh-server
RUN yum install -y mod_wsgi
RUN mkdir /var/www/html/dragon-corpus
WORKDIR /var/www/html/dragon-corpus
copy DragonCorpus /var/www/html/dragon-corpus/DragonCorpus
WORKDIR /var/www/html/dragon-corpus/DragonCorpus
copy httpd.conf /etc/httpd/conf/
RUN yum install -y wget
RUN wget https://bootstrap.pypa.io/get-pip.py
RUN python get-pip.py
RUN pip install django==1.11.5
RUN yum install -y gcc
RUN yum install -y python-devel
RUN yum install -y mysql-devel
RUN yum install -y openssl-devel
RUN yum install -y zlib-devel
RUN pip install MySQL-python
RUN pip install djangorestframework
RUN pip install XlsxWriter
RUN pip install xlrd
RUN pip install xlwt
RUN pip install xlutils
ENV PYTHONPATH /var/www/html/dragon-corpus/DragonCorpus
RUN chmod -R 777 /var/www/html/dragon-corpus
RUN /sbin/httpd
ADD run.sh /usr/local/sbin/run.sh
RUN chmod 755 /usr/local/sbin/run.sh
#RUN python /var/www/html/dragon-corpus/DragonCorpus/manage.py makemigrations
#RUN python /var/www/html/dragon-corpus/DragonCorpus/manage.py migrate
EXPOSE 22 80 8000
VOLUME /var/www/html/dragon-corpus/DragonCorpus/data 
CMD ["/usr/local/sbin/run.sh"]
#CMD ["python", "/var/www/html/dragon-corpus/DragonCorpus/manage.py", "runserver"]
