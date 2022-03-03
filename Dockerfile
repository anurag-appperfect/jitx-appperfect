# FROM 'ubuntu:latest'
# RUN apt-get update
# RUN apt-get install -y python3.8
# RUN apt-get install -y python3-pip
# RUN pip3 install -U pytest
# RUN pip3 install pytest-html
# RUN apt-get update
# RUN apt-get install -y wget unzip
# # Installs the latest internal release, it is 0.11.5-rc.2 on 02/15/2022
# RUN wget https://jitx-staging.s3.amazonaws.com/public/ubuntu-bionic/jitx.zip
# RUN unzip -p jitx.zip jitpcb.release/scripts/install.sh > install.sh
# RUN bash install.sh jitx.zip
# COPY license /root/.jitx/
# COPY refresh_license /root/.jitx/
# COPY user.params /root/.jitx/
# COPY machine-id /etc/
# ENV PATH "$PATH:/root/.jitx/current/"
FROM windows-base-image:latest
SHELL ["C:/msys64/msys2_shell.cmd", "-mingw64", "-no-start", "-defterm", "-here", "--login", "-c"]
RUN pacman -S -q --needed --noconfirm mingw-w64-x86_64-python3 wget unzip
# RUN pip3 install pytest
# RUN pip3 install pytest-html
# # Installs the latest internal release, it is 0.11.5-rc.2 on 02/15/2022
# RUN wget https://jitx-staging.s3.amazonaws.com/public/ubuntu-bionic/jitx.zip
# RUN unzip -p jitx.zip jitpcb.release/scripts/install.sh > install.sh
# RUN bash install.sh jitx.zip
# COPY license /root/.jitx/
# COPY refresh_license /root/.jitx/
# COPY user.params /root/.jitx/
# COPY machine-id /etc/
# ENV PATH "$PATH:/root/.jitx/current/"
