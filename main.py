from website import create_app

app = create_app()

if __name__ == '_ _main__':
  app.run(debug = True)