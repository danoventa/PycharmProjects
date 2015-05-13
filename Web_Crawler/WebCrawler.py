page =('<div id="top_bin"><div id="top_content" class="width960">'
'<div class="udacity float-left"><a href="http://udacity.com">')
start_link = page.find('<a href=')

start = page.find('"', start_link) + 1
end = page.find('"', start + 1)

url = page[start : end]

print(url)