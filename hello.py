import eel

# Set web files folder
eel.init('web')

count = 0

@eel.expose                         # Expose this function to Javascript
def say_hello_py(x):
    print('Hello from %s' % x)

@eel.expose
def get_data_py():
    global count
    count += 1
    print(f"get_data_py() -> {count}")
    return count

@eel.expose
def log_py(msg):
    print(f"js: {msg}")


eel.start('hello.html', size=(300, 200), allowed_extensions=[".html", ".js", ".css", ".woff", ".svg", ".svgz", ".png"])  # Start

