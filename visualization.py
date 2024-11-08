import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def plot_path_and_obstacles(path, obstacles, goal):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    x_path = [p[1] for p in path]
    y_path = [p[2] for p in path]
    z_path = [p[0] for p in path]

    x_obstacles = [o[1] for o in obstacles]
    y_obstacles = [o[2] for o in obstacles]
    z_obstacles = [o[0] for o in obstacles]

    ax.plot(x_path, y_path, z_path, color='blue', marker='o', label='Path')
    ax.scatter(x_obstacles, y_obstacles, z_obstacles, color='red', label='Obstacles', s=50)
    ax.scatter(goal[1], goal[2], goal[0], color='green', label='Goal', s=100)

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Layer')
    ax.set_title('Optimal Path with Dynamic Obstacles')
    ax.legend()
    plt.show()

