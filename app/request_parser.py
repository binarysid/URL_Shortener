from flask_restx import reqparse

class RequestParser:
    def __init__(self,arg,type,location):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument(arg,type=type,location=location)
        
    def getParser(self):
        return self.parser

    def parse_args(self):
        return self.parser.parse_args()
