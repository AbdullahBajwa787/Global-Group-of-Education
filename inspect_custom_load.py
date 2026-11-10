with open('public/assets/js/custom.js', 'r', encoding='utf-8', errors='ignore') as f:
    js = f.read()

pos = js.find("$(window).on('load'")
if pos == -1:
    pos = js.find("$wn.on('load'")
print("Found $wn.on('load'):", pos)
print(js[pos:pos+500])
