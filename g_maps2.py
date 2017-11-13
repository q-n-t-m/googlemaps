import googlemaps

gmaps = googlemaps.Client(key='AIzaSyD872uTbM8dkSusVD9HvbG_W2Ggkb1K6cE')

# how I attempted the problem initially

#directions_ = gmaps.directions('London n8 8pt', 'London ec2y 9AR')
#direction_start = directions_[0]['legs'][0]['steps'][0]['html_instructions']
#direction_end = directions_[0]['legs'][0]['steps'][11]['html_instructions']
#print(direction_start)
#print(direction_end)


# here is the correct answer:

def my_get_directions(add1, add2):
    direction_result = gmaps.directions(add1, add2)
    list_of_directions = []
    list_of_steps = direction_result[0]['legs'][0]['steps']

    for s in list_of_steps:
        list_of_directions.append(s['html_instructions'])

    for j in list_of_directions:
        formatted_string = my_format_string(j)
        splitted_string = break_on_continue(formatted_string, 'Continue')
        splitted_string = break_on_continue(formatted_string, 'Destination')
        print(splitted_string)

def my_format_string(string_in):
    string_out = string_in.replace('<div>', '')
    string_out = string_out.replace('</div>', '')
    string_out = string_out.replace('<b>', '')
    string_out = string_out.replace('</b>', '')
    string_out = string_out.replace('<div style="font-size:0.9em">', '')
    string_out = string_out.replace('Ln', 'Lane')
    string_out = string_out.replace('Ave', 'Avenue')
    return string_out

def break_on_continue(string_in, word_in):
    string_list = string_in.split(word_in)
    word_in_with_new_line = '\n' + word_in
    string_out = word_in_with_new_line.join(string_list)
    return string_out