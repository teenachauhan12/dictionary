def remove_dictionary(colors,a):
    colors=[d for d in colors if d.get('id') != a]
    return colors

colors=[{"id" : "#FF0000", "color" : "Red"}, 
          {"id" : "#800000", "color" : "Maroon"}, 
          {"id" : "#FFFF00", "color" : "Yellow"}, 
          {"id" : "#808000", "color" : "Olive"}] 
print(colors)
r_id = "#FF0000"
print("\nRemove id",r_id,"from the said list of dictionary")
print(remove_dictionary(colors, r_id))









