# Plot Graphs 

-   [Description](#description)
-   [Quick start](#Quick-start)
-   [Walk through](#walk-through)
    -   [File structure](#file-structure)
    -   [Final Project](#Final)
    
    
### Description

In this project I get a Json object, split it into ECG and PPG data and display the data as two separate graphs through the Django Web Framework.

### Quick-start

### To run the project, we will enter the following commands:

1. --To run the server -- run following command :

**python manage.py runserver**

2. --To show the graphs -- do the following steps :

**Enter the Postman software --> Click on POST --> 
Enter the next path -- http://127.0.0.1:8000/plot --> Click on Send**



###walk-through

### File-structure

```sh
├── README.md
├── images
├── signals
│   ├── __init__.py
│   ├── asgi.py
│   ├── data.json
│   ├── data_handling.py
│   ├── plots.py
│   ├── settings.py
│   ├── urls.py
│   ├── views.py 
└── ├── wsgi.py

```

## Final

![](/signals/images/gif_plot_graph.gif)
