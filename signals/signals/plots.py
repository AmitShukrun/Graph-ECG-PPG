import matplotlib.pyplot as plt
from io import BytesIO


def plot_graph(ecg, ppg):  # Create graphs for the ECG and PPG data.

    plt.switch_backend('Agg')   # Ask matplotlib to write graphs to an image instead of opening a window

    plot, (ch1, ch2) = plt.subplots(2)
    plot.subplots_adjust(hspace=0.5)

    ch1.plot(ecg)
    ch1.set_title('ECG')

    ch2.plot(ppg)
    ch2.set_title('PPG')

    return plot


def get_chart_as_image(plot):  #Transform matplotlib chart into an image.

    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()
    return image_png
