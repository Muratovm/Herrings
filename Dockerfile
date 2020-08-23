FROM python:3
WORKDIR /
COPY server.py /
EXPOSE 8080
#CMD ["python", "-c", "print('running server script')"]
CMD ["python", "-u", "server.py"]
# CMD ["tail", "-f", "/dev/null"]