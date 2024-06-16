FROM python:3.9-slim as build

WORKDIR /script
COPY . .

RUN apt-get update && \
    apt-get install -y build-essential python3-dev libatomic1 python3-rpi.gpio
RUN pip3 install -r requirements.txt

FROM python:3.9-slim as development

WORKDIR /script
COPY --from=build /script /script
COPY --from=build /usr/local/lib/python3.9/site-packages /usr/local/lib/python3.9/site-packages
CMD ["sleep", "infinity"]

FROM python:3.9-slim as production

WORKDIR /script
COPY --from=build /script /script
COPY --from=build /usr/local/lib/python3.9/site-packages /usr/local/lib/python3.9/site-packages
CMD ["python", "-u", "mainProtos.py"]
