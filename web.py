form flask inport Flask
app = Flask (__name__)

@app.route('/')
def index():
  return 'hello, world'
