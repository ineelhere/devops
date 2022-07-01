FROM ubuntu:latest
RUN apt-get update \
    && apt-get install -y git \
    && apt-get install -y figlet;

RUN apt-get install -y python3-pip \
    && git clone -b dockers https://github.com/ineelhere/devops.git \
    && pip3 install -r ./devops/requirements.txt;

EXPOSE 8501
ENTRYPOINT ["streamlit", "run"]
CMD ["./devops/app.py"]