import PySimpleGUI as sg
import matplotlib.pyplot as plt

"""
historical_data.py

This module contains the "historical data" layout and the function to create the chart(line).
I use matplotlib to create the line chart and pysimplegui to create the layout.
"""


def historical_des_layout():
    """
    Function to create the layout of this "Historical data" des.The chatbox and chatinput are non-functional 
    at the moment.Same for the fetch weather button.
    Reference for combo: https://docs.pysimplegui.com/en/latest/cookbook/original/keybad_entry/
    Reference for multiline: https://docs.pysimplegui.com/en/latest/documentation/module/elements/multiline/
    Reference for key: https://docs.pysimplegui.com/en/latest/cookbook/original/keybad_entry/
    Reference for datetime: https://docs.python.org/3/library/datetime.html#module-datetime
    Reference for push: https://docs.pysimplegui.com/en/latest/documentation/module/layouts/#push
    Reference for expand_x: https://docs.pysimplegui.com/en/latest/documentation/module/common_element_parameters/#expand_x-expand_y
    """
    figure_w, figure_h = 700, 400
    layout = [
        [sg.Button('Prev'), sg.Text('Historical Data', font=('Arial', 22), justification='center', expand_x=True), sg.Button('Next')],
        [sg.Text('Data type:'),sg.Combo(['Temperature', 'Humidity', 'Pressure'],default_value='Temperature')], 
        [sg.Text('Year:'), sg.Input(size=(20, 2))],
        [sg.Text('City:'), sg.Input(size=(20, 2))],
        [sg.Canvas(size=(figure_w, figure_h), key='canvas-chart')],
        [sg.Push(), sg.Button('Fetch Weather', size=(20, 2)), sg.Push()],
        [sg.Multiline(size=(60, 5),expand_x=True)],
        [sg.Input(size=(60, 3),expand_x=True)],
        [sg.Push(), sg.Button('Send'),sg.Push()],
        [sg.Push(), sg.Button('Exit')],
    ]
    return layout

def create_historical_chart():
    
    """
    Function to create a line chart about a specific year of a specific data type using dummy data.
    Reference for plt.subplots,ax.set and ax.plot: 
    https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html

    #TODO - For V2:
    The ylabel of my chart should be dynamic. It should change according to the data type selected by the user.
    I will add more data type after looking at the openweather app api documentation and see what is available.
    The title name should be dynamic according to the years selected by the user,the city and the data type(Example: Temperature in Nelson in 1998).
    """
    fig, ax = plt.subplots(figsize=(10, 4))
    categories = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']  
    values = [3, 7, 5, 9, 6, 8, 4, 7, 5, 10, 6, 8]  
    ax.plot(categories, values)  
    ax.set_title("Historical Data")
    ax.set_ylabel("Data type")
    ax.set_xlabel("Months")
    return fig


# if __name__ == '__main__':
#     historical_des_layout()
#     create_historical_chart()