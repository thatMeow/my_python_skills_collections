figs = []
traces = []
for i, cl in enumerate(df.index):
    traces.append(    
        go.Bar(
    x=[df.columns[0],df.columns[1]
      ,df.columns[2],df.columns[3]],
    y=[df.ix[i,0],df.ix[i,1]
      ,df.ix[i,2],df.ix[i,3]],
    name=df.index[i],
    marker=dict(color=cof_pal[i]
    )
   )
)
data = traces
            
layout = go.Layout(showlegend=True, title="example_1", font=dict(size=Chart_Title_Font_Size),
                   yaxis=dict(title='sample title', titlefont=dict(size=yaxis_font_size)
                              , tickfont=dict(size=yaxis_font_size)),
                   xaxis=dict(title='sample x axis', titlefont=dict(size=xaxis_font_size)
                              , tickfont=dict(size=yaxis_font_size))
                  )

fig = go.Figure(data=data, layout=layout)
iplot(fig, filename='example_plot')
figs.append(fig)
