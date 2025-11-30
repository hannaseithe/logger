from .api import run, MyHttpRequestHandler

def main():
    run(handler_class=MyHttpRequestHandler)

main()