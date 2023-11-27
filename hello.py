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


eel.start('hello.html', size=(300, 200))  # Start

