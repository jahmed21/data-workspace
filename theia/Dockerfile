FROM debian:buster-slim

RUN \
	apt-get update && \
	apt-get install -y --no-install-recommends \
		locales=2.28-10 && \
	echo "en_GB.UTF-8 UTF-8" >> /etc/locale.gen && \
	locale-gen en_GB.utf8 && \
	rm -rf /var/lib/apt/lists/*

ENV \
	LC_ALL=en_GB.UTF-8 \
	LANG=en_GB.UTF-8 \
	LANGUAGE=en_GB.UTF-8

RUN \
	apt-get update && \
	apt-get install -y --no-install-recommends \
		ca-certificates \
		dirmngr \
		gnupg2 && \
	rm -rf /var/lib/apt/lists/* && \
	echo "deb https://s3-eu-west-2.amazonaws.com/mirrors.notebook.uktrade.io/debian/ buster main" > /etc/apt/sources.list && \
	echo "deb https://s3-eu-west-2.amazonaws.com/mirrors.notebook.uktrade.io/debian/ buster-updates main" >> /etc/apt/sources.list && \
	echo "Acquire{Check-Valid-Until false; Retries 10;}" >> /etc/apt/apt.conf

RUN \
	apt-get update && \
	apt-get install -y \
		build-essential \
		git \
		curl \
		python3 \
		python3-dev \
		python3-pip \
		sudo && \
	curl -sL https://deb.nodesource.com/setup_10.x | bash - && \
    apt-get install -y nodejs && \
    rm /etc/apt/sources.list.d/nodesource.list && \
    rm -rf /var/lib/apt/lists/*

RUN \
	update-alternatives --install /usr/bin/python python /usr/bin/python3 2 && \
	update-alternatives --install /usr/bin/python python /usr/bin/python2 1

RUN \
    echo '[global]' > /etc/pip.conf && \
    echo 'index-url = https://s3-eu-west-2.amazonaws.com/mirrors.notebook.uktrade.io/pypi/' >> /etc/pip.conf

WORKDIR /root
RUN \
    curl -o- -L https://yarnpkg.com/install.sh | bash

ENV \
	PATH="/root/.yarn/bin:/root/node_modules/.bin:$PATH"

COPY package.json /root
COPY yarn.lock /root

RUN \
	yarn install && \
	yarn theia download:plugins && \
	yarn theia build && \
	yarn cache clean && \
	find /root -type d -exec chmod 755 {} + && \
	chmod -R +r /root

COPY requirements.txt /root

RUN \
	python3 -m pip install pip --upgrade && \
	pip3 install setuptools==49.2.0 --upgrade && \
	pip3 install -r requirements.txt

RUN \
	addgroup --system --gid 4356 theia && \
	adduser --disabled-password --gecos '' --ingroup theia --uid 4357 theia

RUN \
	mkdir /tmp/.yarn-cache && \
	chown theia:theia /tmp/.yarn-cache && \
	touch /root/yarn-error.log && \
	chown theia:theia /root/yarn-error.log && \
	echo "root ALL=(ALL:ALL) ALL" > /etc/sudoers && \
	echo "theia ALL=NOPASSWD:/usr/bin/apt,/usr/bin/apt-get" >> /etc/sudoers && \
	echo 'PS1="\w\\\\$ \[$(tput sgr0)\]"' >> /etc/bash.bashrc && \
	rm /home/theia/.bashrc

COPY vscode_postgres.theia /root/plugins/vscode_postgres.theia
COPY start.sh /start.sh

ENV \
	# Theia by default puts webviews on a subdomain, requests to which I think are intercepted by
	# a service worker. This doesn't work with the locked down DW CSP
	THEIA_WEBVIEW_EXTERNAL_ENDPOINT={{hostname}} \
	SHELL=/bin/bash

CMD ["/start.sh"]
