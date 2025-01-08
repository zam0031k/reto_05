from reto_05.shape_01.shape_01 import *

def main():
    print("RECTÁNGULO") 
    rectangle = Rectangle(Point(0, 0), width=4, height=2)

    print("Área del rectángulo:", rectangle.compute_area())
    print("Perímetro del rectángulo:", rectangle.compute_perimeter())
    print("Vértices:", rectangle.get_vertices())
    print("Bordes:", rectangle.get_edges())
    print("Longitudes de los lados:", rectangle.get_edge_lengths())
    print("Ángulos internos:", rectangle.get_inner_angles())

    print("\nCUADRADO")
    square = Square(Point(0,0), side=5)

    print("Área del cuadrado:", square.compute_area())
    print("Perímetro del cuadrado:", square.compute_perimeter())
    print("Vértices:", square.get_vertices())
    print("Bordes:", square.get_edges())
    print("Longitudes de los lados:", square.get_edge_lengths())
    print("Ángulos internos:", square.get_inner_angles())

    print("\nTRIÁNGULO")
    tri = Triangle(Point(0, 0), Point(3, 0), Point(0, 4))

    print("Área del triangulo:", tri.compute_area())
    print("Perimetro del triangulo:", tri.compute_perimeter())
    print("Vértices:", tri.get_vertices())
    print("Bordes:", tri.get_edges())
    print("Longitudes de los lados:", tri.get_edge_lengths())
    print("Ángulos internos:", tri.get_inner_angles())

    print("\nTRIÁNGULO EQUILÁTERO")
    eq = Equilateral(Point(0, 0), side=5)

    print("Área de un triangulo equilátero:", eq.compute_area())
    print("Perimetro de un triangulo equilátero:", eq.compute_perimeter())
    print("Vértices:", eq.get_vertices())
    print("Bordes:", eq.get_edges())    
    print("Longitudes de los lados:", eq.get_edge_lengths())
    print("Ángulos internos:", eq.get_inner_angles())

    print("\nTRIÁNGULO ISOSCELES")
    iso = Isosceles(Point(0, 0), base=4, side=5)

    print("Área del triangulo isosceles:", iso.compute_area())
    print("Perimetro de un triangulo equilátero:", iso.compute_perimeter())
    print("Vértices:", iso.get_vertices())
    print("Bordes:", iso.get_edges())
    print("Longitudes de los lados:", iso.get_edge_lengths())
    print("Ángulos internos:", iso.get_inner_angles())

    print("\nTRIÁNGULO ESCALENO")
    sca = Scalene(Point(0, 0), Point(4, 0), Point(2, 3))

    print("Área del triangulo isosceles:", sca.compute_area())
    print("Perimetro de un triangulo equilátero:", sca.compute_perimeter())
    print("Vértices:", sca.get_vertices())
    print("Bordes:", sca.get_edges())
    print("Longitudes de los lados:", sca.get_edge_lengths())
    print("Ángulos internos:", sca.get_inner_angles())

    print("\nTRIÁNGULO RECTÁNGULO")
    tri_rect = TriRectangle(Point(0, 0), base=3, height=4)

    print("Área del triangulo isosceles:", tri_rect.compute_area())
    print("Perimetro de un triangulo equilátero:", tri_rect.compute_perimeter())
    print("Vértices:", tri_rect.get_vertices())
    print("Bordes:", tri_rect.get_edges())
    print("Longitudes de los lados:", tri_rect.get_edge_lengths())
    print("Ángulos internos:", tri_rect.get_inner_angles())

if __name__ == "__main__":
    main()  