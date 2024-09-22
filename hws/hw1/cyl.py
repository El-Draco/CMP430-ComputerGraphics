import math

def disk_triangle_generator(vertices):
    """Generates triangle faces for a disk using the given vertices."""
    n = len(vertices)
    for i in range(n - 2):
        yield vertices[0], vertices[i + 1], vertices[i + 2]
    # Closing the disk with a final triangle
    yield vertices[0], vertices[-1], vertices[1]


def side_triangle_generator(vertices):
    """Generates side triangle faces using the given vertices."""
    n = len(vertices)
    for i in range(n):
        yield vertices[i], vertices[(i + 1) % n], vertices[(i + 2) % n]

def main(output_to_file=True) -> None:
    # 32 top face + 1 top center + 32 bottom face + 1 bottom center
    num_vertices = 66
    theta = 0
    theta_step = (2 * math.pi) / 32

    # Open file for writing or use print for console output
    if output_to_file:
        output = lambda x: f.write(x)
        f = open('output.obj', 'w')
    else:
        output = print
        f = None

    try:
        # Output vertices
        output('v 0 -1.5 0\n')
        output('v 0 1.5 0\n')

        # Generate vertices
        while abs(theta - 2 * math.pi) > 0.1:
            x = round(math.cos(theta), 5)
            z = round(math.sin(theta), 5)
            output(f'v {x} -1.5 {z}\n')
            output(f'v {x} 1.5 {z}\n')
            theta += theta_step


        vertices = list(range(1, num_vertices + 1))

        # Now generate all the faces
        top_faces = disk_triangle_generator(vertices[1::2])
        bottom_faces = disk_triangle_generator(vertices[0::2])
        side_faces = side_triangle_generator(vertices[2:])

        # Output faces
        for face in top_faces:
            output(f'f {face[0]} {face[1]} {face[2]}\n')
        for face in bottom_faces:
            output(f'f {face[0]} {face[1]} {face[2]}\n')
        for face in side_faces:
            output(f'f {face[0]} {face[1]} {face[2]}\n')

    finally:
        if f:
            f.close()


if __name__ == '__main__':
    # Set the output flag: True for file output, False for console output
    main(output_to_file=True)
