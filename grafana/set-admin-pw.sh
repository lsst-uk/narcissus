#!/bin/sh

ADMINPASS=$(openssl rand -base64 8 | tr -d =)
echo "$ADMINPASS" > /root/grafana.admin.password.txt
echo "Set Grafana admin password to $ADMINPASS"
grafana-cli --config="/etc/grafana/grafana.ini" admin reset-admin-password $ADMINPASS

