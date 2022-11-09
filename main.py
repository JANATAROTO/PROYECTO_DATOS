from graph import *
import safe
import draw_map
import time


def main():
    #Empieza el temporizador
    start_time = time.time()
    print('Loading graph...')
    #Crear un gráfico con el primer tipo de riesgo de acoso
    graph = create_graph(1)

    #primer testeo: Universidad de Antioquia -> Universidad Nacional
    print("First test: Universidad de Antioquia -> Universidad Nacional")
    path, path_names, distance, distance_harassment = safe.shortest_safest_path(graph, (-75.5694416, 6.2650137),(-75.5762232, 6.266327))
    print("Path: ", path)
    print("Path names: ", path_names)
    print("Distance: ", distance)
    print("Distance-harassment: ", distance_harassment)
    print("----------------------------------------")
    draw_map.draw_map(path)
    #Termina el temporizador y lo printea
    print("Time: ", time.time() - start_time)
    print()

    #Corre el temporizador
    start_time = time.time()
    print('Loading graph...')
    #crea el grafico
    graph = create_graph(2)

    
    print("Second test: Universidad EAFIT -> Universidad de Medellin")
    path, path_names, distance, distance_harassment = safe.shortest_safest_path(graph, (-75.5769749, 6.2056892),
                                                                                    (-75.6348967, 6.2704309))
    print("Path: ", path)
    print("Path names: ", path_names)
    print("Distance: ", distance)
    print("Distance-harassment: ", distance_harassment)
    print("----------------------------------------")
    draw_map.draw_map(path)
    
    print("Time: ", time.time() - start_time)
    print()

    
    start_time = time.time()
    print('Loading graph...')
    
    graph = create_graph(3)

    
    print("Third test: Universidad Nacional -> Universidad Luis Amigó")
    path, path_names, distance, distance_harassment = safe.shortest_safest_path(graph, (-75.609497, 6.2581403),
                                                                                    (-75.6348967, 6.2704309))
    print("Path: ", path)
    print("Path names: ", path_names)
    print("Distance: ", distance)
    print("Distance-harassment: ", distance_harassment)
    print("----------------------------------------")
    draw_map.draw_map(path)
    
    print("Time: ", time.time() - start_time)
    print()


if __name__ == '__main__':
    main()
