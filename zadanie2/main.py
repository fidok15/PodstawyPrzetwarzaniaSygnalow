import numpy as np
import matplotlib.pyplot as plt
def sinusoidal_one():
    x = np.arange(0, 4, 0.01)
    y = np.sin(x*np.pi*2)
    plt.plot(x, y, color='green')
    plt.show()

def sinusoida_pare():
    x = np.arange(0, 4, 0.01)
    y = np.sin(x*np.pi*2)
    y2 = np.sin(x*np.pi*1.5)
    y3 = np.sin(x*np.pi*0.75)+np.sin(x*np.pi*1.25)+np.sin(x*np.pi*2.75-1.24)
    _, axs = plt.subplots(2)
    axs[0].plot(x,y2, color='red')
    axs[1].plot(x,y3,color='blue')
    plt.show()

def zabawa():
    plt.style.use('_mpl-gallery')
    _, axs = plt.subplots(2, 1, figsize=(8, 6))

    x = np.arange(0, 4, 0.01)
    y = np.sin(x * np.pi * 2)
    y2 = np.sin(x * np.pi * 1.5)
    y3 = np.sin(x * np.pi * 0.75)

    axs[0].set_title("sinusoidalnie")
    axs[0].plot(x, y, color='green', label='f1')
    axs[0].plot(x, y2, color='red', label='f2')
    axs[0].plot(x, y3, color='blue', label='f3')
    axs[0].set_xlabel("oś X")
    axs[0].set_ylabel("oś Y")
    axs[0].legend()
    axs[0].grid(True)


    y4 = [4.8, 5.5, 3.5, 4.6, 7.5, 6.6, 2.6, 3.0]
    axs[1].set_title("schodkowo")
    axs[1].stairs(y4, linewidth=2.5)
    axs[1].set(xlim=(0, 8), xticks=np.arange(1, 8),
               ylim=(0, 8), yticks=np.arange(1, 8))
    axs[1].set_xlabel("X")
    axs[1].set_ylabel("Y")

    plt.tight_layout()
    plt.show()

def main():
    sinusoidal_one()
    sinusoida_pare()
    zabawa()


if __name__ == "__main__":
    main()
