import random

import networkx as nx
import osmnx as ox

##################################

#          (ﾉ◕ヮ◕)ﾉ*:･ﾟ✧          #
# conjuring a code for good luck #

##################################

#######################################

# пока на похуй пишу - потом поправлю #


#######################################

class GraphMap:
    __PLACE = ["Yekaterinburg, Russia"]
    __NETWORK_TYPE = 'drive'
    __IMG_FORMAT_SAVE = 'png'
    __TRAVEL_TIME = 'travel_time'

    fig: int

    def __init__(self):
        self.G = ox.graph_from_place(GraphMap.__PLACE, simplify=True,
                                     network_type=GraphMap.__NETWORK_TYPE, retain_all=False)
        print(self.G)

        self.nodes_list = list(self.G.nodes())
        self.ax, self.rnd_node = (0, 0)

        if self.G:
            self.draw()

    def draw(self):
        self.fig, self.ax = ox.plot_graph(self.G, node_size=0,
                                          dpi=1600, save=False, edge_alpha=1)

        if self.fig:
            self.save_img_png()

    @classmethod
    def save_img_png(cls):
        cls.fig.tight_layout(pad=0)
        cls.fig.savefig('yekaterinburg.png', dpi=300, bbox_inches='tight', format=GraphMap.__IMG_FORMAT_SAVE,
                         facecolor=cls.fig.get_facecolor(), transparent=False)

    def get_random_node(self):
        self.rnd_node = random.choice(self.nodes_list)
        self.nodes_list.remove(self.rnd_node)

        return self.rnd_node

    def get_path_time_min(self, start_point, end_point):
        time = nx.shortest_path_length(self.G, start_point, end_point, weight=GraphMap.__TRAVEL_TIME)
        print(time)

        return time

    def get_path_dist_m(self, start_point, end_point):
        dist = nx.shortest_path(self.G, start_point, end_point, weight=GraphMap.__TRAVEL_TIME)
        print(dist)

        return dist

    def save_path_img_png(self, ):
        fgi, an = ox.plot_graph_route(self.G, self.get_path_dist_m())
        fgi.tight_layout(pad=0)
        fgi.savefig('yekaterinburg.png', dpi=300, bbox_inches='tight', format=GraphMap.__IMG_FORMAT_SAVE,
                         facecolor=self.fgi.get_facecolor(), transparent=False)

y_graph = GraphMap()

# place = ["Yekaterinburg, Russia"]
# G = ox.graph_from_place(place, simplify=True, network_type='drive', retain_all=False)
# print(G)
#
# print(G.edges())
#
# fig, ax = ox.plot_graph(G, node_size=0,
#                         dpi=1600,
#                         save=False, edge_alpha=1)
# print(fig)
#
# begin = random.choice(list(G.nodes))
# end = random.choice(list(G.nodes))
#
# route = nx.shortest_path(G, begin, end, weight='travel_time')
# time = nx.shortest_path_length(G, begin, end, weight='travel_time')
# print(time)
#
# fgi, an = ox.plot_graph_route(G, route)
#
# print(fgi)

# создать класс который поможет по static получать gps
# дистанция, время от точки до точки
# Метод для получения списка такси, которое прибудет менее чем за 15 минут до клиента. При этом is_busy = False
