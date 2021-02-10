from unittest import TestCase

from osbot_utils.utils.Dev import Dev

#
#<script src="https://cdnjs.cloudflare.com/ajax/libs/vivagraphjs/0.10.1/vivagraph.min.js"></script>
from osbot_browser.view_helpers.View_Examples import View_Examples


class Test_View_Examples(TestCase):
    def setUp(self):
        self.headless      = False
        self.view_examples = View_Examples('/tmp/test_screenshot_html.png',self.headless)
        self.clip          = {'x': 1, 'y': 1, 'width': 520, 'height': 50}

    def test_hello_world_content(self):
        result = self.view_examples.hello_world__html()
        assert '<h1>Hello World.....</h1>' in result.html()

    def test_hello_world    (self): self.view_examples.set_clip(self.clip).hello_world()
    def test_bootstrap_cdn  (self): self.view_examples.set_clip(self.clip).bootstrap_cdn()
    def test_folder_root    (self): self.view_examples.folder_root()

    def test_visjs_simnple  (self): self.view_examples.render_file_from_zip('/examples/vis-js.html')

    def test_render_file_from_zip(self): self.view_examples.render_file_from_zip('/examples/hello-world.html')

    def test_open_file_in_browser__markdown(self):
        result = self.view_examples.open_file_in_browser('/examples/markdown.html')
        Dev.pprint(result)

    def test_open_file_in_browser__markdown_with_js(self):
        js_code= { 'name': 'convert', 'params' : '# aaaa \n 123 \n - bullet point \n - another one ![](http://visjs.org/images/gettingstartedSlide.png)'}
        result = self.view_examples.open_file_in_browser('/examples/markdown.html',js_code)
        Dev.print(result('#md_html').html())

    def test_open_file_in_browser__r1_and_r2(self):
        result = self.view_examples.open_file_in_browser('/gs/risk/r1-and-r2.html')
        Dev.pprint(result)

    def test_open_file_in_browser__vivagraph(self):
        result = self.view_examples.open_file_in_browser('/vivagraph/first-test.html')
        Dev.pprint(result)

    def test_open_file_in_browser__go_gs(self):
        result = self.view_examples.open_file_in_browser('/go-js/simple.html')
        Dev.pprint(result)

    def test_open_file_in_browser__full_calendar(self):
        result = self.view_examples.open_file_in_browser('/full-calendar/test.html')
        Dev.pprint(result)
