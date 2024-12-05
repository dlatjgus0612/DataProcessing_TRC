import plotly.graph_objects as go
import pandas as pd

def setpath():
    df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/2014_us_cities.csv')
    df['text'] = df['name'] + '<br>Population ' + (df['pop']/1e6).astype(str) + ' million'
    return df

def setting():
    limits = [(0, 3), (3, 11), (11, 21), (21, 50), (50, 3000)]
    colors = ["royalblue", "crimson", "lightseagreen", "orange", "lightgrey"]
    scale = 5000
    return limits, colors, scale

def ploton(df, limits, colors, scale):
    fig = go.Figure()
    for i in range(len(limits)): 
        lim = limits[i]
        df_sub = df.iloc[lim[0]:lim[1]]
        fig.add_trace(go.Scattergeo(
            locationmode='USA-states',
            lon = df_sub['lon'],
            lat = df_sub['lat'],
            text = df_sub['text'],
            marker=dict(
                size = df_sub['pop']/scale,
                color = colors[i],
                line_color = 'rgb(40,40,40)',
                line_width = 0.5,
                sizemode = 'area'
            ),
            name = f'{lim[0]} to {lim[1]}'
        )) 
    fig.update_layout( 
        title_text = '2014 US city populations<br>(Click legend to toggle traces)',
        showlegend = True,
        geo = dict(scope = 'usa', landcolor = 'rgb(217, 217, 217)')
    )
    fig.show()

if __name__ == "__main__":
    df = setpath()
    limits, colors, scale = setting()
    ploton(df, limits, colors, scale)