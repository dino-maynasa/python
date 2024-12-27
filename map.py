import folium

m = folium.Map(location=[-16.5000, -68.1500], zoom_start=13)

folium.CircleMarker(
    location=[-16.5000, -68.1500],
    radius=50,
    popup='La Paz, Bolivia',
    color='#3186cc',
    fill=True,
    fill_color='#3186cc'
).add_to(m)

m.save('mapa.html')