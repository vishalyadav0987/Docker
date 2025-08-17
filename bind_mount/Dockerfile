FROM python

WORKDIR /myapp


COPY /read.py .



COPY /file.txt /myapp/file.txt
# Host machine (jahan aapka Dockerfile hai) ke file.txt ko
# Container ke andar /myapp/ folder me copy karna.


CMD ["python" , "read.py"]