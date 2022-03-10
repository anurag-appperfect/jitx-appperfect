FROM 657302324634.dkr.ecr.us-west-2.amazonaws.com/mingw-base
SHELL ["C:/msys64/msys2_shell.cmd", "-mingw64", "-no-start", "-defterm", "-here", "--login", "-c"]

COPY ./provision C:/jitx/provision
WORKDIR C:/jitx
RUN ./provision
