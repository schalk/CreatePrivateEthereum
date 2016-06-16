#!/usr/bin/env python
# -*- coding: utf-8 -*-

## geth --networkid 100 --identity node1 --verbosity 3 --nodiscover --nat none --datadir=~/myblockchain/node1 account new

import sys
import argparse
import subprocess
import json
from subprocess import Popen, PIPE, STDOUT

def load_config_keys(key):
    """ doc """
    file = open("pgeth_config.json", "r")
    txt = file.read()
    file.close()
    d = json.loads(txt)
    return d[key]


def init(args):
    """doc3S"""
    datadir = load_config_keys("datadir")
    # account new
    str_datadir = " --datadir=" + datadir + " "
    str_options =  " --networkid 100 --identity node1 --verbosity 3 --nodiscover --nat none "
    str_args = "geth " + str_datadir + str_options + "account new"
    #p = subprocess.Popen([str_args])
    #.stdin.write("toto\ntoto\n")
    #p.communicate(input="totot\ntoto\n")
    # init
    ##subprocess.call(["geth", str_options, str_datadir, "init"])
    p = Popen(['geth account new'], stdout=PIPE, stdin=PIPE, stderr=STDOUT) 
    grep_stdout = p.communicate(input=b'one\ntwo\nthree\nfour\nfive\nsix\n')[0] 
    print(grep_stdout.decode())
    #print str_args

def start(args):
    """ doc """
    print args

def stop(args):
    """ doc """
    print args

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description = 'to be completed')

    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers()

    init_parser = subparsers.add_parser('init')
    init_parser.set_defaults(func = init)

    start_parser = subparsers.add_parser('start')
    start_parser.set_defaults(func = start)

    stop_parser = subparsers.add_parser('stop')
    stop_parser.set_defaults(func = stop)

    args = parser.parse_args()
    args.func(args)  # call the default function