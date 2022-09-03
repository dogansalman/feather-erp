FROM ubuntu 

RUN apt-get update 
RUN apt-get install python3-pip
RUN apt-get install flask
# requirements.txt pip install yapmak lazım yoksa tek tek her paketi eklemek durumunda kalınabilir...
ADD app.py /
WORKDIR /

# Port
EXPOSE 5000 

# python3 server.py 
# ubuntu'da python3 server.py olarak çalışıyor olabilir ama wincmd de python server.py olarak ayağa kalkıyor
CMD ["python3","server.py"]