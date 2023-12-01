import eel

# Set web files folder
eel.init('web')

count = 0


data = [["REQ1234-54", "The application shall allow users to import a MS Word document preserving structure of document sections and paragraphs, rich text description of requirements and images."],
        ["REQ1234-74", "The application shall allow users to create a new document from a chosen document template file preserving the structure of document sections and the definition and values of requirement attributes."],
        ]

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
def get_artefact_list():
    return data

@eel.expose
def log_py(msg):
    print(f"js: {msg}")




eel.start('hello.html', size=(300, 200), allowed_extensions=[".html", ".js", ".css", ".woff", ".svg", ".svgz", ".png"])  # Start

