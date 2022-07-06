FROM python:3.8-slim
WORKDIR /app
COPY . . 

# Install default services
RUN pip install -r requirements.txt
WORKDIR /app/gateway_iac
#ENTRYPOINT ["chalice"]
#CMD ls -lah
CMD ./entrypoint.sh