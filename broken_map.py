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
    __STRATEGY = 'stupid_strategy'

    def __init__(self):
        ox.config(use_cache=True)
        self.G = ox.graph_from_point((56.835555, 60.600893), dist=6500, simplify=False,
                                     network_type=GraphMap.__NETWORK_TYPE, retain_all=False)
        # print(self.G)

        self.nodes_list = list(self.G.nodes())
        self.fig, self.ax, self.rnd_node = (0, 0, 0)

        if self.G:
            self.draw()

    def draw(self):
        self.fig, self.ax = ox.plot_graph(self.G, node_size=0,
                                          dpi=1600, save=False, edge_alpha=1)

        if self.fig:
            self.save_img_png()

    def save_img_png(self):
        self.fig.tight_layout(pad=0)
        self.fig.savefig('yekaterinburg.png', dpi=300, bbox_inches='tight', format=GraphMap.__IMG_FORMAT_SAVE,
                         facecolor=self.fig.get_facecolor(), transparent=False)

    def get_random_node(self):
        self.rnd_node = random.choice(self.nodes_list)
        self.nodes_list.remove(self.rnd_node)

        return self.rnd_node

    def get_path_time_min(self, start_point, end_point):
        time = nx.shortest_path_length(self.G, start_point, end_point, weight=GraphMap.__TRAVEL_TIME)
        # print(time)

        return time

    def get_path_dist_m(self, start_point, end_point):
        dist = nx.shortest_path(self.G, start_point, end_point, weight=GraphMap.__TRAVEL_TIME)
        # print(dist)


        return sum(dist)

    def save_path_img_png(self, start_point, end_point):
        fgi, an = ox.plot_graph_route(self.G, self.get_path_dist_m(start_point=start_point, end_point=end_point))
        fgi.tight_layout(pad=0)
        fgi.savefig('yekaterinburg.png', dpi=300, bbox_inches='tight', format=GraphMap.__IMG_FORMAT_SAVE,
                    facecolor=fgi.get_facecolor(), transparent=False)

    def get_strategy(self):
        return GraphMap.__STRATEGY

    def closer_taxi_to_client(self, taxi_container, client_gps):
        bestDistance = 999999999999999999999999999
        bestTaxi = None

        for taxi in taxi_container:
            try:
                currentDistance = self.get_path_dist_m(client_gps, taxi.gps)

                if bestDistance > currentDistance:
                    bestDistance = currentDistance
                    bestTaxi = taxi
            except:
                continue

        return bestTaxi












        # print('Начинаем искать')
        #
        # left_list_el, right_list_el = 0, len(taxi_container) - 1
        # #
        # # # is_client_gps = True if client_gps in taxi_container.gps else False
        # #
        # # if client_gps == taxi_container[left_list_el].gps or \
        # #         client_gps == taxi_container[right_list_el].gps:
        # #
        # #     lle_time_min = self.get_path_time_min(taxi_container[left_list_el].gps, client_gps)
        # #     rle_time_min = self.get_path_time_min(taxi_container[right_list_el].gps, client_gps)
        # #
        # #     if lle_time_min < rle_time_min:
        # #         print('закончили искать')
        # #
        # #         return taxi_container[left_list_el]
        # #
        # #     print('закончили искать')
        # #
        # #     return taxi_container[right_list_el]
        #
        # while left_list_el < right_list_el:
        #     # if is_client_gps:
        #     #     if right_list_el % left_list_el == 2:
        #     #         lle_time_min = self.get_path_time_min(taxi_container[left_list_el].gps, client_gps)
        #     #         rle_time_min = self.get_path_time_min(taxi_container[right_list_el].gps, client_gps)
        #     #
        #     #         if lle_time_min < rle_time_min:
        #     #             return taxi_container[left_list_el]
        #     #
        #     #         return taxi_container[right_list_el]
        #     #
        #     #     if taxi_container[left_list_el].gps < client_gps and \
        #     #             client_gps % taxi_container[left_list_el].gps > 0:
        #     #         left_list_el += 1
        #     #
        #     #     if taxi_container[right_list_el].gps > client_gps and \
        #     #             taxi_container[right_list_el].gps % client_gps > 0:
        #     #         right_list_el -= 1
        #     #
        #     # else:
        #     #
        #     # if right_list_el % left_list_el == 1:
        #     #     lle_time_min = self.get_path_time_min(taxi_container[left_list_el].gps, client_gps)
        #     #     rle_time_min = self.get_path_time_min(taxi_container[right_list_el].gps, client_gps)
        #     #
        #     #     if lle_time_min < rle_time_min:
        #     #         print('закончили искать')
        #     #
        #     #         return taxi_container[left_list_el]
        #     #
        #     #     print('закончили искать')
        #     #
        #     #     return taxi_container[right_list_el]
        #
        #     if taxi_container[left_list_el].gps < client_gps:
        #         left_list_el += 1
        #
        #     if taxi_container[right_list_el].gps > client_gps:
        #         right_list_el -= 1
        #
        # lle_time_min = self.get_path_time_min(taxi_container[left_list_el].gps, client_gps)
        # rle_time_min = self.get_path_time_min(taxi_container[right_list_el].gps, client_gps)
        #
        # if lle_time_min < rle_time_min:
        #     print('закончили искать')
        #     return taxi_container[left_list_el]
        #
        # print('закончили искать')
        # return taxi_container[right_list_el]






# y_graph = GraphMap()

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
