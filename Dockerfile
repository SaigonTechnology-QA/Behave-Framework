FROM baseImage


WORKDIR /the/workdir/path


COPY source dest

RUN command

CMD [ "executable" ]

ENV key=value
