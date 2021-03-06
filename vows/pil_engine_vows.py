#!/usr/bin/python
# -*- coding: utf-8 -*-

# thumbor imaging service
# https://github.com/globocom/thumbor/wiki

# Licensed under the MIT license:
# http://www.opensource.org/licenses/mit-license
# Copyright (c) 2011 globo.com timehome@corp.globo.com

from pyvows import Vows, expect
ctx = Vows.Context

import thumbor.engines.pil as PIL

@Vows.batch
class PilEngineVows(ctx):

    class ShouldRaiseIfFiltersNotAvailable(ctx):
        def topic(self):
            PIL.FILTERS_AVAILABLE = False
            engine = PIL.Engine(None)
            return engine.paste(None, None, True)

        def should_be_an_error(self, topic):
            expect(topic).to_be_an_error()
            expect(topic).to_be_an_error_like(RuntimeError)
            expect(topic).to_have_an_error_message_of('You need filters enabled to use paste with merge. Please reinstall thumbor with proper compilation of its filters.')

