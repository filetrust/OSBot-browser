from unittest import TestCase

from osbot_utils.utils.Dev import Dev
from osbot_browser.view_helpers.Go_Js import Go_Js
from osbot_browser.view_helpers.VivaGraph_Js import VivaGraph_Js


class Test_VivaGraph_Js(TestCase):

    def setUp(self):
        self.go_gs = Go_Js()

    def test_load_page(self):
        self.go_gs.load_page()

    #def test_create_graph(self):
    #    (nodes, edges, graph_data, graph_name) = (0,0,0,None)
    #    Dev.pprint(self.go_gs.create_graph(nodes, edges, graph_data, graph_name))


