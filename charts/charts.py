import matplotlib.pyplot as plt

def generate_pie_chart():
    labels = ['a','b','c']
    values = [200, 500, 700]

    fig, ax = plt.subplots()
    ax.pie(values, labels = labels)
    plt.savefig('pie.png')
    plt.close()