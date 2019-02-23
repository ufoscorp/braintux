path = $(pwd)

cp -r $pwd /opt

echo "alias braintux='/usr/bin/env python3 /opt/braintux/braintux-core.py'" >> ~/.bashrc

env bash -l
