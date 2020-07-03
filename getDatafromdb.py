import datetime
import sqlite3
from matplotlib import pyplot as plt


date = (datetime.datetime.now() + datetime.timedelta(hours=3)).strftime("%Y-%d-%m %H:%M")


def get_data(command):
    if command == '/btc1' or command == '/btc5':
        db_name = 'DbOf2HourValues.db'
        if command == '/btc1':
            limit = 12
            width = 15
            height = 6
            fontsizex = 7
            fontsizey = 13
        else:
            limit = 60
            width = 20
            height = 6
            fontsizex = 12
            fontsizey = 17

    if command == '/btcm' or command == '/btcy':
        db_name = 'DbOf24HourValues.db'
        if command == '/btcm':
            limit = 30
            width = 20
            height = 6
            fontsizex = 10
            fontsizey = 13
        else:
            limit = 365
            width = 30
            height = 10
            fontsizex = 20
            fontsizey = 20

    def get_data_from_db():
        conn = sqlite3.connect('{}'.format(db_name))

        c = conn.cursor()

        c.execute("SELECT * FROM BTC ORDER BY {} DESC LIMIT {}".format(date, limit))

        output_data = c.fetchall()

        conn.close()

        index_slice = 5
        x, y = [], []
        counter = 0

        for i in output_data:
            xvalue = output_data[counter][0]
            yvalue = output_data[counter][1]
            x.append(xvalue[index_slice:])
            y.append(round(float(yvalue), 1))
            counter += 1
        return x, y

    def draw_graph():
        x = get_data_from_db()[0]
        y = get_data_from_db()[1]

        if limit == 12:
            positions_on_y = [i for i in range(12)]
            positions_names = x[::1]
            rotation = 20

        if limit == 30:
            positions_on_y = [i for i in range(30)]
            positions_names = x[::1]
            rotation = 20

        if limit == 60:
            positions_on_y = [i for i in range(0, 60, 5)]
            positions_names = x[::2]
            rotation = 20

        if limit == 365:
            positions_on_y = [0, 31, 60, 91, 121, 152, 182, 213, 243, 274, 304, 335]
            positions_names = [x[0], x[31], x[60], x[91], x[121], x[152],
                               x[182], x[213], x[243], x[274], x[304], x[335]]
            rotation = 0

        plt.figure(figsize=(width, height))

        ax = plt.axes()
        ax.set_facecolor('#36393f')

        plt.plot(x, y, linestyle='solid', color='#46f148',)

        ymax = max(y)
        ymin = min(y)
        xmaxpos, xminpos = y.index(ymax), y.index(ymin)
        xmax, xmin = x[xmaxpos], x[xminpos]

        ax.annotate('{}'.format(ymax), xy=(xmax, ymax), xytext=(x[xmaxpos], ymax),
                    fontsize=fontsizey, weight='black', color='white', ha='center', va='baseline',)
        ax.annotate('{}'.format(ymin), xy=(xmin, ymin), xytext=(x[xminpos], ymin),
                    fontsize=fontsizey, weight='black', color='white', va='bottom')
        ax.annotate('{}'.format(y[-1]), xy=(x[-1], y[-1]), xytext=(x[-1], y[-1]),
                    fontsize=fontsizey, weight='black', color='white', ha='left', va='baseline',)

        props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
        text = 'max = {}\nmin = {}'.format(ymax, ymin)

        ax.text(x.index(x[-1]), ymax, text, fontsize=fontsizey, color='black', verticalalignment='top',
                horizontalalignment='right', bbox=props)

        plt.tight_layout(rect=[0.01, 0.05, 1, 1])
        plt.grid(color='grey')
        plt.yticks(fontsize=fontsizey, color='white')
        plt.xticks(positions_on_y,
                   positions_names,
                   color='white',
                   fontsize=fontsizex,
                   rotation=rotation)

        plt.savefig('graph.jpeg', facecolor='#2f3136')
        photo = open('graph.jpeg', 'rb')
        return photo
    return draw_graph()