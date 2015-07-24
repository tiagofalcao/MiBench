#!/usr/bin/env python
# encoding: utf-8

APPNAME="MiBench"
VERSION="1.0"

top = '.'
out = 'build'

def options(ctx):
    ctx.load('compiler_c')

def configure(ctx):
    print("Configure from: " + ctx.path.abspath())
    import os

    prefix  = ctx.env.PREFIX
    datadir = ctx.env.DATADIR
    if not datadir:
        ctx.env.DATADIR = os.path.join(prefix,'share', APPNAME)

    ctx.start_msg("Prefix")
    ctx.end_msg(ctx.env.PREFIX)

    ctx.start_msg("Data directory")
    ctx.end_msg(ctx.env.DATADIR)

    ctx.load('compiler_c')
    ctx.env.append_unique('LIB', 'm')

    abspath = ctx.path.abspath()
    for subdir in os.listdir(abspath):
        path = os.path.join(abspath, subdir)
        if not os.path.isdir(path): continue
        if not os.path.isfile(os.path.join(path, "wscript")): continue

        ctx.recurse(subdir)

    #print(ctx.env)


def dist(ctx):
    #print("Building ditribution...")

    import os
    abspath = ctx.path.abspath()
    for subdir in os.listdir(abspath):
        path = os.path.join(abspath, subdir)
        if not os.path.isdir(path): continue
        if not os.path.isfile(os.path.join(path, "wscript")): continue

        ctx.recurse(subdir)


def build(ctx):
    print("Build from: " + ctx.path.abspath())

    import os
    abspath = ctx.path.abspath()
    for subdir in os.listdir(abspath):
        path = os.path.join(abspath, subdir)
        if not os.path.isdir(path): continue
        if not os.path.isfile(os.path.join(path, "wscript")): continue

        ctx.recurse(subdir)
