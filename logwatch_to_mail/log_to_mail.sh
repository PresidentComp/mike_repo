#!/bin/bash

logwatch --detail Med --mailto root --service sshd vsftpd --range yesterday
