# syntax=docker/dockerfile:1.4
FROM jupyter/tensorflow-notebook as base
COPY requirements.txt /tmp/pip-tmp/
USER root 
RUN apt-get update --yes && apt-get install --yes xvfb
#RUN |3 NB_USER=jovyan NB_UID=1000 NB_GID=100 /bin/bash -o pipefail -c apt-get update --yes && apt-get upgrade --yes && apt-get install --yes --no-install-recommends bzip2 ca-certificates locales sudo tini wget && apt-get clean && rm -rf /var/lib/apt/lists/* && echo "en_US.UTF-8 UTF-8" > /etc/locale.gen && locale-gen # buildkit
USER 1000
RUN pip3 --disable-pip-version-check --no-cache-dir install -r /tmp/pip-tmp/requirements.txt
COPY .jupyter/jupyter_notebook_config.py /home/jovyan/.jupyter/jupyter_notebook_config.py

CMD ["jupyter", "notebook", "--port=8888", "--ip=0.0.0.0", "--allow-root"]