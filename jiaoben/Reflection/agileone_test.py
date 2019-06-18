#! /usr/bin/env python
# -*- coding: utf-8 -*-


class AgileoneTest:

    def open_browser(self, url):
        print('open homepage %s' % url)

    def input_text(self, locator, content):
        print('input %s at %s.' % (content, locator))

    def input_password(self, locator, password):
        self.input_text(locator, password)

    def on_click(self, locator):
        print('on click button at %s.' % locator)

    def wait(self, delay):
        print('wait %ss.' % delay)

    def close_browser(self):
        print('close browser.')
