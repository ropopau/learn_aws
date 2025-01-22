#!/usr/bin/env python3

import aws_cdk as cdk
from lib.stack import Stck

app = cdk.App()
Stck(app, "MainStack")

app.synth()
