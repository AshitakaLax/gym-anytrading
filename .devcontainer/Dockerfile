# syntax=docker/dockerfile:1.4
FROM jupyter/tensorflow-notebook as base
COPY requirements.txt /tmp/pip-tmp/
RUN pip3 --disable-pip-version-check --no-cache-dir install -r /tmp/pip-tmp/requirements.txt
COPY .jupyter/jupyter_notebook_config.py /home/jovyan/.jupyter/jupyter_notebook_config.py

CMD ["jupyter", "notebook", "--port=8888", "--ip=0.0.0.0", "--allow-root"]